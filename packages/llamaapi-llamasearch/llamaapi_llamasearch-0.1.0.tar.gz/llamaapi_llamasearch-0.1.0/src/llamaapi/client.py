"""
API Client implementation for making HTTP requests.
"""
from typing import Any, Dict, List, Optional, Union, BinaryIO, Tuple, Callable
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
from contextlib import contextmanager
import hashlib
import json
import time
import urllib.parse

from llamaapi.auth import BaseAuth, ApiKeyAuth
from llamaapi.middleware import Middleware
from llamaapi.cache import BaseCache, NoCache
from llamaapi.exceptions import ApiError, AuthenticationError, RateLimitError, ServerError

logger = logging.getLogger(__name__)

class ApiRequest:
    """
    Represents an API request with all its attributes.
    """
    def __init__(
        self,
        method: str,
        url: str,
        headers: Dict[str, str] = None,
        params: Dict[str, Any] = None,
        data: Any = None,
        json: Dict[str, Any] = None,
        files: Dict[str, BinaryIO] = None,
        timeout: int = 30,
        stream: bool = False,
    ):
        self.method = method.upper()
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.json = json
        self.files = files
        self.timeout = timeout
        self.stream = stream

class ApiResponse:
    """
    Wrapper around requests.Response with additional functionality.
    """
    def __init__(self, response: requests.Response):
        self._response = response
        
    @property
    def status_code(self) -> int:
        """Get the HTTP status code of the response."""
        return self._response.status_code
        
    @property
    def headers(self) -> Dict[str, str]:
        """Get the response headers."""
        return dict(self._response.headers)
        
    @property
    def content(self) -> bytes:
        """Get the raw content of the response."""
        return self._response.content
        
    @property
    def text(self) -> str:
        """Get the decoded text content of the response."""
        return self._response.text
        
    def json(self) -> Dict[str, Any]:
        """Parse the JSON response body."""
        return self._response.json()
        
    def iter_content(self, chunk_size: int = 1024):
        """Iterate over the response content in chunks."""
        return self._response.iter_content(chunk_size=chunk_size)
        
    def iter_lines(self, chunk_size: int = 1024):
        """Iterate over the response content line by line."""
        return self._response.iter_lines(chunk_size=chunk_size)
        
    def raise_for_status(self):
        """Raise an exception for HTTP error responses."""
        try:
            self._response.raise_for_status()
        except requests.HTTPError as e:
            status_code = self.status_code
            
            # Try to get more detailed error message from JSON response
            error_message = str(e)
            try:
                error_data = self.json()
                if "error" in error_data:
                    error_message = error_data["error"]
                    if "message" in error_data["error"]:
                        error_message = error_data["error"]["message"]
            except:
                # If JSON parsing fails, use the response text
                if self.text:
                    error_message = self.text
            
            # Map to specific error types
            if 400 <= status_code < 500:
                if status_code == 401:
                    raise AuthenticationError(error_message, response=self)
                elif status_code == 429:
                    raise RateLimitError(error_message, response=self)
                else:
                    raise ApiError(error_message, response=self)
            elif status_code >= 500:
                raise ServerError(error_message, response=self)
            
    def __enter__(self):
        """Support for context manager protocol."""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure response is closed when exiting context."""
        self._response.close()

class ApiClient:
    """
    Client for making API requests with authentication, middleware, and caching.
    """
    
    def __init__(
        self,
        base_url: str,
        auth: Optional[BaseAuth] = None,
        timeout: int = 30,
        retries: int = 3,
        middleware: List[Middleware] = None,
        cache: BaseCache = None,
        cache_ttl: int = 300,
        verify_ssl: bool = True,
        user_agent: Optional[str] = None,
    ):
        """
        Initialize the API client.
        
        Args:
            base_url: The base URL for the API.
            auth: The authentication method to use.
            timeout: The default request timeout in seconds.
            retries: The number of times to retry failed requests.
            middleware: List of middleware to process requests and responses.
            cache: The cache implementation to use.
            cache_ttl: Time-to-live for cached responses in seconds.
            verify_ssl: Whether to verify SSL certificates.
            user_agent: Custom User-Agent header value.
        """
        self.base_url = base_url.rstrip('/')
        self.auth = auth
        self.timeout = timeout
        self.middleware = middleware or []
        self.cache = cache or NoCache()
        self.cache_ttl = cache_ttl
        self.verify_ssl = verify_ssl
        
        # Set up the requests session
        self.session = requests.Session()
        self.session.verify = verify_ssl
        
        # Configure default headers
        default_headers = {
            'User-Agent': user_agent or f'LlamaAPI-Client/1.0',
            'Accept': 'application/json',
        }
        self.session.headers.update(default_headers)
        
        # Configure retry behavior
        if retries > 0:
            retry_strategy = Retry(
                total=retries,
                backoff_factor=0.3,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)
    
    def _build_url(self, endpoint: str) -> str:
        """
        Build the full URL for the API request.
        
        Args:
            endpoint: The API endpoint.
            
        Returns:
            The full URL.
        """
        # If the endpoint is already a full URL, return it as is
        if endpoint.startswith('http://') or endpoint.startswith('https://'):
            return endpoint
            
        # Otherwise, join it with the base URL
        endpoint = endpoint.lstrip('/')
        return f"{self.base_url}/{endpoint}"
    
    def _prepare_request(self, request: ApiRequest):
        """
        Prepare a request by applying authentication and middleware.
        
        Args:
            request: The request to prepare.
            
        Returns:
            The prepared request.
        """
        # Apply middleware (before request)
        for middleware in self.middleware:
            request = middleware.before_request(request)
            
        # Apply authentication if configured
        if self.auth:
            request = self.auth.authenticate(request)
            
        return request
    
    def _process_response(self, response: ApiResponse) -> ApiResponse:
        """
        Process a response by applying middleware.
        
        Args:
            response: The response to process.
            
        Returns:
            The processed response.
        """
        # Apply middleware (after response)
        for middleware in reversed(self.middleware):
            response = middleware.after_response(response)
            
        return response
    
    def _get_cache_key(self, request: ApiRequest) -> str:
        """
        Generate a cache key for the request.
        
        Args:
            request: The request to generate a key for.
            
        Returns:
            The cache key.
        """
        # Only cacheable methods
        if request.method not in ['GET', 'HEAD', 'OPTIONS']:
            return None
            
        # Build a key from the request attributes
        key_parts = [
            request.method,
            request.url,
            urllib.parse.urlencode(sorted(request.params.items())),
            json.dumps(request.headers, sort_keys=True),
        ]
        
        key = '::'.join(str(part) for part in key_parts)
        return hashlib.md5(key.encode('utf-8')).hexdigest()
    
    def request(
        self,
        method: str,
        endpoint: str,
        headers: Dict[str, str] = None,
        params: Dict[str, Any] = None,
        data: Any = None,
        json: Dict[str, Any] = None,
        files: Dict[str, BinaryIO] = None,
        timeout: Optional[int] = None,
        stream: bool = False,
        use_cache: bool = True,
    ) -> ApiResponse:
        """
        Make an API request.
        
        Args:
            method: The HTTP method.
            endpoint: The API endpoint.
            headers: Optional request headers.
            params: Optional query parameters.
            data: Optional request body.
            json: Optional JSON request body.
            files: Optional files to upload.
            timeout: Optional request timeout in seconds.
            stream: Whether to stream the response.
            use_cache: Whether to use the cache.
            
        Returns:
            The API response.
        """
        # Build the full URL
        url = self._build_url(endpoint)
        
        # Merge request-specific headers with default headers
        request_headers = {}
        if headers:
            request_headers.update(headers)
        
        # Create the API request
        request = ApiRequest(
            method=method,
            url=url,
            headers=request_headers,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=timeout or self.timeout,
            stream=stream,
        )
        
        # Prepare the request (apply middleware and authentication)
        request = self._prepare_request(request)
        
        # Check cache for cacheable requests
        cache_key = None
        if use_cache and method.upper() in ['GET', 'HEAD', 'OPTIONS']:
            cache_key = self._get_cache_key(request)
            cached_response = self.cache.get(cache_key)
            if cached_response:
                logger.debug(f"Cache hit for {method} {url}")
                return cached_response
        
        # Make the request
        try:
            logger.debug(f"Making {method} request to {url}")
            start_time = time.time()
            
            response = self.session.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                params=request.params,
                data=request.data,
                json=request.json,
                files=request.files,
                timeout=request.timeout,
                stream=request.stream,
            )
            
            elapsed = time.time() - start_time
            logger.debug(f"Request completed in {elapsed:.2f}s with status {response.status_code}")
            
            # Wrap the response
            api_response = ApiResponse(response)
            
            # Process the response (apply middleware)
            api_response = self._process_response(api_response)
            
            # Cache the response if cacheable
            if cache_key and not stream and 200 <= api_response.status_code < 300:
                self.cache.set(cache_key, api_response, ttl=self.cache_ttl)
            
            return api_response
            
        except requests.exceptions.Timeout:
            raise ApiError(f"Request timed out after {request.timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise ApiError(f"Connection error while connecting to {url}")
        except requests.exceptions.RequestException as e:
            raise ApiError(f"Request error: {str(e)}")
    
    def get(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a GET request."""
        return self.request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a POST request."""
        return self.request("POST", endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a PUT request."""
        return self.request("PUT", endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a DELETE request."""
        return self.request("DELETE", endpoint, **kwargs)
    
    def patch(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a PATCH request."""
        return self.request("PATCH", endpoint, **kwargs)
    
    def head(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make a HEAD request."""
        return self.request("HEAD", endpoint, **kwargs)
    
    def options(self, endpoint: str, **kwargs) -> ApiResponse:
        """Make an OPTIONS request."""
        return self.request("OPTIONS", endpoint, **kwargs)
    
    @contextmanager
    def stream(self, method: str, endpoint: str, **kwargs) -> ApiResponse:
        """
        Make a streaming request.
        
        Args:
            method: The HTTP method.
            endpoint: The API endpoint.
            **kwargs: Additional request parameters.
            
        Yields:
            The streaming API response.
        """
        # Set streaming mode
        kwargs['stream'] = True
        # Disable caching for streaming requests
        kwargs['use_cache'] = False
        
        # Make the request
        response = self.request(method, endpoint, **kwargs)
        
        try:
            # Yield the response for iteration
            yield response
        finally:
            # Ensure the response is closed
            response._response.close() 