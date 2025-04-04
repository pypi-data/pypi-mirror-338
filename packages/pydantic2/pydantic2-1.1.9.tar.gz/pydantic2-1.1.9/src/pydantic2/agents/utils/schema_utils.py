from typing import Dict, Any, Type, Optional
from pydantic import BaseModel, create_model, Field
import traceback

# Default values for different schema types
DEFAULT_VALUES = {
    "string": ("str", ""),
    "integer": ("int", 0),
    "number": ("float", 0.0),
    "boolean": ("bool", False),
    "array": ("list", []),
    "object": ("dict", {}),
}


def generate_default_value(schema: Dict[str, Any]) -> Any:
    """Generates a default value based on the JSON Schema type."""
    schema_type = schema.get("type", "string")  # Default to string
    return DEFAULT_VALUES.get(schema_type, ("Any", None))


def schema_to_model(schema: Dict[str, Any], model_name: Optional[str] = None) -> Type[BaseModel]:
    """
    Converts a JSON Schema dictionary into a Pydantic model class with default values.

    Args:
        schema: The JSON Schema dictionary.
        model_name: Optional name for the generated model class.

    Returns:
        A dynamically created Pydantic model class.
    """
    try:
        # Determine model name
        final_model_name = model_name or schema.get("title", "DynamicModel")
        final_model_name = "".join(c for c in final_model_name if c.isalnum())

        # Extract properties and generate annotations + default values
        properties = schema.get("properties", {})
        fields = {
            key: (eval(generate_default_value(value)[0]), Field(default=generate_default_value(value)[1]))
            for key, value in properties.items()
        }

        # Create dynamic model
        model_class = create_model(final_model_name, **fields)

        return model_class
    except Exception as e:
        traceback.print_exc()
        raise e


if __name__ == "__main__":
    # Example usage
    schema_example = {
        "title": "User",
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "is_active": {"type": "boolean"},
            "roles": {"type": "array"},
            "profile": {
                "type": "object",
                "properties": {
                    "age": {"type": "integer"},
                    "bio": {"type": "string"}
                }
            }
        }
    }

    # Create Pydantic model from JSON Schema
    UserModel = schema_to_model(schema_example)

    # Create instance with default values
    user_instance = UserModel()

    print(user_instance)
