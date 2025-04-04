import base64
import hashlib
import json
import logging
import time
import urllib.parse
from typing import Dict, Any, List, Optional, Tuple
import jwt
from jwcrypto import jwk
import redis
import requests
from auth_proxy.auth_plugins.base import AuthPlugin, AuthResult, PluginPath

logger = logging.getLogger(__name__)


class SessionStore:
    """Abstract base class for session storage"""

    def get(self, session_id: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError()

    def set(self, session_id: str, data: Dict[str, Any], ttl: int = 3600) -> None:
        raise NotImplementedError()

    def delete(self, session_id: str) -> None:
        raise NotImplementedError()


class RedisSessionStore(SessionStore):
    """Redis-based session storage"""

    def __init__(
        self,
        redis_url: str,
        prefix: str = "oidc_session:",
        encryption_key: Optional[str] = None,
        salt: str = "auth_proxy_oidc_salt",
    ):
        self.redis = redis.from_url(redis_url)
        self.prefix = prefix

        # Set up encryption if key is provided
        self.fernet = None
        if encryption_key:
            # Derive a key from the provided encryption key
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            from cryptography.fernet import Fernet

            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt.encode(),
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(encryption_key.encode()))
            self.fernet = Fernet(key)

    def get(self, session_id: str) -> Optional[Dict[str, Any]]:
        key = f"{self.prefix}{session_id}"
        data = self.redis.get(key)
        if not data:
            return None

        # Decrypt if encryption is enabled
        if self.fernet:
            try:
                data = self.fernet.decrypt(data)
            except Exception as e:
                logger.error(f"Failed to decrypt session data: {e}")
                return None

        try:
            return json.loads(data)
        except json.JSONDecodeError:
            logger.error("Failed to decode session data")
            return None

    def set(self, session_id: str, data: Dict[str, Any], ttl: int = 3600) -> None:
        key = f"{self.prefix}{session_id}"
        json_data = json.dumps(data)

        # Encrypt if encryption is enabled
        if self.fernet:
            json_data = self.fernet.encrypt(json_data.encode())
        else:
            json_data = json_data.encode()

        self.redis.setex(key, ttl, json_data)

    def delete(self, session_id: str) -> None:
        key = f"{self.prefix}{session_id}"
        self.redis.delete(key)


class MemorySessionStore(SessionStore):
    """In-memory session storage (for development only)"""

    def __init__(self):
        self.sessions = {}
        self.expiry = {}
        logger.warning("Using in-memory session store - NOT RECOMMENDED FOR PRODUCTION")

    def get(self, session_id: str) -> Optional[Dict[str, Any]]:
        if session_id not in self.sessions:
            return None

        # Check if session has expired
        if session_id in self.expiry and self.expiry[session_id] < time.time():
            self.delete(session_id)
            return None

        return self.sessions[session_id]

    def set(self, session_id: str, data: Dict[str, Any], ttl: int = 3600) -> None:
        self.sessions[session_id] = data
        self.expiry[session_id] = time.time() + ttl

    def delete(self, session_id: str) -> None:
        if session_id in self.sessions:
            del self.sessions[session_id]
        if session_id in self.expiry:
            del self.expiry[session_id]


class JWKSCache:
    """Cache for JWKS keys with conversion to PEM format"""
    def __init__(self, jwks_uri: str, cache_ttl: int = 3600):
        self.jwks_uri = jwks_uri
        self.cache_ttl = cache_ttl
        self.keys = {}  # Original JWK format
        self.pem_keys = {}  # PEM format for PyJWT
        self.last_updated = 0
    
    def get_key(self, kid: str) -> Optional[str]:
        """Get a key by its ID in PEM format, refreshing the cache if needed"""
        current_time = time.time()
        
        # Refresh cache if expired or if the requested key is not in the cache
        if current_time - self.last_updated > self.cache_ttl or kid not in self.pem_keys:
            self._refresh_keys()
        
        return self.pem_keys.get(kid)
    
    def _refresh_keys(self) -> None:
        """Refresh the JWKS keys from the provider and convert to PEM format"""
        try:
            response = requests.get(self.jwks_uri, timeout=10)
            response.raise_for_status()
            jwks_data = response.json()
            
            # Store original JWK format keys
            self.keys = {key.get('kid'): key for key in jwks_data.get('keys', [])}
            
            # Convert each key to PEM format
            self.pem_keys = {}
            for kid, key_data in self.keys.items():
                try:
                    # Convert JWK to PEM
                    key = jwk.JWK.from_json(json.dumps(key_data))
                    if key_data.get('kty') == 'RSA':
                        pem_key = key.export_to_pem(private_key=False, password=None)
                        self.pem_keys[kid] = pem_key
                    elif key_data.get('kty') == 'EC':
                        pem_key = key.export_to_pem(private_key=False, password=None)
                        self.pem_keys[kid] = pem_key
                    else:
                        logger.warning(f"Unsupported key type: {key_data.get('kty')}")
                except Exception as e:
                    logger.error(f"Failed to convert key {kid} to PEM format: {e}")
            
            self.last_updated = time.time()
            
        except Exception as e:
            logger.error(f"Failed to refresh JWKS keys: {e}")
            # If this is the first time, raise the error
            if self.last_updated == 0:
                raise

class OIDCAuthPlugin(AuthPlugin):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)

        # Required OIDC configuration
        self.issuer = config.get("issuer")
        if not self.issuer:
            raise ValueError("OIDC issuer must be specified")

        self.client_id = config.get("client_id")
        if not self.client_id:
            raise ValueError("OIDC client_id must be specified")

        self.client_secret = config.get("client_secret")
        if not self.client_secret:
            raise ValueError("OIDC client_secret must be specified")

        # Callback path configuration
        self.callback_path = config.get("callback_path", "/auth/oidc/callback")

        # The redirect_uri can be explicitly set or will be automatically generated
        # when needed based on the request
        self.redirect_uri = config.get("redirect_uri")

        # Optional OIDC configuration
        self.scope = config.get("scope", "openid profile email")
        self.response_type = config.get("response_type", "code")
        self.response_mode = config.get("response_mode", "query")
        self.pkce_enabled = config.get("pkce_enabled", True)

        # Session configuration
        self.cookie_name = config.get("cookie_name", "oidc_session")
        self.cookie_secure = config.get("cookie_secure", True)
        self.cookie_http_only = config.get("cookie_http_only", True)
        self.cookie_same_site = config.get("cookie_same_site", "Lax")
        self.cookie_max_age = config.get("cookie_max_age", 86400)  # 24 hours
        self.cookie_domain = config.get("cookie_domain", "")
        self.cookie_path = config.get("cookie_path", "/")

        # Token validation
        self.validate_issuer = config.get("validate_issuer", True)
        self.validate_audience = config.get("validate_audience", True)
        self.validate_nonce = config.get("validate_nonce", True)
        self.token_leeway = config.get("token_leeway", 30)  # seconds

        # Session storage
        redis_url = config.get("redis_url")
        encryption_key = config.get("encryption_key")

        if redis_url:
            self.session_store = RedisSessionStore(
                redis_url=redis_url,
                prefix=f"oidc_{self.client_id}_",
                encryption_key=encryption_key,
            )
        else:
            self.session_store = MemorySessionStore()

        # CSRF protection
        self.csrf_protection = config.get("csrf_protection", True)

        # Discover OIDC endpoints
        self.discover_endpoints()

        # Initialize JWKS cache
        self.jwks_cache = JWKSCache(self.jwks_uri)

    def discover_endpoints(self) -> None:
        """Discover OIDC endpoints from the issuer's well-known configuration"""
        discovery_url = f"{self.issuer.rstrip('/')}/.well-known/openid-configuration"
        try:
            response = requests.get(discovery_url, timeout=10)
            response.raise_for_status()
            config = response.json()

            self.authorization_endpoint = config.get("authorization_endpoint")
            self.token_endpoint = config.get("token_endpoint")
            self.userinfo_endpoint = config.get("userinfo_endpoint")
            self.jwks_uri = config.get("jwks_uri")
            self.end_session_endpoint = config.get("end_session_endpoint")

            if (
                not self.authorization_endpoint
                or not self.token_endpoint
                or not self.jwks_uri
            ):
                raise ValueError("Failed to discover required OIDC endpoints")

        except Exception as e:
            logger.error(f"OIDC discovery failed: {e}")
            raise ValueError(f"OIDC discovery failed: {str(e)}")

    def authenticate(self, request_headers: Dict[str, str], path: str) -> AuthResult:
        """Authenticate a request using OIDC"""

        # Check for session cookie
        cookies = self._parse_cookies(request_headers.get("Cookie", ""))
        session_id = cookies.get(self.cookie_name)

        if session_id:
            session = self.session_store.get(session_id)

            if session:
                # Check if the access token is expired
                if session.get("expires_at", 0) < time.time():
                    # Try to refresh the token if we have a refresh token
                    if "refresh_token" in session:
                        try:
                            token = self._refresh_token(
                                session["refresh_token"], request_headers
                            )
                            session.update(token)
                            self.session_store.set(
                                session_id, session, ttl=self.cookie_max_age
                            )
                        except Exception as e:
                            logger.warning(f"Token refresh failed: {e}")
                            # If refresh fails, redirect to login
                            return self._redirect_to_login(request_headers)
                    else:
                        # No refresh token, redirect to login
                        return self._redirect_to_login(request_headers)

                # Valid session, return authenticated
                return AuthResult(
                    authenticated=True,
                    headers=self._get_auth_headers_from_session(session),
                )

        # No valid session, redirect to login
        return self._redirect_to_login(request_headers)

    def _get_redirect_uri(self, request_headers: Dict[str, str]) -> str:
        """
        Generate the redirect_uri based on the request headers if not explicitly set
        """
        # If redirect_uri is explicitly configured, use it
        if self.redirect_uri:
            return self.redirect_uri

        # Otherwise, generate it from the request
        host = request_headers.get("Host")
        if not host:
            raise ValueError("Cannot determine redirect_uri: Host header is missing")

        # Determine protocol (http or https)
        protocol = request_headers.get("X-Forwarded-Proto", "http")

        # Construct the redirect_uri
        return f"{protocol}://{host}{self.callback_path}"

    def _redirect_to_login(self, request_headers: Dict[str, str]) -> AuthResult:
        """Create a redirect to the OIDC authorization endpoint"""
        state = self._generate_secure_random_string(32)
        nonce = self._generate_secure_random_string(16)

        # Get the redirect_uri
        redirect_uri = self._get_redirect_uri(request_headers)

        # PKCE support
        code_verifier = None
        code_challenge = None
        code_challenge_method = None

        if self.pkce_enabled:
            code_verifier = self._generate_secure_random_string(64)
            code_challenge = self._create_code_challenge(code_verifier)
            code_challenge_method = "S256"

        # Store state and other data for validation on callback
        session_data = {
            "state": state,
            "nonce": nonce,
            "original_url": self._get_original_url(request_headers),
            "created_at": time.time(),
            "redirect_uri": redirect_uri,
        }

        if code_verifier:
            session_data["code_verifier"] = code_verifier

        # Store in session store with a short TTL (10 minutes)
        self.session_store.set(state, session_data, ttl=600)

        # Build authorization URL
        params = {
            "client_id": self.client_id,
            "response_type": self.response_type,
            "scope": self.scope,
            "redirect_uri": redirect_uri,
            "state": state,
            "nonce": nonce,
            "response_mode": self.response_mode,
        }

        # Add PKCE parameters if enabled
        if self.pkce_enabled and code_challenge:
            params["code_challenge"] = code_challenge
            params["code_challenge_method"] = code_challenge_method

        auth_url = f"{self.authorization_endpoint}?{urllib.parse.urlencode(params)}"

        # Return a redirect response
        return AuthResult(
            authenticated=False, redirect_status_code=302, redirect_url=auth_url
        )

    def _get_original_url(self, request_headers: Dict[str, str]) -> str:
        """Get the original URL from request headers"""
        original_uri = request_headers.get("X-Original-URI", "/")
        original_host = request_headers.get("Host", "")
        original_proto = request_headers.get("X-Forwarded-Proto", "http")

        if original_uri.startswith("http"):
            return original_uri

        if original_host:
            return f"{original_proto}://{original_host}{original_uri}"

        return original_uri

    def _generate_secure_random_string(self, length: int = 32) -> str:
        """Generate a cryptographically secure random string"""
        import secrets

        return secrets.token_urlsafe(length)

    def _create_code_challenge(self, code_verifier: str) -> str:
        """Create a PKCE code challenge from the code verifier"""
        sha256 = hashlib.sha256(code_verifier.encode()).digest()
        return base64.urlsafe_b64encode(sha256).decode().rstrip("=")

    def _parse_cookies(self, cookie_header: str) -> Dict[str, str]:
        """Parse Cookie header into a dictionary"""
        cookies = {}
        if not cookie_header:
            return cookies

        for cookie in cookie_header.split(";"):
            if "=" in cookie:
                name, value = cookie.strip().split("=", 1)
                cookies[name.strip()] = value.strip()

        return cookies

    def _get_auth_headers_from_session(self, session: Dict[str, Any]) -> Dict[str, str]:
        """Extract authentication headers from session data"""
        headers = {}

        if "id_token_claims" in session:
            claims = session["id_token_claims"]

            # Add standard user info headers
            if "sub" in claims:
                headers["X-Auth-User-ID"] = claims["sub"]
            if "email" in claims:
                headers["X-Auth-User-Email"] = claims["email"]
            if "name" in claims:
                headers["X-Auth-User-Name"] = claims["name"]

            # Add roles/groups if available
            if "groups" in claims:
                headers["X-Auth-User-Groups"] = ",".join(claims["groups"])
            if "roles" in claims:
                headers["X-Auth-User-Roles"] = ",".join(claims["roles"])

            # Add access token if available
            if "access_token" in session:
                headers["X-Auth-Token"] = session["access_token"]

            # Add all claims as JSON (be careful with header size limits)
            headers["X-Auth-User-Claims"] = json.dumps(claims)

        return headers

    def _refresh_token(
        self, refresh_token: str, request_headers: Dict[str, str]
    ) -> Dict[str, Any]:
        """Refresh an expired access token"""
        # Get the redirect_uri that was used for the initial authorization
        redirect_uri = self._get_redirect_uri(request_headers)

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": redirect_uri,  # Some providers require this for refresh, too
        }

        try:
            response = requests.post(self.token_endpoint, data=data, timeout=10)
            response.raise_for_status()

            token_data = response.json()
            token_data["expires_at"] = time.time() + token_data.get("expires_in", 3600)

            # If a new ID token is provided, validate and decode it
            if "id_token" in token_data:
                id_token_claims = self._validate_and_decode_id_token(
                    token_data["id_token"], None  # No nonce validation on refresh
                )
                token_data["id_token_claims"] = id_token_claims

            return token_data

        except Exception as e:
            logger.error(f"Token refresh failed: {e}")
            raise

    def get_plugin_paths(self) -> List[PluginPath]:
        """Register the OIDC callback path"""
        paths = [
            PluginPath(
                path=self.callback_path,
                regex=False,
                authenticate=False,
                description=f"OIDC callback endpoint for {self.client_id}",
            )
        ]

        # Add logout path if end_session_endpoint is available
        if hasattr(self, "end_session_endpoint"):
            paths.append(
                PluginPath(
                    path="/auth/oidc/logout",
                    regex=False,
                    authenticate=False,
                    description=f"OIDC logout endpoint for {self.client_id}",
                )
            )

        return paths

    def handle_plugin_path(
        self, path: str, request_headers: Dict[str, str], request_body: bytes
    ) -> Optional[Tuple[int, Dict[str, str], bytes]]:
        """Handle plugin-specific paths"""

        # Handle OIDC callback
        if path.split("?")[0] == self.callback_path:
            return self._handle_callback(path, request_headers, request_body)

        # Handle logout
        if path.split("?")[0] == "/auth/oidc/logout":
            return self._handle_logout(request_headers, request_body)

        return None

    def _handle_callback(
        self, path: str, request_headers: Dict[str, str], request_body: bytes
    ) -> Tuple[int, Dict[str, str], bytes]:
        """Handle the OIDC callback"""
        # Parse query parameters
        query_string = path.split("?", 1)[-1] if "?" in path else ""
        params = urllib.parse.parse_qs(query_string)

        # Get the authorization code and state
        code = params.get("code", [""])[0]
        state = params.get("state", [""])[0]

        if not code or not state:
            logger.error("Invalid callback: missing code or state")
            return (
                400,
                {"Content-Type": "text/plain"},
                "Invalid or missing code or state parameter",
            )

        # Get the stored state data
        state_data = self.session_store.get(state)
        if not state_data:
            logger.error(f"Invalid state: {state}")
            return (
                400,
                {"Content-Type": "text/plain"},
                "Invalid or expired state parameter",
            )

        # Clean up the state data
        self.session_store.delete(state)

        # Verify state to prevent CSRF
        if self.csrf_protection and state_data.get("state") != state:
            logger.error(
                f"State parameter mismatch: {state_data.get('state')} != {state}"
            )
            return (400, {"Content-Type": "text/plain"}, "State parameter mismatch")

        original_url = state_data.get("original_url", "/")

        try:
            # Exchange the code for tokens
            token_data = self._exchange_code(code, state_data)

            # Validate the ID token
            id_token_claims = self._validate_and_decode_id_token(
                token_data.get("id_token", ""),
                state_data.get("nonce") if self.validate_nonce else None,
            )

            # Add the ID token claims to the token data
            token_data["id_token_claims"] = id_token_claims

            # Create a new session
            session_id = self._generate_secure_random_string(32)
            self.session_store.set(session_id, token_data, ttl=self.cookie_max_age)

            # Build the Set-Cookie header
            cookie_parts = [
                f"{self.cookie_name}={session_id}",
                f"Path={self.cookie_path}",
                f"Max-Age={self.cookie_max_age}",
            ]

            if self.cookie_domain:
                cookie_parts.append(f"Domain={self.cookie_domain}")

            if self.cookie_secure:
                cookie_parts.append("Secure")

            if self.cookie_http_only:
                cookie_parts.append("HttpOnly")

            if self.cookie_same_site:
                cookie_parts.append(f"SameSite={self.cookie_same_site}")

            set_cookie = "; ".join(cookie_parts)

            # Set the session cookie and redirect to the original URL
            return (302, {"Location": original_url, "Set-Cookie": set_cookie}, b"")

        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return (
                500,
                {"Content-Type": "text/plain"},
                f"Authentication error: {str(e)}".encode(),
            )

    def _handle_logout(
        self, request_headers: Dict[str, str], request_body: bytes
    ) -> Tuple[int, Dict[str, str], bytes]:
        """Handle logout requests"""
        cookies = self._parse_cookies(request_headers.get("Cookie", ""))
        session_id = cookies.get(self.cookie_name)

        # Clear the session if it exists
        if session_id:
            session = self.session_store.get(session_id)
            self.session_store.delete(session_id)
        else:
            session = None

        # Build the cookie clearing header
        clear_cookie = f"{self.cookie_name}=; Path={self.cookie_path}; Max-Age=0"
        if self.cookie_domain:
            clear_cookie += f"; Domain={self.cookie_domain}"
        if self.cookie_secure:
            clear_cookie += "; Secure"
        if self.cookie_http_only:
            clear_cookie += "; HttpOnly"

        # Get the ID token hint if available
        id_token_hint = None
        if session and "id_token" in session:
            id_token_hint = session["id_token"]

        # Get the post-logout redirect URI
        post_logout_redirect_uri = request_headers.get("X-Auth-Return-To", "/")

        # If we don't have an absolute URL, make it absolute
        if not post_logout_redirect_uri.startswith("http"):
            host = request_headers.get("Host", "")
            protocol = request_headers.get("X-Forwarded-Proto", "http")
            if host:
                post_logout_redirect_uri = (
                    f"{protocol}://{host}{post_logout_redirect_uri}"
                )

        # If we have an end session endpoint, redirect to it
        if hasattr(self, "end_session_endpoint") and self.end_session_endpoint:
            params = {"client_id": self.client_id}

            if id_token_hint:
                params["id_token_hint"] = id_token_hint

            if post_logout_redirect_uri:
                params["post_logout_redirect_uri"] = post_logout_redirect_uri

            logout_url = f"{self.end_session_endpoint}?{urllib.parse.urlencode(params)}"

            return (302, {"Location": logout_url, "Set-Cookie": clear_cookie}, b"")

        # Otherwise, just clear the cookie and redirect
        return (
            302,
            {"Location": post_logout_redirect_uri, "Set-Cookie": clear_cookie},
            b"",
        )

    def _exchange_code(self, code: str, state_data: Dict[str, Any]) -> Dict[str, Any]:
        """Exchange the authorization code for tokens"""
        # Get the redirect_uri that was used for the authorization request
        redirect_uri = state_data.get("redirect_uri")
        if not redirect_uri:
            raise ValueError("No redirect_uri found in state data")

        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        # Add PKCE code verifier if available
        if "code_verifier" in state_data:
            data["code_verifier"] = state_data["code_verifier"]

        try:
            response = requests.post(self.token_endpoint, data=data, timeout=10)
            response.raise_for_status()

            token_data = response.json()
            token_data["expires_at"] = time.time() + token_data.get("expires_in", 3600)

            return token_data

        except Exception as e:
            logger.error(f"Token exchange failed: {e}")
            raise ValueError(f"Failed to exchange code for tokens: {str(e)}")

    def _validate_and_decode_id_token(self, id_token: str, expected_nonce: Optional[str]) -> Dict[str, Any]:
        """Validate and decode the ID token"""
        if not id_token:
            raise ValueError("No ID token provided")

        # Parse the token header to get the key ID (kid)
        try:
            header = jwt.get_unverified_header(id_token)
            kid = header.get('kid')
            if not kid:
                raise ValueError("No 'kid' found in token header")
        except Exception as e:
            raise ValueError(f"Failed to parse token header: {str(e)}")

        # Get the PEM-formatted key from the JWKS cache
        pem_key = self.jwks_cache.get_key(kid)
        if not pem_key:
            raise ValueError(f"No key found with ID {kid}")

        # First, decode the token without verification to see what's in it for debugging
        try:
            unverified_payload = jwt.decode(
                id_token,
                options={"verify_signature": False}
            )
        
            token_issuer = unverified_payload.get('iss')
            logger.debug(f"Token issuer: '{token_issuer}'")
            logger.debug(f"Expected issuer: '{self.issuer}'")
            logger.debug(f"Token audience: {unverified_payload.get('aud')}")
            logger.debug(f"Token subject: {unverified_payload.get('sub')}")
            logger.debug(f"Token expiration: {unverified_payload.get('exp')}")
        
        except Exception as e:
            logger.error(f"Error decoding unverified token: {e}")

        # Set up the verification options
        options = {
            'verify_signature': True,
            'verify_exp': True,
            'verify_nbf': True,
            'verify_iat': True,
            'verify_aud': self.validate_audience,
            'verify_iss': self.validate_issuer,
            'leeway': self.token_leeway
        }

        audience = None
        if self.validate_audience:
            audience = self.client_id

        if not isinstance(audience, str):
            audience = str(audience)

        # Verify and decode the token
        try:
            payload = jwt.decode(
                id_token,
                pem_key,
                algorithms=['RS256', 'ES256'],
                audience=audience,
                issuer=self.issuer if self.validate_issuer else None,
                options=options
            )
        except jwt.ExpiredSignatureError:
            raise ValueError("ID token has expired")
        except jwt.ImmatureSignatureError:
            raise ValueError("ID token not yet valid")
        except jwt.InvalidIssuerError:
            raise ValueError("Invalid issuer")
        except jwt.InvalidAudienceError:
            raise ValueError("Invalid audience")
        except Exception as e:
            logger.error(f"Detailed token validation error: {str(e)}")
            logger.debug(f"Token: {id_token[:20]}...")
            logger.debug(f"Audience: {audience}")
            logger.debug(f"Issuer: {self.issuer}")
            raise ValueError(f"Token validation failed: {str(e)}")

        # Verify nonce if required
        if self.validate_nonce and expected_nonce and payload.get('nonce') != expected_nonce:
            raise ValueError("Invalid nonce")

        return payload
