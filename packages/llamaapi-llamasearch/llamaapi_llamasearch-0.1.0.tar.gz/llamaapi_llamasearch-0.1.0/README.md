# LlamaAPI

Flexible API client and server utilities for LlamaSearch.ai applications.

## Features

### API Client

- **Flexible Authentication**: Support for API keys, Bearer tokens, Basic auth, and OAuth2
- **Middleware Pipeline**: Customize request/response handling with middleware
- **Caching**: Built-in caching system with memory, file, and Redis backends
- **Error Handling**: Comprehensive error types and handling
- **Retry Logic**: Automatic retry with configurable backoff strategies
- **Streaming Support**: Efficient handling of large data streams
- **Rate Limiting**: Client-side rate limiting to avoid API throttling

### API Server

- **Route Management**: Easy-to-use decorators for defining API routes
- **Request Validation**: JSON schema validation for requests
- **Middleware Support**: Global and route-specific middleware
- **Error Handling**: Comprehensive error handling with custom handlers
- **Authentication**: Built-in authentication utilities
- **CORS Support**: Simple CORS configuration
- **Async Support**: First-class support for async/await

## Installation

```bash
pip install llamaapi
```

## Client Example

```python
from llamaapi import create_client, ApiKeyAuth, LoggingMiddleware

# Create API client with API key authentication
client = create_client(
    base_url="https://api.example.com/v1",
    auth=ApiKeyAuth("your-api-key"),
    middleware=[LoggingMiddleware()],
    timeout=10,
    retries=3,
)

# Make GET request
response = client.get("users")
response.raise_for_status()
users = response.json()
print(f"Found {len(users)} users")

# Make POST request
new_user = {"name": "John Doe", "email": "john.doe@example.com"}
response = client.post("users", json=new_user)
response.raise_for_status()
created_user = response.json()
print(f"Created user: {created_user['name']}")
```

## Server Example

```python
from llamaapi import create_api, Request, Response, HttpMethod

# Create API instance
api = create_api(name="My API", version="1.0.0")

# Define a route
@api.route("/users", methods=HttpMethod.GET)
async def get_users(request: Request) -> Response:
    # Get data from your data source
    users = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    return Response().with_json(users)

# Define a route with path parameters
@api.route("/users/{user_id}", methods=HttpMethod.GET)
async def get_user(request: Request) -> Response:
    user_id = request.path_params.get("user_id")
    
    # Get user data from your data source
    user = {"id": user_id, "name": "John Doe"}
    
    return Response().with_json(user)
```

For more detailed examples, see the `examples` directory.

## Authentication

### API Key Auth

```python
from llamaapi import create_client, ApiKeyAuth

client = create_client(
    base_url="https://api.example.com",
    auth=ApiKeyAuth(api_key="your-api-key"),
)
```

### Bearer Token Auth

```python
from llamaapi import create_client, BearerAuth

client = create_client(
    base_url="https://api.example.com",
    auth=BearerAuth(token="your-token"),
)
```

### OAuth2 Auth

```python
from llamaapi import create_client, OAuth2Auth

auth = OAuth2Auth(
    token_url="https://auth.example.com/oauth/token",
    client_id="your-client-id",
    client_secret="your-client-secret",
    scope="read write",
)

# Use client credentials flow to get a token
auth.client_credentials_flow()

client = create_client(
    base_url="https://api.example.com",
    auth=auth,
)
```

## Advanced Client Features

### Middleware

```python
from llamaapi import (
    create_client, 
    LoggingMiddleware, 
    RetryMiddleware, 
    HeadersMiddleware,
)

middleware = [
    LoggingMiddleware(log_headers=True),
    RetryMiddleware(max_retries=3),
    HeadersMiddleware({"User-Agent": "MyApp/1.0"}),
]

client = create_client(
    base_url="https://api.example.com",
    middleware=middleware,
)
```

### Caching

```python
from llamaapi import create_client, MemoryCache, FileCache

# Memory cache
client = create_client(
    base_url="https://api.example.com",
    cache=MemoryCache(max_size=100),
)

# File cache
client = create_client(
    base_url="https://api.example.com",
    cache=FileCache(cache_dir=".cache"),
)
```

### Streaming

```python
from llamaapi import create_client

client = create_client(base_url="https://api.example.com")

# Stream large data
with client.stream("GET", "large-dataset") as response:
    for chunk in response.iter_content(chunk_size=1024):
        process_chunk(chunk)
```

## Advanced Server Features

### Request Validation

```python
from llamaapi import api, validate_json_schema

user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2},
        "email": {"type": "string", "format": "email"},
    },
    "required": ["name", "email"],
}

@api.route(
    "/users", 
    methods=HttpMethod.POST,
    middleware=[validate_json_schema(user_schema)]
)
async def create_user(request: Request) -> Response:
    user_data = request.json()
    # Create user with validated data
    return Response(status_code=201).with_json(new_user)
```

### Authentication

```python
from llamaapi import api, require_auth

# Define authentication middleware
async def auth_middleware(request: Request) -> Request:
    api_key = request.headers.get("X-API-Key")
    if api_key == "secret-key":
        request.context["user"] = {"id": "admin", "role": "admin"}
    return request

api.add_middleware(auth_middleware)

# Require authentication for specific routes
@api.route("/admin-only", methods=HttpMethod.GET)
@require_auth
async def admin_only(request: Request) -> Response:
    user = request.context["user"]  # This is guaranteed to exist
    return Response().with_json({"message": f"Hello, {user['id']}"})
```

## License

MIT License 