"""
OpenAPI specification generation.
"""
from typing import Dict, Any, List, Optional, Union, Type
import inspect
import json
import datetime
import re
import logging

from llamaapi.server import API, Route, HttpMethod
from llamaapi.schema import Schema, Field, String, Integer, Float, Boolean, List as ListField, Dict as DictField, Email, URL, DateTime

logger = logging.getLogger(__name__)

class OpenAPISpec:
    """
    OpenAPI specification.
    """
    def __init__(
        self,
        title: str,
        version: str,
        description: Optional[str] = None,
        servers: Optional[List[Dict[str, str]]] = None,
    ):
        self.spec = {
            "openapi": "3.0.3",
            "info": {
                "title": title,
                "version": version,
            },
            "paths": {},
            "components": {
                "schemas": {},
                "securitySchemes": {},
            },
        }
        
        if description:
            self.spec["info"]["description"] = description
        
        if servers:
            self.spec["servers"] = servers
    
    def add_path(
        self,
        path: str,
        method: str,
        operation_id: str,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        request_body: Optional[Dict[str, Any]] = None,
        responses: Optional[Dict[str, Any]] = None,
        parameters: Optional[List[Dict[str, Any]]] = None,
        security: Optional[List[Dict[str, List[str]]]] = None,
    ):
        """
        Add a path to the OpenAPI specification.
        """
        if path not in self.spec["paths"]:
            self.spec["paths"][path] = {}
        
        operation = {
            "operationId": operation_id,
        }
        
        if summary:
            operation["summary"] = summary
        
        if description:
            operation["description"] = description
        
        if tags:
            operation["tags"] = tags
        
        if request_body:
            operation["requestBody"] = request_body
        
        if responses:
            operation["responses"] = responses
        else:
            operation["responses"] = {
                "200": {
                    "description": "Successful operation",
                },
                "400": {
                    "description": "Bad request",
                },
                "500": {
                    "description": "Internal server error",
                },
            }
        
        if parameters:
            operation["parameters"] = parameters
        
        if security:
            operation["security"] = security
        
        self.spec["paths"][path][method.lower()] = operation
    
    def add_schema(self, name: str, schema: Dict[str, Any]):
        """
        Add a schema to the OpenAPI specification.
        """
        self.spec["components"]["schemas"][name] = schema
    
    def add_security_scheme(self, name: str, scheme: Dict[str, Any]):
        """
        Add a security scheme to the OpenAPI specification.
        """
        self.spec["components"]["securitySchemes"][name] = scheme
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Get the OpenAPI specification as a dictionary.
        """
        return self.spec
    
    def to_json(self) -> str:
        """
        Get the OpenAPI specification as a JSON string.
        """
        return json.dumps(self.spec, indent=2)


def _convert_field_to_openapi(field: Field) -> Dict[str, Any]:
    """
    Convert a schema field to an OpenAPI property definition.
    """
    openapi_type = "string"
    openapi_format = None
    openapi_items = None
    openapi_properties = None
    
    if isinstance(field, String):
        openapi_type = "string"
        if isinstance(field, Email):
            openapi_format = "email"
        elif isinstance(field, URL):
            openapi_format = "uri"
    elif isinstance(field, Integer):
        openapi_type = "integer"
        openapi_format = "int32"
    elif isinstance(field, Float):
        openapi_type = "number"
        openapi_format = "float"
    elif isinstance(field, Boolean):
        openapi_type = "boolean"
    elif isinstance(field, DateTime):
        openapi_type = "string"
        openapi_format = "date-time"
    elif isinstance(field, ListField):
        openapi_type = "array"
        openapi_items = _convert_field_to_openapi(field.items)
    elif isinstance(field, DictField):
        openapi_type = "object"
        if field.schema:
            openapi_properties = {}
            for key, schema_field in field.schema.items():
                openapi_properties[key] = _convert_field_to_openapi(schema_field)
    
    result = {"type": openapi_type}
    
    if openapi_format:
        result["format"] = openapi_format
    
    if openapi_items:
        result["items"] = openapi_items
    
    if openapi_properties:
        result["properties"] = openapi_properties
    
    if field.description:
        result["description"] = field.description
    
    if hasattr(field, "min_length") and field.min_length is not None:
        result["minLength"] = field.min_length
    
    if hasattr(field, "max_length") and field.max_length is not None:
        result["maxLength"] = field.max_length
    
    if hasattr(field, "pattern") and field.pattern is not None:
        result["pattern"] = field.pattern.pattern
    
    if hasattr(field, "enum") and field.enum is not None:
        result["enum"] = field.enum
    
    if hasattr(field, "minimum") and field.minimum is not None:
        result["minimum"] = field.minimum
    
    if hasattr(field, "maximum") and field.maximum is not None:
        result["maximum"] = field.maximum
    
    if hasattr(field, "min_items") and field.min_items is not None:
        result["minItems"] = field.min_items
    
    if hasattr(field, "max_items") and field.max_items is not None:
        result["maxItems"] = field.max_items
    
    if hasattr(field, "unique_items") and field.unique_items:
        result["uniqueItems"] = True
    
    if field.nullable:
        result["nullable"] = True
    
    if field.default is not None:
        result["default"] = field.default
    
    return result


def _convert_schema_to_openapi(schema: Schema) -> Dict[str, Any]:
    """
    Convert a schema to an OpenAPI schema definition.
    """
    properties = {}
    required = []
    
    for name, field in schema.fields.items():
        properties[name] = _convert_field_to_openapi(field)
        
        if field.required:
            required.append(name)
    
    result = {
        "type": "object",
        "properties": properties,
    }
    
    if required:
        result["required"] = required
    
    return result


def _extract_doc_info(route: Route) -> Dict[str, str]:
    """
    Extract documentation information from the route handler docstring.
    """
    result = {
        "summary": route.name,
        "description": "",
    }
    
    if route.handler.__doc__:
        lines = route.handler.__doc__.strip().split("\n")
        if lines:
            result["summary"] = lines[0].strip()
            if len(lines) > 1:
                result["description"] = "\n".join(line.strip() for line in lines[1:]).strip()
    
    return result


def generate_openapi_spec(
    api: API,
    base_path: str = "/",
    servers: Optional[List[Dict[str, str]]] = None,
    security_schemes: Optional[Dict[str, Dict[str, Any]]] = None,
) -> OpenAPISpec:
    """
    Generate an OpenAPI specification from an API instance.
    """
    spec = OpenAPISpec(
        title=api.title,
        version=api.version,
        description=api.description,
        servers=servers,
    )
    
    # Add security schemes
    if security_schemes:
        for name, scheme in security_schemes.items():
            spec.add_security_scheme(name, scheme)
    
    # Process routes
    for route_key, route in api.routes.items():
        path, methods = route_key.split(":")
        
        # Make sure path starts with '/'
        if not path.startswith("/"):
            path = f"/{path}"
        
        # Include base path
        if base_path and base_path != "/" and not path.startswith(base_path):
            path = f"{base_path.rstrip('/')}{path}"
        
        for method in methods.split(","):
            method = method.lower()
            
            # Get documentation info
            doc_info = _extract_doc_info(route)
            
            # Build operation ID
            operation_id = route.name
            if route.name.endswith(method):
                operation_id = route.name
            else:
                operation_id = f"{route.name}_{method}"
            
            # Build request body
            request_body = None
            if route.schema and method in ["post", "put", "patch"]:
                schema_name = f"{route.name.title().replace('_', '')}Schema"
                openapi_schema = _convert_schema_to_openapi(route.schema)
                
                spec.add_schema(schema_name, openapi_schema)
                
                request_body = {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{schema_name}",
                            },
                        },
                    },
                    "required": True,
                }
            
            # Add the path to the specification
            spec.add_path(
                path=path,
                method=method,
                operation_id=operation_id,
                summary=doc_info["summary"],
                description=doc_info["description"],
                request_body=request_body,
            )
    
    return spec


def generate_openapi_yaml(api: API, **kwargs) -> str:
    """
    Generate an OpenAPI specification as YAML.
    """
    try:
        import yaml
        spec = generate_openapi_spec(api, **kwargs)
        return yaml.dump(spec.to_dict(), sort_keys=False)
    except ImportError:
        raise ImportError(
            "The PyYAML package is required for YAML output. "
            "Install it with `pip install PyYAML`."
        )


class OpenAPISchema:
    """
    Represents an OpenAPI schema.
    """
    def __init__(
        self,
        title: str,
        version: str,
        description: Optional[str] = None,
        servers: Optional[List[Dict[str, str]]] = None,
    ):
        """
        Initialize OpenAPI schema.
        
        Args:
            title: API title.
            version: API version.
            description: API description.
            servers: List of server objects.
        """
        self.title = title
        self.version = version
        self.description = description
        self.servers = servers or []
        self.paths = {}
        self.components = {
            "schemas": {},
            "securitySchemes": {},
            "parameters": {},
            "responses": {},
            "requestBodies": {},
        }
        self.tags = []
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to OpenAPI dict.
        
        Returns:
            OpenAPI schema as a dictionary.
        """
        spec = {
            "openapi": "3.0.3",
            "info": {
                "title": self.title,
                "version": self.version,
            },
            "paths": self.paths,
            "components": self.components,
        }
        
        if self.description:
            spec["info"]["description"] = self.description
        
        if self.servers:
            spec["servers"] = self.servers
        
        if self.tags:
            spec["tags"] = self.tags
        
        return spec
    
    def to_json(self, **kwargs) -> str:
        """
        Convert to JSON string.
        
        Args:
            **kwargs: Additional arguments to pass to json.dumps.
            
        Returns:
            OpenAPI schema as a JSON string.
        """
        return json.dumps(self.to_dict(), **kwargs)


def generate_openapi_schema(
    api: API,
    additional_servers: Optional[List[Dict[str, str]]] = None,
    security_schemes: Optional[Dict[str, Dict[str, Any]]] = None,
    tags: Optional[List[Dict[str, str]]] = None,
) -> OpenAPISchema:
    """
    Generate OpenAPI schema from API instance.
    
    Args:
        api: API instance.
        additional_servers: Additional server objects.
        security_schemes: Security scheme definitions.
        tags: Tag definitions.
        
    Returns:
        OpenAPI schema.
    """
    schema = OpenAPISchema(
        title=api.name,
        version=api.version,
        servers=additional_servers,
    )
    
    # Add security schemes
    if security_schemes:
        schema.components["securitySchemes"] = security_schemes
    
    # Add tags
    if tags:
        schema.tags = tags
    
    # Process routes
    for route in api.routes:
        _add_route_to_schema(schema, route)
    
    return schema


def _add_route_to_schema(schema: OpenAPISchema, route: Route) -> None:
    """
    Add a route to the OpenAPI schema.
    
    Args:
        schema: OpenAPI schema.
        route: Route to add.
    """
    path = _normalize_path(route.path)
    method = route.method.lower()
    
    # Initialize path if it doesn't exist
    if path not in schema.paths:
        schema.paths[path] = {}
    
    # Extract documentation from handler docstring
    docstring = inspect.getdoc(route.handler) or ""
    
    # Parse docstring for summary and description
    summary, description = _parse_docstring(docstring)
    
    # Create operation object
    operation = {
        "summary": summary,
        "description": description,
        "parameters": _get_parameters(route),
        "responses": _get_responses(route),
    }
    
    # Add request body for methods that have one
    if method in ["post", "put", "patch"]:
        request_body = _get_request_body(route)
        if request_body:
            operation["requestBody"] = request_body
    
    # Add operation to path
    schema.paths[path][method] = operation


def _normalize_path(path: str) -> str:
    """
    Normalize a path to OpenAPI format.
    
    Args:
        path: Path to normalize.
        
    Returns:
        Normalized path.
    """
    # Convert {param} to {param}
    return re.sub(r'\{(\w+)\}', r'{\1}', path)


def _parse_docstring(docstring: str) -> tuple:
    """
    Parse a docstring into summary and description.
    
    Args:
        docstring: Docstring to parse.
        
    Returns:
        Tuple of (summary, description).
    """
    if not docstring:
        return ("", "")
    
    parts = docstring.strip().split("\n\n", 1)
    
    if len(parts) == 1:
        return (parts[0], "")
    else:
        return (parts[0], parts[1])


def _get_parameters(route: Route) -> List[Dict[str, Any]]:
    """
    Get parameters for a route.
    
    Args:
        route: Route to extract parameters from.
        
    Returns:
        List of parameter objects.
    """
    parameters = []
    
    # Add path parameters
    for param in route.path_params:
        parameters.append({
            "name": param,
            "in": "path",
            "required": True,
            "schema": {"type": "string"},
        })
    
    # Add query parameters
    for param in route.required_params:
        parameters.append({
            "name": param,
            "in": "query",
            "required": True,
            "schema": {"type": "string"},
        })
    
    return parameters


def _get_request_body(route: Route) -> Optional[Dict[str, Any]]:
    """
    Get request body for a route.
    
    Args:
        route: Route to extract request body from.
        
    Returns:
        Request body object or None.
    """
    # Look for a json schema validator in the middleware
    for middleware in route.middleware:
        # Check for validate_json_schema middleware
        if hasattr(middleware, "__closure__") and middleware.__name__ == "middleware":
            # Try to extract the schema from the closure
            for cell in middleware.__closure__:
                if hasattr(cell, "cell_contents") and isinstance(cell.cell_contents, dict):
                    schema = cell.cell_contents
                    return {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": schema
                            }
                        }
                    }
    
    # If required body fields are specified, create a simple schema
    if route.required_body_fields:
        schema = {
            "type": "object",
            "required": route.required_body_fields,
            "properties": {
                field: {"type": "string"} for field in route.required_body_fields
            }
        }
        return {
            "required": True,
            "content": {
                "application/json": {
                    "schema": schema
                }
            }
        }
    
    return None


def _get_responses(route: Route) -> Dict[str, Dict[str, Any]]:
    """
    Get responses for a route.
    
    Args:
        route: Route to extract responses from.
        
    Returns:
        Dictionary of response objects.
    """
    # Start with default responses
    responses = {
        "200": {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": {"type": "object"}
                }
            }
        },
        "400": {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "code": {"type": "string"},
                            "errors": {"type": "object"}
                        }
                    }
                }
            }
        },
        "401": {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "code": {"type": "string"}
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Not Found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "code": {"type": "string"}
                        }
                    }
                }
            }
        },
        "500": {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "code": {"type": "string"}
                        }
                    }
                }
            }
        }
    }
    
    # Add 201 response for POST methods
    if route.method == HttpMethod.POST:
        responses["201"] = {
            "description": "Created",
            "content": {
                "application/json": {
                    "schema": {"type": "object"}
                }
            }
        }
    
    # Look for @require_auth decorator
    if any(hasattr(mw, "__name__") and mw.__name__ == "wrapper" and "authentication" in str(mw) 
           for mw in route.middleware):
        responses["403"] = {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "code": {"type": "string"}
                        }
                    }
                }
            }
        }
    
    return responses


def add_openapi_route(api: API) -> None:
    """
    Add a route to serve the OpenAPI schema.
    
    Args:
        api: API instance.
    """
    async def openapi_handler(request):
        from llamaapi import Response
        
        schema = generate_openapi_schema(api)
        return Response().with_json(schema.to_dict())
    
    api.add_route("/openapi.json", HttpMethod.GET, openapi_handler) 