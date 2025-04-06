"""
Middleware components for processing API requests and responses.
"""
import logging
import time
import gzip
import json
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Union
import random
import threading

logger = logging.getLogger(__name__)

class Middleware:
    """
    Base class for middleware components.
    """
    def before_request(self, request):
        """
        Process a request before it is sent.
        
        Args:
            request: The request to process.
            
        Returns:
            The processed request.
        """
        return request
    
    def after_response(self, response):
        """
        Process a response after it is received.
        
        Args:
            response: The response to process.
            
        Returns:
            The processed response.
        """
        return response


class LoggingMiddleware(Middleware):
    """
    Middleware for logging requests and responses.
    """
    def __init__(
        self, 
        logger_name: str = "llamaapi.client",
        log_level: int = logging.INFO,
        log_headers: bool = False,
        log_body: bool = False,
        max_body_length: int = 1000,
    ):
        """
        Initialize logging middleware.
        
        Args:
            logger_name: Name of the logger to use.
            log_level: Logging level to use.
            log_headers: Whether to log request/response headers.
            log_body: Whether to log request/response bodies.
            max_body_length: Maximum length of body to log.
        """
        self.logger = logging.getLogger(logger_name)
        self.log_level = log_level
        self.log_headers = log_headers
        self.log_body = log_body
        self.max_body_length = max_body_length
    
    def before_request(self, request):
        """Log details about the outgoing request."""
        self.logger.log(self.log_level, f"Request: {request.method} {request.url}")
        
        if self.log_headers and request.headers:
            # Redact sensitive headers
            headers = request.headers.copy()
            for header in headers:
                if header.lower() in ["authorization", "x-api-key", "api-key"]:
                    headers[header] = "REDACTED"
            self.logger.log(self.log_level, f"Request Headers: {headers}")
        
        if self.log_body:
            body = None
            if request.json:
                body = json.dumps(request.json)
            elif request.data:
                try:
                    if isinstance(request.data, (dict, list)):
                        body = json.dumps(request.data)
                    elif isinstance(request.data, str):
                        body = request.data
                    else:
                        body = str(request.data)
                except:
                    body = "Unable to serialize request data"
            
            if body:
                if len(body) > self.max_body_length:
                    body = body[:self.max_body_length] + "... (truncated)"
                self.logger.log(self.log_level, f"Request Body: {body}")
        
        return request
    
    def after_response(self, response):
        """Log details about the incoming response."""
        self.logger.log(
            self.log_level, 
            f"Response: {response.status_code} from {response._response.request.method} {response._response.url}"
        )
        
        if self.log_headers and response.headers:
            self.logger.log(self.log_level, f"Response Headers: {dict(response.headers)}")
        
        if self.log_body and not response._response._content_consumed:
            try:
                if 'application/json' in response.headers.get('Content-Type', ''):
                    body = json.dumps(response.json())
                    if len(body) > self.max_body_length:
                        body = body[:self.max_body_length] + "... (truncated)"
                    self.logger.log(self.log_level, f"Response Body: {body}")
            except:
                self.logger.log(self.log_level, "Unable to log response body")
        
        return response


class RetryMiddleware(Middleware):
    """
    Middleware for automatically retrying failed requests.
    """
    def __init__(
        self,
        max_retries: int = 3,
        retry_status_codes: List[int] = None,
        retry_methods: List[str] = None,
        backoff_factor: float = 0.3,
        jitter: bool = True,
    ):
        """
        Initialize retry middleware.
        
        Args:
            max_retries: Maximum number of retry attempts.
            retry_status_codes: HTTP status codes that should trigger a retry.
            retry_methods: HTTP methods that should be retried.
            backoff_factor: Exponential backoff factor.
            jitter: Whether to add jitter to backoff times.
        """
        self.max_retries = max_retries
        self.retry_status_codes = retry_status_codes or [429, 500, 502, 503, 504]
        self.retry_methods = [m.upper() for m in (retry_methods or ["GET", "HEAD", "OPTIONS", "PUT", "DELETE"])]
        self.backoff_factor = backoff_factor
        self.jitter = jitter
        
        # Track retries using thread-local storage
        self.local = threading.local()
    
    def _should_retry(self, response) -> bool:
        """
        Determine if a request should be retried.
        
        Args:
            response: The response to check.
            
        Returns:
            True if the request should be retried, False otherwise.
        """
        # Check if we've exceeded the maximum number of retries
        if not hasattr(self.local, 'retries'):
            self.local.retries = 0
        
        if self.local.retries >= self.max_retries:
            return False
        
        # Check if the request method is allowed to be retried
        request = response._response.request
        if request.method not in self.retry_methods:
            return False
        
        # Check if the status code is one that should be retried
        if response.status_code not in self.retry_status_codes:
            return False
        
        return True
    
    def _get_retry_after(self, response) -> Optional[float]:
        """
        Get the Retry-After value from the response.
        
        Args:
            response: The response to check.
            
        Returns:
            The retry after value in seconds, or None if not available.
        """
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            try:
                if retry_after.isdigit():
                    return float(retry_after)
                else:
                    # Try to parse as a HTTP date
                    retry_date = datetime.strptime(retry_after, "%a, %d %b %Y %H:%M:%S %Z")
                    now = datetime.now()
                    return max(0, (retry_date - now).total_seconds())
            except (ValueError, TypeError):
                pass
        return None
    
    def _calculate_backoff_time(self, retry_count: int) -> float:
        """
        Calculate the backoff time for a retry.
        
        Args:
            retry_count: The current retry count (0-based).
            
        Returns:
            The backoff time in seconds.
        """
        backoff = self.backoff_factor * (2 ** retry_count)
        
        if self.jitter:
            backoff = backoff * (0.5 + random.random())
        
        return backoff
    
    def after_response(self, response):
        """
        Check if the request should be retried and handle backoff.
        """
        if not hasattr(self.local, 'retries'):
            self.local.retries = 0
        
        if not self._should_retry(response):
            # Reset retry count for next request
            self.local.retries = 0
            return response
        
        # Increment retry count
        self.local.retries += 1
        retry_count = self.local.retries
        
        # Calculate backoff time
        retry_after = self._get_retry_after(response)
        if retry_after is None:
            retry_after = self._calculate_backoff_time(retry_count - 1)
        
        logger.info(
            f"Retrying request ({retry_count}/{self.max_retries}) "
            f"to {response._response.request.method} {response._response.url} "
            f"after {retry_after:.2f} seconds"
        )
        
        # Sleep for the backoff time
        time.sleep(retry_after)
        
        # The actual retry happens in the client, which will call the middleware again
        return response


class HeadersMiddleware(Middleware):
    """
    Middleware for adding custom headers to requests.
    """
    def __init__(self, headers: Dict[str, str] = None):
        """
        Initialize headers middleware.
        
        Args:
            headers: Dictionary of headers to add to all requests.
        """
        self.headers = headers or {}
    
    def before_request(self, request):
        """Add custom headers to the request."""
        for name, value in self.headers.items():
            if name not in request.headers:
                request.headers[name] = value
        return request


class TimingMiddleware(Middleware):
    """
    Middleware for measuring request/response times.
    """
    def __init__(self, add_header: bool = True):
        """
        Initialize timing middleware.
        
        Args:
            add_header: Whether to add timing information to response headers.
        """
        self.add_header = add_header
        self.local = threading.local()
    
    def before_request(self, request):
        """Record the start time of the request."""
        self.local.start_time = time.time()
        return request
    
    def after_response(self, response):
        """Calculate and add timing information to the response."""
        if hasattr(self.local, 'start_time'):
            elapsed = time.time() - self.local.start_time
            
            if self.add_header:
                # Add timing information to response headers
                response.headers['X-Request-Time'] = f"{elapsed:.6f}s"
            
            logger.debug(f"Request completed in {elapsed:.6f} seconds")
            
            # Clear the start time
            delattr(self.local, 'start_time')
        
        return response


class CompressionMiddleware(Middleware):
    """
    Middleware for handling request and response compression.
    """
    def __init__(self, compress_requests: bool = True, min_size: int = 1024):
        """
        Initialize compression middleware.
        
        Args:
            compress_requests: Whether to compress request bodies.
            min_size: Minimum body size to compress in bytes.
        """
        self.compress_requests = compress_requests
        self.min_size = min_size
    
    def before_request(self, request):
        """Compress request body if appropriate."""
        if not self.compress_requests:
            return request
        
        # Only compress JSON request bodies
        if request.json and 'Content-Encoding' not in request.headers:
            json_data = json.dumps(request.json).encode('utf-8')
            
            # Only compress if the body is large enough
            if len(json_data) >= self.min_size:
                compressed_data = gzip.compress(json_data)
                
                # Only use compression if it's smaller
                if len(compressed_data) < len(json_data):
                    request.headers['Content-Encoding'] = 'gzip'
                    request.data = compressed_data
                    request.json = None
                    request.headers['Content-Type'] = 'application/json'
        
        return request
    
    def after_response(self, response):
        """Handle decompression of response if needed (usually done by requests)."""
        return response


class RateLimitMiddleware(Middleware):
    """
    Middleware for client-side rate limiting.
    """
    def __init__(
        self,
        calls_per_second: float = 10.0,
        burst: int = 10,
        scope: str = "global",
    ):
        """
        Initialize rate limit middleware.
        
        Args:
            calls_per_second: Maximum calls per second allowed.
            burst: Number of consecutive requests allowed before throttling.
            scope: Rate limit scope ('global', 'host', or 'endpoint').
        """
        self.calls_per_second = calls_per_second
        self.burst = burst
        self.scope = scope.lower()
        
        # Use a token bucket algorithm
        self.tokens = burst
        self.last_refill = time.time()
        self.lock = threading.RLock()
        
        # Separate buckets for different scopes
        self.host_buckets = {}
        self.endpoint_buckets = {}
    
    def _get_bucket_key(self, request) -> str:
        """
        Get the bucket key for the request based on the scope.
        
        Args:
            request: The request.
            
        Returns:
            The bucket key.
        """
        if self.scope == 'host':
            from urllib.parse import urlparse
            parsed = urlparse(request.url)
            return parsed.netloc
        elif self.scope == 'endpoint':
            from urllib.parse import urlparse
            parsed = urlparse(request.url)
            return f"{parsed.netloc}{parsed.path}"
        else:
            return "global"
    
    def _get_tokens(self, key: str) -> Tuple[float, float]:
        """
        Get the current tokens and last refill time for a bucket.
        
        Args:
            key: The bucket key.
            
        Returns:
            Tuple of (tokens, last_refill).
        """
        if self.scope == 'host':
            if key not in self.host_buckets:
                self.host_buckets[key] = (self.burst, time.time())
            return self.host_buckets[key]
        elif self.scope == 'endpoint':
            if key not in self.endpoint_buckets:
                self.endpoint_buckets[key] = (self.burst, time.time())
            return self.endpoint_buckets[key]
        else:
            return (self.tokens, self.last_refill)
    
    def _update_tokens(self, key: str, tokens: float, last_refill: float) -> None:
        """
        Update the tokens and last refill time for a bucket.
        
        Args:
            key: The bucket key.
            tokens: The new token value.
            last_refill: The new last refill time.
        """
        if self.scope == 'host':
            self.host_buckets[key] = (tokens, last_refill)
        elif self.scope == 'endpoint':
            self.endpoint_buckets[key] = (tokens, last_refill)
        else:
            self.tokens = tokens
            self.last_refill = last_refill
    
    def before_request(self, request):
        """
        Apply rate limiting to the request.
        """
        with self.lock:
            key = self._get_bucket_key(request)
            tokens, last_refill = self._get_tokens(key)
            
            # Refill tokens based on time elapsed
            now = time.time()
            elapsed = now - last_refill
            new_tokens = min(self.burst, tokens + elapsed * self.calls_per_second)
            
            # If we have at least one token, proceed with the request
            if new_tokens >= 1:
                # Update the bucket
                self._update_tokens(key, new_tokens - 1, now)
            else:
                # We need to wait
                wait_time = (1 - new_tokens) / self.calls_per_second
                logger.debug(f"Rate limit exceeded, waiting {wait_time:.2f} seconds")
                time.sleep(wait_time)
                
                # Update the bucket (consumed one token, refill time is now)
                self._update_tokens(key, 0, now)
        
        return request 