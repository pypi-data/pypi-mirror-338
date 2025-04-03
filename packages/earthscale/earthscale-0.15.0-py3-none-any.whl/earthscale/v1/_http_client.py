import datetime
import hashlib
import http.server
import logging
import sys
import threading
import time
import urllib.parse
import webbrowser
from pathlib import Path
from typing import Any, Literal

import requests
from pydantic import BaseModel, ValidationError, AwareDatetime
from supabase import Client, ClientOptions

from earthscale.v1.exceptions import (
    AuthenticationError,
    EarthscaleClientError,
    NotFoundError,
    TokenRefreshRequired,
    ValidationFailedError,
)
from earthscale.v1.models import ErrorResponse

logger = logging.getLogger("earthscale")

_SUCCESSFUL_LOGIN_HTML = b"""
    <html>
        <head>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    color: #333;
                }
                .message {
                    text-align: center;
                    border-radius: 15px;
                    padding: 50px;
                    background-color: #fff;
                    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
                }
                h1 {
                    margin-bottom: 20px;
                    font-size: 24px;
                }
                p {
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="message">
                <h1>You have successfully logged in to Earthscale!</h1>
                <p>You can now close this tab.</p>
            </div>
        </body>
    </html>
"""


def _is_webbrowser_supported() -> bool:
    """Check if webbrowser is supported."""
    try:
        webbrowser.get()
        return True
    except webbrowser.Error:
        return False


class _Credentials(BaseModel):
    """Credentials model for storing authentication information."""

    auth_url: str
    user_email: str
    access_token: str
    refresh_token: str
    expires_in: int | None = None
    expires_at: AwareDatetime | None = None


class _OAuthRedirectCodeHandler(http.server.BaseHTTPRequestHandler):
    code: str | None = None
    credentials: _Credentials | None = None
    client: Client | None = None

    def log_message(self, format: Any, *args: Any) -> None:
        return

    def do_GET(self) -> None:
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        code = params.get("code", [None])[0]

        if code is None:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Authentication failed! Did you use the right account?")
            return

        if _OAuthRedirectCodeHandler.client is None:
            raise AuthenticationError("No client available for code exchange")
        session_response = _OAuthRedirectCodeHandler.client.auth.exchange_code_for_session(
            {
                "auth_code": code,
                "redirect_to": "http://localhost:3000",  # Required hack for Supabase
            }
        ).session

        if session_response is None:
            raise AuthenticationError("No session returned from authentication service")

        # Store credentials from session
        _OAuthRedirectCodeHandler.credentials = _Credentials(
            auth_url=_OAuthRedirectCodeHandler.client.supabase_url,
            user_email=session_response.user.email,
            access_token=session_response.access_token,
            refresh_token=session_response.refresh_token,
            expires_in=session_response.expires_in,
            expires_at=session_response.expires_at,
        )

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(_SUCCESSFUL_LOGIN_HTML)
        _OAuthRedirectCodeHandler.code = code


class _EarthscaleHttpClient:
    """Private HTTP client for the Earthscale API.

    This class handles all HTTP-related functionality including:
    - Session management
    - Authentication
    - Request handling and error processing
    - Header management
    """

    def __init__(
        self,
        api_url: str,
        auth_url: str,
        anon_key: str,
        email: str | None = None,
        password: str | None = None,
        credentials_file: Path | None = None,
        session: requests.Session | None = None,
    ):
        """Initialize the HTTP client.

        Args:
            api_url: The URL of the Earthscale API.
            auth_url: URL for authentication service.
            anon_key: The anon key for the authentication service.
            email: Email for authentication.
            password: Password for authentication.
            credentials_file: Path to the credentials file.
            session: Optional custom requests session to use.
        """
        self._api_url: str = api_url.rstrip("/")
        self._auth_url: str = auth_url.rstrip("/")
        self._anon_key: str = anon_key
        self._email: str | None = email
        self._password: str | None = password
        # Using separate files per auth url to avoid leaking credentials to other
        # environments/services
        auth_hash = hashlib.md5(auth_url.encode()).hexdigest()
        self._credentials_file: Path = (
            credentials_file
            or Path.home() / ".earthscale" / f"credentials-{auth_hash}.json"
        ).absolute()
        self._credentials: _Credentials | None = None

        self._owns_session: bool = session is None
        self._session = session if session else requests.Session()

        self._try_to_load_credentials()

    @property
    def user_email(self) -> str | None:
        if self._credentials:
            return self._credentials.user_email
        return None

    @property
    def api_url(self) -> str:
        return self._api_url

    @property
    def auth_url(self) -> str:
        return self._auth_url

    def _save_credentials(self, credentials: _Credentials) -> None:
        """Save credentials to file and update headers/session."""
        self._credentials_file.parent.mkdir(exist_ok=True, parents=True)
        with self._credentials_file.open("w") as f:
            f.write(credentials.model_dump_json(indent=2))

    def _try_to_load_credentials(self) -> None:
        if not self._credentials_file.exists():
            return

        try:
            with self._credentials_file.open() as f:
                credentials = _Credentials.model_validate_json(f.read())

            if self._email and credentials.user_email != self._email:
                logger.info(
                    "Not loading credentials from '%s' because email '%s' does not match "
                    "the explicitly provided email '%s'",
                    self._credentials_file,
                    credentials.user_email,
                    self._email,
                )
                return

            logger.info("Loaded credentials from '%s'", self._credentials_file)
            self._credentials = credentials
        except ValidationError as e:
            logger.warning(
                "Failed to load credentials from '%s': %s",
                self._credentials_file,
                e,
            )

    def _authenticate_with_oauth(self) -> _Credentials:
        print(
            """
================================================================================

  Authenticating using OAuth flow. This will open a browser window/tab.

  Please check your Browser to see whether interaction is required.

================================================================================

""",
            file=sys.stderr,
        )
        # Initialize Supabase client
        client = Client(
            self._auth_url,
            self._anon_key,
            options=ClientOptions(
                flow_type="pkce",
                auto_refresh_token=False,
            ),
        )

        # Add client to CodeHandler for use during code exchange
        _OAuthRedirectCodeHandler.client = client

        server = http.server.HTTPServer(("localhost", 0), _OAuthRedirectCodeHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        # Get OAuth URL using Supabase client
        oauth_response = client.auth.sign_in_with_oauth(
            {
                "provider": "google",
                "options": {
                    "redirect_to": f"http://localhost:{server.server_port}/auth/callback",
                    "query_params": {
                        "response_type": "code",
                    },
                },
            },
        )
        webbrowser.open(oauth_response.url)

        # Wait for authentication
        timeout_s = 120
        start_time = time.time()
        while (
            _OAuthRedirectCodeHandler.code is None
            and time.time() - start_time < timeout_s
        ):
            time.sleep(0.5)

        server.shutdown()
        server.server_close()

        if _OAuthRedirectCodeHandler.code is None:
            raise AuthenticationError(
                f"Authentication timed out after {timeout_s} seconds"
            )

        if _OAuthRedirectCodeHandler.credentials is None:
            raise AuthenticationError("No credentials returned from authentication")

        return _OAuthRedirectCodeHandler.credentials

    def _authenticate_with_email_password(self) -> _Credentials:
        """Authenticate using email and password credentials.

        Raises:
            AuthenticationError: If authentication fails.
        """
        # already checked, this is for mypy
        assert self._email is not None
        assert self._password is not None

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if self._anon_key:
            headers["apiKey"] = self._anon_key

        response = self._session.post(
            f"{self._auth_url}/auth/v1/token?grant_type=password",
            json={
                "email": self._email,
                "password": self._password,
            },
            headers=headers,
        )

        if not response.ok:
            raise AuthenticationError(
                f"Login failed, status code: {response.status_code}, response: "
                f"{response.text}"
            )

        auth_data = response.json()
        credentials = _Credentials(
            auth_url=self._auth_url,
            user_email=self._email,
            access_token=auth_data["access_token"],
            refresh_token=auth_data["refresh_token"],
            expires_in=auth_data["expires_in"],
            expires_at=auth_data["expires_at"],
        )
        return credentials

    def login(self) -> None:
        """Login using service account credentials or OAuth.

        Raises:
            AuthenticationError: If authentication fails.
        """
        credentials: _Credentials
        auth_method: Literal["email_password", "oauth"]
        # use credentials from file if valid
        if self._email and self._password:
            logger.info(
                "Environment variables EARTHSCALE_EMAIL and EARTHSCALE_PASSWORD set. "
                "Using email/password authentication."
            )
            credentials = self._authenticate_with_email_password()
            auth_method = "email_password"
        elif _is_webbrowser_supported():
            logger.info(
                "Environment variables EARTHSCALE_EMAIL and EARTHSCALE_PASSWORD not "
                "set. Using OAuth authentication."
            )
            credentials = self._authenticate_with_oauth()
            auth_method = "oauth"
        else:
            raise AuthenticationError(
                "No email or password provided and webbrowser is not supported."
                "Please provide email and password via the EARTHSCALE_EMAIL and"
                "EARTHSCALE_PASSWORD environment variables, or use a supported"
                "browser to authenticate via OAuth."
            )

        if not credentials:
            raise AuthenticationError(
                f"No credentials returned from authentication method '{auth_method}'"
            )

        self._credentials = credentials

        if not self._are_credentials_valid():
            raise AuthenticationError(
                f"Invalid credentials returned from authentication method "
                f"'{auth_method}'"
            )
        self._save_credentials(credentials)

    def _is_token_expired(self) -> bool:
        """Check if the token is expired."""
        if not self._credentials:
            return True
        return (
            self._credentials.expires_at is not None
            and self._credentials.expires_at.replace(tzinfo=datetime.timezone.utc)
            < datetime.datetime.now(datetime.timezone.utc)
        )

    def _are_credentials_valid(self) -> bool:
        """
        Credentials are valid if:
            - user email from env matches credentials user (or is not set)
            - token is not expired
        """
        if not self._credentials:
            return False

        if self._email and self._email != self._credentials.user_email:
            return False

        return not self._is_token_expired()

    def refresh_token(self) -> None:
        """Refresh the JWT token using the refresh token.

        Raises:
            AuthenticationError: If token refresh fails.
        """
        if not self._are_credentials_valid():
            self.login()
            return

        # already checked, this is for mypy
        assert self._credentials is not None

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self._anon_key:
            headers["apiKey"] = self._anon_key

        response = self._session.post(
            f"{self._auth_url}/auth/v1/token?grant_type=refresh_token",
            json={
                "refresh_token": self._credentials.refresh_token,
            },
            headers=headers,
        )

        if not response.ok:
            # If refresh fails, try logging in again
            self.login()
            return

        auth_data = response.json()
        credentials = _Credentials(
            auth_url=self._auth_url,
            user_email=self._credentials.user_email,
            access_token=auth_data["access_token"],
            refresh_token=auth_data["refresh_token"],
            expires_in=auth_data["expires_in"],
            expires_at=auth_data["expires_at"],
        )
        self._credentials = credentials
        if not self._are_credentials_valid():
            raise AuthenticationError("Invalid credentials returned from token refresh")
        self._save_credentials(credentials)

    @staticmethod
    def _handle_response(response: requests.Response) -> bytes:
        """Handle the API response.

        Args:
            response: The response from the API.

        Returns:
            Raw response content.

        Raises:
            TokenRefreshRequired: If authentication fails and token refresh is needed.
            AuthenticationError: If authentication fails.
            NotFoundError: If the resource is not found.
            ValidationFailedError: If validation fails.
            ServerError: If the server returns an error.
        """
        # Check for authentication errors that might require token refresh
        if response.status_code == 401:
            raise TokenRefreshRequired("Authentication token expired or invalid")

        # Map status codes to exception types
        error_classes = {
            401: AuthenticationError,
            404: NotFoundError,
            400: ValidationFailedError,
        }

        if not response.ok:
            # Try to parse the error response
            error_class = error_classes.get(
                response.status_code,
                EarthscaleClientError,
            )

            try:
                error = ErrorResponse.model_validate_json(response.text)
                raise error_class(error.message, error.error_class)
            except ValidationError:
                # If we can't parse the error response, use a generic message
                message = (
                    "Authentication failed"
                    if response.status_code == 401
                    else "Resource not found"
                    if response.status_code == 404
                    else "Validation failed"
                    if response.status_code == 400
                    else "Server error"
                    if response.status_code >= 500
                    else f"Request failed with status code {response.status_code}"
                )
                raise error_class(message) from None

        return response.content

    def request(
        self,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        endpoint: str,
        data: BaseModel | None = None,
        api_version: str = "v1",
        use_auth: bool = True,
    ) -> bytes:
        """Make a request to the API with automatic retries and token refresh.

        Args:
            method: The HTTP method to use.
            endpoint: The API endpoint to call (without the base URL and version).
            data: Optional data to send with the request.
            api_version: The API version to use. This is basically url prefix.
            use_auth: Use authentication for the request. Triggers login if true and not
                already authenticated.

        Returns:
            Raw response content
        """

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        # Ensure we have a token before making the request
        if use_auth:
            if not self._are_credentials_valid():
                self.login()
            assert self._credentials is not None
            assert self._credentials.access_token is not None
            headers["Authorization"] = f"Bearer {self._credentials.access_token}"

        api_version = api_version.strip("/") + "/" if api_version else ""
        url = f"{self._api_url}/{api_version}{endpoint.lstrip('/')}"

        data_json = data.model_dump_json() if data else None
        try:
            response = self._session.request(
                method,
                url,
                data=data_json,
                headers=headers,
            )
            return self._handle_response(response)
        except TokenRefreshRequired:
            # Token is expired, refresh it and retry the request once
            self.refresh_token()
            response = self._session.request(
                method,
                url,
                data=data_json,
                headers=headers,
            )
            return self._handle_response(response)

    def close_session(self) -> None:
        """Close the session if we own it."""
        if self._owns_session:
            self._session.close()
