"""
Server utilities for building API endpoints.
"""
import inspect
import json
import logging
import time
import traceback
from dataclasses import dataclass, field
from enum import Enum
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Set, Type, Union, get_type_hints

from llamaapi.exceptions import ValidationError, ResourceNotFoundError, ServerError

# Set up logging
logger = logging.getLogger(__name__)

class HttpMethod(str, Enum):
    """HTTP methods supported by the API."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


@dataclass
class Request:
    """
    Represents an HTTP request to the API.
    """
    method: str
    path: str
    headers: Dict[str, str]
    query_params: Dict[str, str] = field(default_factory=dict)
    body: Optional[Any] = None
    path_params: Dict[str, str] = field(default_factory=dict)
    files: Dict[str, Any] = field(default_factory=dict)
    context: Dict[str, Any] = field(default_factory=dict)
    
    def json(self) -> Any:
        """
        Parse the request body as JSON.
        
        Returns:
            The parsed JSON data.
            
        Raises:
            ValidationError: If the body is not valid JSON.
        """
        if not self.body:
            return None
            
        if isinstance(self.body, (dict, list)):
            return self.body
            
        try:
            if isinstance(self.body, bytes):
                return json.loads(self.body.decode('utf-8'))
            elif isinstance(self.body, str):
                return json.loads(self.body)
        except json.JSONDecodeError as e:
            raise ValidationError(f"Invalid JSON: {str(e)}")
            
        return self.body
    
    def validate_required_params(self, required_params: List[str]) -> None:
        """
        Validate that all required query parameters are present.
        
        Args:
            required_params: List of required parameter names.
            
        Raises:
            ValidationError: If any required parameters are missing.
        """
        missing = [param for param in required_params if param not in self.query_params]
        if missing:
            raise ValidationError(
                f"Missing required query parameters: {', '.join(missing)}",
                errors={param: "This field is required" for param in missing}
            )
    
    def validate_required_body_fields(self, required_fields: List[str]) -> None:
        """
        Validate that all required fields are present in the request body.
        
        Args:
            required_fields: List of required field names.
            
        Raises:
            ValidationError: If any required fields are missing.
        """
        body = self.json()
        if not body or not isinstance(body, dict):
            raise ValidationError("Request body must be a JSON object")
            
        missing = [field for field in required_fields if field not in body]
        if missing:
            raise ValidationError(
                f"Missing required fields: {', '.join(missing)}",
                errors={field: "This field is required" for field in missing}
            )


@dataclass
class Response:
    """
    Represents an HTTP response from the API.
    """
    status_code: int = 200
    body: Optional[Any] = None
    headers: Dict[str, str] = field(default_factory=dict)
    
    def with_json(self, data: Any) -> 'Response':
        """
        Set the response body as JSON data.
        
        Args:
            data: The data to serialize as JSON.
            
        Returns:
            The updated response.
        """
        self.body = data
        self.headers['Content-Type'] = 'application/json'
        return self
    
    def with_status(self, status_code: int) -> 'Response':
        """
        Set the response status code.
        
        Args:
            status_code: The HTTP status code.
            
        Returns:
            The updated response.
        """
        self.status_code = status_code
        return self
    
    def with_header(self, name: str, value: str) -> 'Response':
        """
        Set a response header.
        
        Args:
            name: The header name.
            value: The header value.
            
        Returns:
            The updated response.
        """
        self.headers[name] = value
        return self


class Route:
    """
    Represents a route handler for an API endpoint.
    """
    def __init__(
        self,
        path: str,
        method: HttpMethod,
        handler: Callable,
        middleware: Optional[List[Callable]] = None,
        required_params: Optional[List[str]] = None,
        required_body_fields: Optional[List[str]] = None,
    ):
        """
        Initialize a route.
        
        Args:
            path: The URL path pattern.
            method: The HTTP method.
            handler: The function to handle requests to this route.
            middleware: Optional list of middleware functions for this route.
            required_params: Optional list of required query parameters.
            required_body_fields: Optional list of required body fields.
        """
        self.path = path
        self.method = method
        self.handler = handler
        self.middleware = middleware or []
        self.required_params = required_params or []
        self.required_body_fields = required_body_fields or []
        
        # Extract path parameter names from the path pattern
        self.path_params = []
        parts = path.split('/')
        for part in parts:
            if part.startswith('{') and part.endswith('}'):
                self.path_params.append(part[1:-1])
    
    def matches(self, method: str, path: str) -> bool:
        """
        Check if this route matches the given method and path.
        
        Args:
            method: The HTTP method.
            path: The request path.
            
        Returns:
            True if the route matches, False otherwise.
        """
        if method != self.method:
            return False
            
        # Split the paths into parts
        route_parts = self.path.split('/')
        path_parts = path.split('/')
        
        # Paths must have the same number of parts
        if len(route_parts) != len(path_parts):
            return False
            
        # Check each part
        for route_part, path_part in zip(route_parts, path_parts):
            # If it's a path parameter, it always matches
            if route_part.startswith('{') and route_part.endswith('}'):
                continue
            # Otherwise, it must match exactly
            if route_part != path_part:
                return False
                
        return True
    
    def extract_path_params(self, path: str) -> Dict[str, str]:
        """
        Extract path parameters from a URL path.
        
        Args:
            path: The request path.
            
        Returns:
            A dictionary of path parameters.
        """
        params = {}
        
        # Split the paths into parts
        route_parts = self.path.split('/')
        path_parts = path.split('/')
        
        # Extract values for path parameters
        for route_part, path_part in zip(route_parts, path_parts):
            if route_part.startswith('{') and route_part.endswith('}'):
                param_name = route_part[1:-1]
                params[param_name] = path_part
                
        return params
    
    async def handle(self, request: Request) -> Response:
        """
        Handle a request to this route.
        
        Args:
            request: The request to handle.
            
        Returns:
            The response.
        """
        # Extract path parameters
        request.path_params = self.extract_path_params(request.path)
        
        # Validate required parameters
        if self.required_params:
            request.validate_required_params(self.required_params)
            
        # Validate required body fields
        if self.required_body_fields and request.method in ['POST', 'PUT', 'PATCH']:
            request.validate_required_body_fields(self.required_body_fields)
        
        # Apply middleware
        for middleware in self.middleware:
            request = await middleware(request)
            
        # Call the handler
        return await self.handler(request)


class API:
    """
    API server for handling HTTP requests.
    """
    def __init__(self, name: str = "API", version: str = "1.0.0"):
        """
        Initialize the API.
        
        Args:
            name: The API name.
            version: The API version.
        """
        self.name = name
        self.version = version
        self.routes: List[Route] = []
        self.middleware: List[Callable] = []
        self.error_handlers: Dict[Type[Exception], Callable] = {}
        
        # Register default error handlers
        self.register_error_handler(ValidationError, self._handle_validation_error)
        self.register_error_handler(ResourceNotFoundError, self._handle_not_found)
        self.register_error_handler(Exception, self._handle_server_error)
    
    def add_middleware(self, middleware: Callable) -> None:
        """
        Add global middleware to the API.
        
        Args:
            middleware: The middleware function.
        """
        self.middleware.append(middleware)
    
    def register_error_handler(
        self, 
        exception_type: Type[Exception], 
        handler: Callable[[Exception], Response]
    ) -> None:
        """
        Register an error handler for a specific exception type.
        
        Args:
            exception_type: The exception type to handle.
            handler: The function to handle the exception.
        """
        self.error_handlers[exception_type] = handler
    
    def route(
        self,
        path: str,
        methods: Union[HttpMethod, List[HttpMethod]] = HttpMethod.GET,
        middleware: Optional[List[Callable]] = None,
        required_params: Optional[List[str]] = None,
        required_body_fields: Optional[List[str]] = None,
    ) -> Callable:
        """
        Register a route handler.
        
        Args:
            path: The URL path pattern.
            methods: The HTTP method(s) to handle.
            middleware: Optional route-specific middleware.
            required_params: Optional list of required query parameters.
            required_body_fields: Optional list of required body fields.
            
        Returns:
            A decorator for the route handler function.
        """
        def decorator(handler: Callable) -> Callable:
            if isinstance(methods, list):
                for method in methods:
                    self.add_route(path, method, handler, middleware, required_params, required_body_fields)
            else:
                self.add_route(path, methods, handler, middleware, required_params, required_body_fields)
            return handler
        return decorator
    
    def add_route(
        self,
        path: str,
        method: HttpMethod,
        handler: Callable,
        middleware: Optional[List[Callable]] = None,
        required_params: Optional[List[str]] = None,
        required_body_fields: Optional[List[str]] = None,
    ) -> None:
        """
        Add a route to the API.
        
        Args:
            path: The URL path pattern.
            method: The HTTP method.
            handler: The function to handle requests to this route.
            middleware: Optional route-specific middleware.
            required_params: Optional list of required query parameters.
            required_body_fields: Optional list of required body fields.
        """
        # Wrap the handler to make it async if it's not already
        async_handler = self._ensure_async(handler)
        
        # Create the route
        route = Route(
            path=path,
            method=method,
            handler=async_handler,
            middleware=middleware,
            required_params=required_params,
            required_body_fields=required_body_fields,
        )
        
        # Add the route
        self.routes.append(route)
    
    def _ensure_async(self, func: Callable) -> Callable:
        """
        Ensure a function is asynchronous.
        
        Args:
            func: The function to check/wrap.
            
        Returns:
            An asynchronous version of the function.
        """
        if inspect.iscoroutinefunction(func):
            return func
            
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
            
        return wrapper
    
    async def handle_request(self, request: Request) -> Response:
        """
        Handle an incoming request.
        
        Args:
            request: The request to handle.
            
        Returns:
            The response.
        """
        # Apply global middleware
        for middleware in self.middleware:
            try:
                middleware_result = middleware(request)
                if inspect.isawaitable(middleware_result):
                    request = await middleware_result
                else:
                    request = middleware_result
            except Exception as e:
                return await self._handle_exception(e)
        
        # Find a matching route
        for route in self.routes:
            if route.matches(request.method, request.path):
                try:
                    return await route.handle(request)
                except Exception as e:
                    return await self._handle_exception(e)
        
        # No matching route found
        return await self._handle_exception(
            ResourceNotFoundError(f"No route found for {request.method} {request.path}")
        )
    
    async def _handle_exception(self, exception: Exception) -> Response:
        """
        Handle an exception.
        
        Args:
            exception: The exception to handle.
            
        Returns:
            The response.
        """
        # Log the exception
        logger.exception(f"Error handling request: {str(exception)}")
        
        # Find the most specific handler for this exception type
        handler = None
        for exc_type, h in self.error_handlers.items():
            if isinstance(exception, exc_type):
                if handler is None or issubclass(exc_type, handler.__self__):
                    handler = h
        
        # Fall back to the default handler
        if handler is None:
            handler = self._handle_server_error
        
        # Call the handler
        try:
            result = handler(exception)
            if inspect.isawaitable(result):
                return await result
            return result
        except Exception as e:
            # If the error handler fails, use a simple fallback
            logger.exception(f"Error in exception handler: {str(e)}")
            return Response(
                status_code=500,
                body={"error": "Internal server error"},
                headers={"Content-Type": "application/json"}
            )
    
    async def _handle_validation_error(self, exception: ValidationError) -> Response:
        """
        Handle a validation error.
        
        Args:
            exception: The validation error.
            
        Returns:
            The response.
        """
        return Response(
            status_code=400,
            body={
                "error": str(exception),
                "errors": exception.errors,
                "code": exception.code,
            },
            headers={"Content-Type": "application/json"}
        )
    
    async def _handle_not_found(self, exception: ResourceNotFoundError) -> Response:
        """
        Handle a resource not found error.
        
        Args:
            exception: The not found error.
            
        Returns:
            The response.
        """
        return Response(
            status_code=404,
            body={
                "error": str(exception),
                "code": exception.code,
            },
            headers={"Content-Type": "application/json"}
        )
    
    async def _handle_server_error(self, exception: Exception) -> Response:
        """
        Handle a server error.
        
        Args:
            exception: The server error.
            
        Returns:
            The response.
        """
        return Response(
            status_code=500,
            body={
                "error": "Internal server error",
                "message": str(exception),
                "code": "server_error",
            },
            headers={"Content-Type": "application/json"}
        )


def create_api(name: str = "API", version: str = "1.0.0") -> API:
    """
    Create a new API instance.
    
    Args:
        name: The API name.
        version: The API version.
        
    Returns:
        A new API instance.
    """
    return API(name=name, version=version)


# Request validation and middleware utilities

def validate_json_schema(schema: Dict[str, Any]) -> Callable:
    """
    Create middleware to validate request JSON against a schema.
    
    Args:
        schema: The JSON schema to validate against.
        
    Returns:
        Middleware function.
    """
    try:
        # Try to import SchemaValidator from schema module
        from llamaapi.schema import SchemaValidator
        validator = SchemaValidator(schema)
        
        async def middleware(request: Request) -> Request:
            data = request.json()
            if data is not None:
                validator.validate(data)
            return request
            
        return middleware
    except ImportError:
        # Fall back to using jsonschema directly
        try:
            import jsonschema
        except ImportError:
            raise ImportError(
                "The jsonschema package is required for schema validation. "
                "Install it with: pip install jsonschema"
            )
        
        async def middleware(request: Request) -> Request:
            data = request.json()
            if data is not None:
                try:
                    jsonschema.validate(data, schema)
                except jsonschema.exceptions.ValidationError as e:
                    raise ValidationError(f"JSON validation failed: {str(e)}", errors={"schema": str(e)})
            return request
        
        return middleware


def require_auth(func: Callable) -> Callable:
    """
    Decorator to require authentication for a route handler.
    
    Args:
        func: The route handler function.
        
    Returns:
        Wrapped handler function.
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        if 'user' not in request.context:
            return Response(
                status_code=401,
                body={"error": "Authentication required", "code": "auth_required"},
                headers={"Content-Type": "application/json"}
            )
        return await func(request, *args, **kwargs)
    
    return wrapper


def log_request(request: Request) -> Request:
    """
    Middleware to log incoming requests.
    
    Args:
        request: The request to log.
        
    Returns:
        The request.
    """
    logger.info(f"{request.method} {request.path}")
    return request


def add_cors_headers(
    allow_origins: Union[str, List[str]] = "*",
    allow_methods: Union[str, List[str]] = "*",
    allow_headers: Union[str, List[str]] = "*",
    max_age: int = 86400,
) -> Callable:
    """
    Create middleware to add CORS headers to responses.
    
    Args:
        allow_origins: Allowed origins.
        allow_methods: Allowed methods.
        allow_headers: Allowed headers.
        max_age: Max age.
        
    Returns:
        Middleware function.
    """
    if isinstance(allow_origins, list):
        allow_origins = ', '.join(allow_origins)
    if isinstance(allow_methods, list):
        allow_methods = ', '.join(allow_methods)
    if isinstance(allow_headers, list):
        allow_headers = ', '.join(allow_headers)
    
    async def middleware(request: Request) -> Response:
        response = await request.next()
        response.headers['Access-Control-Allow-Origin'] = allow_origins
        response.headers['Access-Control-Allow-Methods'] = allow_methods
        response.headers['Access-Control-Allow-Headers'] = allow_headers
        response.headers['Access-Control-Max-Age'] = str(max_age)
        return response
    
    return middleware 