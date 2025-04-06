"""
Schema validation utilities for API requests and responses.
"""
from typing import Dict, Any, Optional, List, Type, Union, Callable, get_type_hints
from enum import Enum
import re
import datetime
import jsonschema
import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """
    Raised when schema validation fails.
    """
    def __init__(self, message, errors=None):
        self.errors = errors or {}
        super().__init__(message)


class Field:
    """
    Base class for schema fields.
    """
    def __init__(
        self,
        required: bool = False,
        default: Any = None,
        description: Optional[str] = None,
        nullable: bool = False,
    ):
        self.required = required
        self.default = default
        self.description = description
        self.nullable = nullable
    
    def validate(self, value: Any, name: str) -> Any:
        """
        Validate the field value.
        """
        if value is None:
            if self.nullable:
                return None
            
            if self.required:
                raise ValidationError("This field is required")
            
            return self.default
        
        return self._validate(value, name)
    
    def _validate(self, value: Any, name: str) -> Any:
        """
        Validate the non-None value.
        """
        return value


class String(Field):
    """
    String field.
    """
    def __init__(
        self,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        enum: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = re.compile(pattern) if pattern else None
        self.enum = enum
    
    def _validate(self, value: Any, name: str) -> str:
        if not isinstance(value, str):
            raise ValidationError("Must be a string")
        
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(f"String must be at least {self.min_length} characters long")
        
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(f"String must be at most {self.max_length} characters long")
        
        if self.pattern and not self.pattern.match(value):
            raise ValidationError("String does not match the required pattern")
        
        if self.enum and value not in self.enum:
            valid_values = ", ".join(self.enum)
            raise ValidationError(f"Value must be one of: {valid_values}")
        
        return value


class Email(String):
    """
    Email field.
    """
    EMAIL_PATTERN = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    
    def __init__(self, **kwargs):
        kwargs["pattern"] = self.EMAIL_PATTERN
        super().__init__(**kwargs)


class URL(String):
    """
    URL field.
    """
    URL_PATTERN = r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
    
    def __init__(self, **kwargs):
        kwargs["pattern"] = self.URL_PATTERN
        super().__init__(**kwargs)


class Number(Field):
    """
    Base class for numeric fields.
    """
    def __init__(
        self,
        minimum: Optional[Union[int, float]] = None,
        maximum: Optional[Union[int, float]] = None,
        exclusive_minimum: bool = False,
        exclusive_maximum: bool = False,
        multiple_of: Optional[Union[int, float]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.exclusive_minimum = exclusive_minimum
        self.exclusive_maximum = exclusive_maximum
        self.multiple_of = multiple_of
    
    def _validate_range(self, value: Union[int, float], name: str):
        """
        Validate the numeric range.
        """
        if self.minimum is not None:
            if self.exclusive_minimum and value <= self.minimum:
                raise ValidationError(f"Value must be greater than {self.minimum}")
            elif not self.exclusive_minimum and value < self.minimum:
                raise ValidationError(f"Value must be greater than or equal to {self.minimum}")
        
        if self.maximum is not None:
            if self.exclusive_maximum and value >= self.maximum:
                raise ValidationError(f"Value must be less than {self.maximum}")
            elif not self.exclusive_maximum and value > self.maximum:
                raise ValidationError(f"Value must be less than or equal to {self.maximum}")
        
        if self.multiple_of is not None and value % self.multiple_of != 0:
            raise ValidationError(f"Value must be a multiple of {self.multiple_of}")


class Integer(Number):
    """
    Integer field.
    """
    def _validate(self, value: Any, name: str) -> int:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError("Must be an integer")
        
        self._validate_range(value, name)
        return value


class Float(Number):
    """
    Float field.
    """
    def _validate(self, value: Any, name: str) -> float:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValidationError("Must be a number")
        
        self._validate_range(value, name)
        return float(value)


class Boolean(Field):
    """
    Boolean field.
    """
    def _validate(self, value: Any, name: str) -> bool:
        if not isinstance(value, bool):
            raise ValidationError("Must be a boolean")
        
        return value


class DateTime(Field):
    """
    DateTime field.
    """
    def __init__(
        self,
        format: str = "iso8601",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.format = format
    
    def _validate(self, value: Any, name: str) -> datetime.datetime:
        if isinstance(value, datetime.datetime):
            return value
        
        if not isinstance(value, str):
            raise ValidationError("Must be a string in ISO 8601 format")
        
        try:
            return datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            raise ValidationError("Invalid ISO 8601 format")


class List(Field):
    """
    List field.
    """
    def __init__(
        self,
        items: Field,
        min_items: Optional[int] = None,
        max_items: Optional[int] = None,
        unique_items: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.items = items
        self.min_items = min_items
        self.max_items = max_items
        self.unique_items = unique_items
    
    def _validate(self, value: Any, name: str) -> List[Any]:
        if not isinstance(value, list):
            raise ValidationError("Must be a list")
        
        if self.min_items is not None and len(value) < self.min_items:
            raise ValidationError(f"List must have at least {self.min_items} items")
        
        if self.max_items is not None and len(value) > self.max_items:
            raise ValidationError(f"List must have at most {self.max_items} items")
        
        if self.unique_items and len(value) != len(set(str(item) for item in value)):
            raise ValidationError("List items must be unique")
        
        validated_items = []
        for i, item in enumerate(value):
            try:
                validated_item = self.items.validate(item, f"{name}[{i}]")
                validated_items.append(validated_item)
            except ValidationError as e:
                raise ValidationError({f"{name}[{i}]": e.errors})
        
        return validated_items


class Dict(Field):
    """
    Dictionary field.
    """
    def __init__(
        self,
        keys: Optional[Field] = None,
        values: Optional[Field] = None,
        schema: Optional[Dict[str, Field]] = None,
        additional_properties: bool = True,
        min_properties: Optional[int] = None,
        max_properties: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.keys = keys or String()
        self.values = values
        self.schema = schema or {}
        self.additional_properties = additional_properties
        self.min_properties = min_properties
        self.max_properties = max_properties
    
    def _validate(self, value: Any, name: str) -> Dict[str, Any]:
        if not isinstance(value, dict):
            raise ValidationError("Must be an object")
        
        if self.min_properties is not None and len(value) < self.min_properties:
            raise ValidationError(f"Object must have at least {self.min_properties} properties")
        
        if self.max_properties is not None and len(value) > self.max_properties:
            raise ValidationError(f"Object must have at most {self.max_properties} properties")
        
        validated_dict = {}
        
        # Validate schema properties
        for prop_name, field in self.schema.items():
            if prop_name in value:
                try:
                    validated_dict[prop_name] = field.validate(value[prop_name], f"{name}.{prop_name}")
                except ValidationError as e:
                    raise ValidationError({f"{name}.{prop_name}": e.errors})
            else:
                try:
                    validated_dict[prop_name] = field.validate(None, f"{name}.{prop_name}")
                except ValidationError as e:
                    raise ValidationError({f"{name}.{prop_name}": e.errors})
        
        # Validate additional properties
        if self.additional_properties:
            for key, val in value.items():
                if key not in self.schema:
                    try:
                        validated_key = self.keys.validate(key, f"{name} key")
                        if self.values:
                            validated_dict[validated_key] = self.values.validate(val, f"{name}.{key}")
                        else:
                            validated_dict[validated_key] = val
                    except ValidationError as e:
                        raise ValidationError({f"{name} key {key}": e.errors})
        else:
            # Check for unexpected properties
            unexpected = set(value.keys()) - set(self.schema.keys())
            if unexpected:
                unexpected_props = ", ".join(unexpected)
                raise ValidationError(f"Unexpected properties: {unexpected_props}")
        
        return validated_dict


class Schema:
    """
    Schema validator.
    """
    def __init__(self, **fields):
        self.fields = fields
    
    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate data against the schema.
        """
        if not isinstance(data, dict):
            raise ValidationError("Data must be an object")
        
        validator = Dict(schema=self.fields)
        return validator.validate(data, "root")


# Field shortcuts
fields = {
    "String": String,
    "Email": Email,
    "URL": URL,
    "Integer": Integer,
    "Float": Float,
    "Boolean": Boolean,
    "DateTime": DateTime,
    "List": List,
    "Dict": Dict,
}

class SchemaValidator:
    """
    Schema validator for JSON data.
    """
    def __init__(self, schema: Dict[str, Any]):
        """
        Initialize the schema validator.
        
        Args:
            schema: JSON schema to validate against.
        """
        self.schema = schema
    
    def validate(self, data: Any) -> Dict[str, Any]:
        """
        Validate data against the schema.
        
        Args:
            data: Data to validate.
            
        Returns:
            Validated data.
            
        Raises:
            ValidationError: If validation fails.
        """
        try:
            from llamaapi.exceptions import ValidationError
        except ImportError:
            # Define a simple ValidationError if the exceptions module is not available
            class ValidationError(Exception):
                def __init__(self, message, errors=None):
                    self.errors = errors or {}
                    super().__init__(message)
        
        try:
            jsonschema.validate(instance=data, schema=self.schema)
            return data
        except jsonschema.exceptions.ValidationError as e:
            logger.debug(f"Schema validation failed: {str(e)}")
            # Extract the path to the error
            path = "/".join(str(p) for p in e.path) if e.path else ""
            field = path.split("/")[-1] if path else "schema"
            raise ValidationError(
                f"Schema validation failed: {e.message}",
                errors={field: e.message}
            )

def create_schema_validator(schema: Dict[str, Any]) -> SchemaValidator:
    """
    Create a schema validator from a JSON schema.
    
    Args:
        schema: JSON schema to validate against.
        
    Returns:
        SchemaValidator instance.
    """
    return SchemaValidator(schema)

# Common JSON schema types and formats
def string_schema(
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    pattern: Optional[str] = None,
    format: Optional[str] = None,
    enum: Optional[List[str]] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a JSON schema for a string.
    
    Args:
        min_length: Minimum length.
        max_length: Maximum length.
        pattern: Regex pattern.
        format: String format (e.g., "email", "date-time").
        enum: Allowed values.
        description: Field description.
        
    Returns:
        JSON schema for a string.
    """
    schema = {"type": "string"}
    
    if min_length is not None:
        schema["minLength"] = min_length
    
    if max_length is not None:
        schema["maxLength"] = max_length
    
    if pattern is not None:
        schema["pattern"] = pattern
    
    if format is not None:
        schema["format"] = format
    
    if enum is not None:
        schema["enum"] = enum
    
    if description is not None:
        schema["description"] = description
    
    return schema

def number_schema(
    type: str = "number",
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    exclusive_minimum: Optional[bool] = None,
    exclusive_maximum: Optional[bool] = None,
    multiple_of: Optional[float] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a JSON schema for a number.
    
    Args:
        type: Number type ("number" or "integer").
        minimum: Minimum value.
        maximum: Maximum value.
        exclusive_minimum: Whether the minimum is exclusive.
        exclusive_maximum: Whether the maximum is exclusive.
        multiple_of: Multiple of this value.
        description: Field description.
        
    Returns:
        JSON schema for a number.
    """
    schema = {"type": type}
    
    if minimum is not None:
        schema["minimum"] = minimum
    
    if maximum is not None:
        schema["maximum"] = maximum
    
    if exclusive_minimum is not None:
        schema["exclusiveMinimum"] = exclusive_minimum
    
    if exclusive_maximum is not None:
        schema["exclusiveMaximum"] = exclusive_maximum
    
    if multiple_of is not None:
        schema["multipleOf"] = multiple_of
    
    if description is not None:
        schema["description"] = description
    
    return schema

def boolean_schema(description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a JSON schema for a boolean.
    
    Args:
        description: Field description.
        
    Returns:
        JSON schema for a boolean.
    """
    schema = {"type": "boolean"}
    
    if description is not None:
        schema["description"] = description
    
    return schema

def array_schema(
    items: Dict[str, Any],
    min_items: Optional[int] = None,
    max_items: Optional[int] = None,
    unique_items: Optional[bool] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a JSON schema for an array.
    
    Args:
        items: Schema for array items.
        min_items: Minimum number of items.
        max_items: Maximum number of items.
        unique_items: Whether items must be unique.
        description: Field description.
        
    Returns:
        JSON schema for an array.
    """
    schema = {
        "type": "array",
        "items": items,
    }
    
    if min_items is not None:
        schema["minItems"] = min_items
    
    if max_items is not None:
        schema["maxItems"] = max_items
    
    if unique_items is not None:
        schema["uniqueItems"] = unique_items
    
    if description is not None:
        schema["description"] = description
    
    return schema

def object_schema(
    properties: Dict[str, Dict[str, Any]],
    required: Optional[List[str]] = None,
    additional_properties: Optional[bool] = False,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a JSON schema for an object.
    
    Args:
        properties: Object properties.
        required: Required properties.
        additional_properties: Whether additional properties are allowed.
        description: Field description.
        
    Returns:
        JSON schema for an object.
    """
    schema = {
        "type": "object",
        "properties": properties,
        "additionalProperties": additional_properties,
    }
    
    if required is not None:
        schema["required"] = required
    
    if description is not None:
        schema["description"] = description
    
    return schema

# Specialized formats
def email_schema(description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a JSON schema for an email.
    
    Args:
        description: Field description.
        
    Returns:
        JSON schema for an email.
    """
    return string_schema(format="email", description=description)

def date_schema(description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a JSON schema for a date.
    
    Args:
        description: Field description.
        
    Returns:
        JSON schema for a date.
    """
    return string_schema(format="date", description=description)

def date_time_schema(description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a JSON schema for a date-time.
    
    Args:
        description: Field description.
        
    Returns:
        JSON schema for a date-time.
    """
    return string_schema(format="date-time", description=description)

def url_schema(description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a JSON schema for a URL.
    
    Args:
        description: Field description.
        
    Returns:
        JSON schema for a URL.
    """
    return string_schema(format="uri", description=description) 