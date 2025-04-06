"""
Authentication implementations for API clients.
"""
from typing import Dict, Optional, Any, List
import base64
import time
import requests
from abc import ABC, abstractmethod
import urllib.parse
from datetime import datetime, timedelta
import logging

from llamaapi.exceptions import AuthenticationError

logger = logging.getLogger(__name__)

class BaseAuth(ABC):
    """
    Base class for all authentication methods.
    """
    @abstractmethod
    def authenticate(self, request):
        """
        Apply authentication to the request.
        
        Args:
            request: The request to authenticate.
            
        Returns:
            The authenticated request.
        """
        pass

class ApiKeyAuth(BaseAuth):
    """
    API Key authentication using a header or query parameter.
    """
    def __init__(
        self, 
        api_key: str, 
        param_name: str = "api_key", 
        location: str = "header", 
        prefix: str = "ApiKey "
    ):
        """
        Initialize API Key authentication.
        
        Args:
            api_key: The API key.
            param_name: The name of the header or query parameter.
            location: Where to place the API key ('header' or 'query').
            prefix: Optional prefix for the API key when using header.
        """
        if not api_key:
            raise AuthenticationError("API key is required")
            
        self.api_key = api_key
        self.param_name = param_name
        self.location = location.lower()
        self.prefix = prefix if location.lower() == "header" else ""
        
        if self.location not in ["header", "query"]:
            raise ValueError("Location must be 'header' or 'query'")
    
    def authenticate(self, request):
        """Apply API key authentication to the request."""
        if self.location == "header":
            # If using Authorization header, standardize the header name
            header_name = "Authorization" if self.param_name.lower() == "authorization" else self.param_name
            request.headers[header_name] = f"{self.prefix}{self.api_key}"
        else:
            # Add API key to query parameters
            request.params[self.param_name] = self.api_key
        
        return request

class BearerAuth(BaseAuth):
    """
    Bearer token authentication using the Authorization header.
    """
    def __init__(self, token: str, prefix: str = "Bearer"):
        """
        Initialize Bearer token authentication.
        
        Args:
            token: The bearer token.
            prefix: The prefix to use (default: "Bearer").
        """
        if not token:
            raise AuthenticationError("Bearer token is required")
            
        self.token = token
        self.prefix = prefix
    
    def authenticate(self, request):
        """Apply bearer token authentication to the request."""
        request.headers["Authorization"] = f"{self.prefix} {self.token}"
        return request

class BasicAuth(BaseAuth):
    """
    HTTP Basic authentication using username and password.
    """
    def __init__(self, username: str, password: str):
        """
        Initialize Basic authentication.
        
        Args:
            username: The username.
            password: The password.
        """
        if not username or not password:
            raise AuthenticationError("Username and password are required")
            
        self.username = username
        self.password = password
        
        # Pre-compute the authorization value
        credentials = f"{username}:{password}"
        self.encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    
    def authenticate(self, request):
        """Apply basic authentication to the request."""
        request.headers["Authorization"] = f"Basic {self.encoded_credentials}"
        return request

class OAuth2Auth(BaseAuth):
    """
    OAuth 2.0 authentication with token refresh capability.
    """
    def __init__(
        self,
        token_url: str,
        client_id: str,
        client_secret: str,
        scope: Optional[str] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        expires_at: Optional[float] = None,
        auto_refresh: bool = True,
        token_placement: str = "header",
    ):
        """
        Initialize OAuth 2.0 authentication.
        
        Args:
            token_url: The token endpoint URL.
            client_id: The OAuth client ID.
            client_secret: The OAuth client secret.
            scope: Optional space-separated scopes.
            access_token: Optional initial access token.
            refresh_token: Optional initial refresh token.
            expires_at: Optional timestamp when the token expires.
            auto_refresh: Whether to automatically refresh tokens.
            token_placement: Where to place the token ('header' or 'query').
        """
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.auto_refresh = auto_refresh
        self.token_placement = token_placement
        
        # Validate token placement
        if token_placement not in ["header", "query"]:
            raise ValueError("token_placement must be 'header' or 'query'")
    
    def is_token_expired(self) -> bool:
        """
        Check if the access token is expired.
        
        Returns:
            True if the token is expired or missing, False otherwise.
        """
        if not self.access_token or not self.expires_at:
            return True
            
        # Add a buffer of 60 seconds to ensure we refresh before expiration
        return time.time() >= (self.expires_at - 60)
    
    def fetch_token(self, grant_type: str, **kwargs) -> Dict[str, Any]:
        """
        Fetch a token from the token endpoint.
        
        Args:
            grant_type: The OAuth grant type.
            **kwargs: Additional parameters for the token request.
            
        Returns:
            The token response as a dictionary.
        """
        import requests  # Import here to avoid circular imports
        
        data = {
            "grant_type": grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            **kwargs
        }
        
        if self.scope and grant_type != "refresh_token":
            data["scope"] = self.scope
        
        try:
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise AuthenticationError(f"Failed to fetch OAuth token: {str(e)}")
    
    def refresh_access_token(self):
        """
        Refresh the access token using the refresh token.
        
        Raises:
            AuthenticationError: If the token refresh fails.
        """
        if not self.refresh_token:
            raise AuthenticationError("No refresh token available")
        
        logger.debug("Refreshing OAuth access token")
        
        # Request new token using refresh_token grant
        token_data = self.fetch_token(
            grant_type="refresh_token",
            refresh_token=self.refresh_token
        )
        
        # Update token information
        self.update_token(token_data)
    
    def update_token(self, token_data: Dict[str, Any]):
        """
        Update token information from response data.
        
        Args:
            token_data: The token response data.
        """
        self.access_token = token_data.get("access_token")
        
        # Only update refresh token if a new one is provided
        if "refresh_token" in token_data:
            self.refresh_token = token_data.get("refresh_token")
        
        # Calculate token expiration
        expires_in = token_data.get("expires_in", 3600)  # Default to 1 hour
        self.expires_at = time.time() + int(expires_in)
        
        logger.debug(f"OAuth token updated, expires in {expires_in} seconds")
    
    def authenticate(self, request):
        """Apply OAuth authentication to the request."""
        # Check if token refresh is needed
        if self.auto_refresh and self.is_token_expired():
            self.refresh_access_token()
        
        # Apply token to the request
        if not self.access_token:
            raise AuthenticationError("No access token available")
        
        if self.token_placement == "header":
            request.headers["Authorization"] = f"Bearer {self.access_token}"
        else:
            request.params["access_token"] = self.access_token
        
        return request
    
    def client_credentials_flow(self):
        """
        Get a token using the client credentials flow.
        """
        token_data = self.fetch_token(grant_type="client_credentials")
        self.update_token(token_data)
    
    def password_flow(self, username: str, password: str):
        """
        Get a token using the password (resource owner) flow.
        
        Args:
            username: The user's username.
            password: The user's password.
        """
        token_data = self.fetch_token(
            grant_type="password",
            username=username,
            password=password
        )
        self.update_token(token_data)
    
    def authorization_code_flow(self, code: str, redirect_uri: str):
        """
        Exchange an authorization code for a token.
        
        Args:
            code: The authorization code.
            redirect_uri: The redirect URI used in the auth request.
        """
        token_data = self.fetch_token(
            grant_type="authorization_code",
            code=code,
            redirect_uri=redirect_uri
        )
        self.update_token(token_data)
    
    def get_authorization_url(self, redirect_uri: str, state: Optional[str] = None, **kwargs) -> str:
        """
        Build the authorization URL for the authorization code flow.
        
        Args:
            redirect_uri: The redirect URI.
            state: Optional state parameter for security.
            **kwargs: Additional parameters for the auth request.
            
        Returns:
            The authorization URL.
        """
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            **kwargs
        }
        
        if self.scope:
            params["scope"] = self.scope
        
        if state:
            params["state"] = state
        
        # Parse the token URL to extract the base URL
        parsed_url = urllib.parse.urlparse(self.token_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        # Replace the path part to point to the authorization endpoint
        # This is a common convention, but might need adjustment for some providers
        auth_path = parsed_url.path.replace("token", "authorize")
        auth_url = f"{base_url}{auth_path}"
        
        # Build the full authorization URL with query parameters
        return f"{auth_url}?{urllib.parse.urlencode(params)}"

def authenticate():
    """
    Decorator for server endpoints that require authentication.
    """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            # Authentication logic would go here
            # For example, check if the request has valid auth headers
            # If not authenticated, return an error response
            
            # For now, just call the original function
            return func(request, *args, **kwargs)
        return wrapper
    return decorator 