"""
Exception classes for API client and server.
"""
from typing import Any, Dict, Optional


class ApiError(Exception):
    """
    Base exception for all API errors.
    """
    def __init__(
        self, 
        message: str, 
        code: Optional[str] = None,
        status_code: Optional[int] = None,
        response: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        request_id: Optional[str] = None,
    ):
        """
        Initialize API error.
        
        Args:
            message: The error message.
            code: The error code.
            status_code: The HTTP status code.
            response: The response object.
            headers: The response headers.
            request_id: The request ID.
        """
        self.message = message
        self.code = code
        self.status_code = status_code
        self.response = response
        self.headers = headers or {}
        self.request_id = request_id
        
        if response and hasattr(response, 'status_code'):
            self.status_code = response.status_code
            self.headers = response.headers
            
            # Try to extract request ID from headers
            if not request_id:
                self.request_id = response.headers.get('X-Request-ID') or response.headers.get('Request-ID')
        
        super().__init__(self.message)
    
    def __str__(self):
        parts = [self.message]
        
        if self.code:
            parts.append(f"Code: {self.code}")
        if self.status_code:
            parts.append(f"Status: {self.status_code}")
        if self.request_id:
            parts.append(f"Request ID: {self.request_id}")
            
        return " | ".join(parts)


class AuthenticationError(ApiError):
    """
    Exception for authentication failures.
    """
    def __init__(self, message: str = "Authentication failed", **kwargs):
        super().__init__(message, code="auth_error", **kwargs)


class AuthorizationError(ApiError):
    """
    Exception for authorization failures (e.g., insufficient permissions).
    """
    def __init__(self, message: str = "Not authorized", **kwargs):
        super().__init__(message, code="forbidden", **kwargs)


class RateLimitError(ApiError):
    """
    Exception for rate limit exceeded.
    """
    def __init__(
        self, 
        message: str = "Rate limit exceeded", 
        retry_after: Optional[int] = None,
        **kwargs
    ):
        """
        Initialize rate limit error.
        
        Args:
            message: The error message.
            retry_after: The number of seconds to wait before retrying.
            **kwargs: Additional keyword arguments for the parent class.
        """
        self.retry_after = retry_after
        
        # Extract retry-after from headers if available
        response = kwargs.get('response')
        if response and hasattr(response, 'headers'):
            retry_header = response.headers.get('Retry-After')
            if retry_header and retry_header.isdigit():
                self.retry_after = int(retry_header)
        
        super().__init__(message, code="rate_limit_exceeded", **kwargs)
    
    def __str__(self):
        base = super().__str__()
        if self.retry_after:
            return f"{base} | Retry after: {self.retry_after}s"
        return base


class ValidationError(ApiError):
    """
    Exception for request validation failures.
    """
    def __init__(
        self, 
        message: str = "Validation error", 
        errors: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize validation error.
        
        Args:
            message: The error message.
            errors: A dictionary of validation errors.
            **kwargs: Additional keyword arguments for the parent class.
        """
        self.errors = errors or {}
        super().__init__(message, code="validation_error", **kwargs)
    
    def __str__(self):
        base = super().__str__()
        if self.errors:
            errors_str = ", ".join(f"{k}: {v}" for k, v in self.errors.items())
            return f"{base} | Errors: {errors_str}"
        return base


class ResourceNotFoundError(ApiError):
    """
    Exception for resource not found.
    """
    def __init__(self, message: str = "Resource not found", resource: Optional[str] = None, **kwargs):
        """
        Initialize resource not found error.
        
        Args:
            message: The error message.
            resource: The name of the resource that wasn't found.
            **kwargs: Additional keyword arguments for the parent class.
        """
        self.resource = resource
        
        # Customize message if resource is provided
        if resource and message == "Resource not found":
            message = f"{resource} not found"
            
        super().__init__(message, code="not_found", **kwargs)


class ServerError(ApiError):
    """
    Exception for server-side errors.
    """
    def __init__(self, message: str = "Server error", **kwargs):
        super().__init__(message, code="server_error", **kwargs)


class TimeoutError(ApiError):
    """
    Exception for request timeouts.
    """
    def __init__(self, message: str = "Request timed out", **kwargs):
        super().__init__(message, code="timeout", **kwargs)


class ConnectionError(ApiError):
    """
    Exception for connection failures.
    """
    def __init__(self, message: str = "Connection failed", **kwargs):
        super().__init__(message, code="connection_error", **kwargs)


class ParseError(ApiError):
    """
    Exception for response parsing failures.
    """
    def __init__(self, message: str = "Failed to parse response", **kwargs):
        super().__init__(message, code="parse_error", **kwargs)


class ServiceUnavailableError(ApiError):
    """
    Exception for service unavailability.
    """
    def __init__(self, message: str = "Service unavailable", **kwargs):
        super().__init__(message, code="service_unavailable", **kwargs)


class APIConfigError(Exception):
    """
    Exception for API configuration errors.
    """
    pass 