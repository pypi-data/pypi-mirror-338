"""
Tests for the schema validation functionality.
"""
import unittest
import sys
import os
import datetime

# Add parent directory to path to import llamaapi
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llamaapi.schema import (
    Schema, ValidationError, Field,
    String, Integer, Float, Boolean, DateTime, Email, URL,
    List, Dict as DictField,
    fields
)

class TestSchemaValidation(unittest.TestCase):
    """Tests for schema validation."""
    
    def test_string_validation(self):
        """Test string field validation."""
        field = String(min_length=3, max_length=10)
        
        # Valid strings
        self.assertEqual(field.validate("abc", "test"), "abc")
        self.assertEqual(field.validate("abcdefg", "test"), "abcdefg")
        
        # Invalid strings
        with self.assertRaises(ValidationError):
            field.validate("ab", "test")  # Too short
        
        with self.assertRaises(ValidationError):
            field.validate("abcdefghijk", "test")  # Too long
        
        with self.assertRaises(ValidationError):
            field.validate(123, "test")  # Not a string
    
    def test_email_validation(self):
        """Test email field validation."""
        field = Email()
        
        # Valid emails
        self.assertEqual(field.validate("user@example.com", "email"), "user@example.com")
        self.assertEqual(field.validate("user.name+tag@example.co.uk", "email"), "user.name+tag@example.co.uk")
        
        # Invalid emails
        with self.assertRaises(ValidationError):
            field.validate("not-an-email", "email")
        
        with self.assertRaises(ValidationError):
            field.validate("missing@domain", "email")
    
    def test_integer_validation(self):
        """Test integer field validation."""
        field = Integer(minimum=1, maximum=100)
        
        # Valid integers
        self.assertEqual(field.validate(1, "number"), 1)
        self.assertEqual(field.validate(50, "number"), 50)
        self.assertEqual(field.validate(100, "number"), 100)
        
        # Invalid integers
        with self.assertRaises(ValidationError):
            field.validate(0, "number")  # Too small
        
        with self.assertRaises(ValidationError):
            field.validate(101, "number")  # Too large
        
        with self.assertRaises(ValidationError):
            field.validate("50", "number")  # Not an integer
    
    def test_float_validation(self):
        """Test float field validation."""
        field = Float(minimum=0.0, maximum=1.0)
        
        # Valid floats
        self.assertEqual(field.validate(0.0, "value"), 0.0)
        self.assertEqual(field.validate(0.5, "value"), 0.5)
        self.assertEqual(field.validate(1.0, "value"), 1.0)
        
        # Test integer to float conversion
        self.assertEqual(field.validate(0, "value"), 0.0)
        self.assertEqual(field.validate(1, "value"), 1.0)
        
        # Invalid floats
        with self.assertRaises(ValidationError):
            field.validate(-0.1, "value")  # Too small
        
        with self.assertRaises(ValidationError):
            field.validate(1.1, "value")  # Too large
    
    def test_boolean_validation(self):
        """Test boolean field validation."""
        field = Boolean()
        
        # Valid booleans
        self.assertEqual(field.validate(True, "flag"), True)
        self.assertEqual(field.validate(False, "flag"), False)
        
        # Invalid booleans
        with self.assertRaises(ValidationError):
            field.validate("true", "flag")  # String, not boolean
        
        with self.assertRaises(ValidationError):
            field.validate(1, "flag")  # Integer, not boolean
    
    def test_datetime_validation(self):
        """Test datetime field validation."""
        field = DateTime()
        
        # Valid datetimes
        self.assertIsInstance(field.validate("2023-01-01T12:00:00", "timestamp"), datetime.datetime)
        self.assertIsInstance(field.validate("2023-01-01T12:00:00Z", "timestamp"), datetime.datetime)
        self.assertIsInstance(field.validate("2023-01-01T12:00:00+00:00", "timestamp"), datetime.datetime)
        
        # Invalid datetimes
        with self.assertRaises(ValidationError):
            field.validate("2023-01-01", "timestamp")  # Not ISO format
        
        with self.assertRaises(ValidationError):
            field.validate("invalid", "timestamp")  # Not a date
    
    def test_list_validation(self):
        """Test list field validation."""
        field = List(items=String(), min_items=1, max_items=3)
        
        # Valid lists
        self.assertEqual(field.validate(["a"], "strings"), ["a"])
        self.assertEqual(field.validate(["a", "b"], "strings"), ["a", "b"])
        self.assertEqual(field.validate(["a", "b", "c"], "strings"), ["a", "b", "c"])
        
        # Invalid lists
        with self.assertRaises(ValidationError):
            field.validate([], "strings")  # Too few items
        
        with self.assertRaises(ValidationError):
            field.validate(["a", "b", "c", "d"], "strings")  # Too many items
        
        with self.assertRaises(ValidationError):
            field.validate([1, 2, 3], "strings")  # Items are not strings
    
    def test_dict_validation(self):
        """Test dictionary field validation."""
        field = DictField(schema={
            "name": String(required=True),
            "age": Integer(minimum=0),
            "email": Email(),
        })
        
        # Valid dict
        self.assertEqual(
            field.validate({"name": "John", "age": 30, "email": "john@example.com"}, "user"),
            {"name": "John", "age": 30, "email": "john@example.com"}
        )
        
        # Missing optional field
        self.assertEqual(
            field.validate({"name": "John"}, "user"),
            {"name": "John", "age": None, "email": None}
        )
        
        # Invalid: missing required field
        with self.assertRaises(ValidationError):
            field.validate({}, "user")
        
        # Invalid field value
        with self.assertRaises(ValidationError):
            field.validate({"name": "John", "age": -1}, "user")
    
    def test_schema_validation(self):
        """Test schema validation."""
        class UserSchema(Schema):
            username = fields.String(required=True, min_length=3)
            email = fields.Email(required=True)
            age = fields.Integer(minimum=18)
            is_active = fields.Boolean(default=True)
        
        # Valid data
        valid_data = {
            "username": "johndoe",
            "email": "john@example.com",
            "age": 25,
        }
        
        validated = UserSchema().validate(valid_data)
        self.assertEqual(validated["username"], "johndoe")
        self.assertEqual(validated["email"], "john@example.com")
        self.assertEqual(validated["age"], 25)
        self.assertEqual(validated["is_active"], True)  # Default value
        
        # Invalid data: missing required field
        with self.assertRaises(ValidationError):
            UserSchema().validate({"username": "johndoe"})
        
        # Invalid data: invalid field value
        with self.assertRaises(ValidationError):
            UserSchema().validate({
                "username": "johndoe",
                "email": "invalid-email",
                "age": 25,
            })
    
    def test_field_shortcuts(self):
        """Test field shortcuts."""
        self.assertIsInstance(fields["String"], type)
        self.assertIsInstance(fields["Email"], type)
        self.assertIsInstance(fields["Integer"], type)
        self.assertIsInstance(fields["Boolean"], type)

if __name__ == "__main__":
    unittest.main() 