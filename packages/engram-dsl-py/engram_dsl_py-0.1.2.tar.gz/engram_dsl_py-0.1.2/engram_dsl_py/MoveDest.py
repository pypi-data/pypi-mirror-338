from __future__ import annotations

import json
import sys
from pathlib import Path
from dataclasses import *
from typing import Any, Type, TypedDict
from typing import TYPE_CHECKING
from typing import TypedDict

# Add current directory to Python path to facilitate imports
_current_file = Path(__file__).resolve()
_current_dir = _current_file.parent
if str(_current_dir) not in sys.path:
    sys.path.append(str(_current_dir))

# Forward references for type checking only
if TYPE_CHECKING:
    from Position import Position
    from TYPE import TYPE


import inspect
from uuid import UUID as Uuid



@dataclass
class MoveDest_Entity(
    # Dataclass for the 'Entity' variant
):
    entity_id: Uuid

    def toJSON(self) -> str:
        """Serialize this dataclass instance to a JSON string."""
        return json.dumps(self._serialize())


    def _serialize(self) -> dict:
        """Convert this dataclass instance to a serializable dictionary with 'type' field."""
        # Add the variant type based on the class name
        variant_type = self.__class__.__name__.split('_', 1)[1] if '_' in self.__class__.__name__ else self.__class__.__name__
        result = {"type": variant_type}
        """Convert this dataclass instance to a serializable dictionary with 'type' field."""
        # Add the variant type based on the class name
        variant_type = self.__class__.__name__.split('_', 1)[1] if '_' in self.__class__.__name__ else self.__class__.__name__
        result = {"type": variant_type}
        for f in fields(self):
            key = f.name
            value = getattr(self, key)
            if value is not None:
                if isinstance(value, Uuid):
                    # Special handling for UUIDs - convert to string
                    result[key] = str(value)
                elif hasattr(value, '_serialize'):
                    result[key] = value._serialize()
                elif isinstance(value, list):
                    result[key] = [
                        str(item) if isinstance(item, Uuid) else
                        item._serialize() if hasattr(item, '_serialize') else 
                        item for item in value
                    ]
                elif isinstance(value, dict):
                    result[key] = {
                        k: str(v) if isinstance(v, Uuid) else
                        v._serialize() if hasattr(v, '_serialize') else 
                        v for k, v in value.items()
                    }
                else:
                    result[key] = value
        return result

    @classmethod
    def fromJSON(cls, json_str: str) -> 'MoveDest_Entity':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'MoveDest_Entity':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "entity_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class MoveDest_Position(
    # Dataclass for the 'Position' tuple variant
):
    field_0: Position

    def toJSON(self) -> str:
        """Serialize this dataclass instance to a JSON string."""
        return json.dumps(self._serialize())


    def _serialize(self) -> dict:
        """Convert this dataclass instance to a serializable dictionary with 'type' field."""
        # Add the variant type based on the class name
        variant_type = self.__class__.__name__.split('_', 1)[1] if '_' in self.__class__.__name__ else self.__class__.__name__
        result = {"type": variant_type}
        """Convert this dataclass instance to a serializable dictionary with 'type' field."""
        # Add the variant type based on the class name
        variant_type = self.__class__.__name__.split('_', 1)[1] if '_' in self.__class__.__name__ else self.__class__.__name__
        result = {"type": variant_type}
        for f in fields(self):
            key = f.name
            value = getattr(self, key)
            if value is not None:
                if isinstance(value, Uuid):
                    # Special handling for UUIDs - convert to string
                    result[key] = str(value)
                elif hasattr(value, '_serialize'):
                    result[key] = value._serialize()
                elif isinstance(value, list):
                    result[key] = [
                        str(item) if isinstance(item, Uuid) else
                        item._serialize() if hasattr(item, '_serialize') else 
                        item for item in value
                    ]
                elif isinstance(value, dict):
                    result[key] = {
                        k: str(v) if isinstance(v, Uuid) else
                        v._serialize() if hasattr(v, '_serialize') else 
                        v for k, v in value.items()
                    }
                else:
                    result[key] = value
        return result


    @classmethod
    def fromJSON(cls, json_str: str) -> 'MoveDest_Position':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        # Expects a list for tuple variants in JSON
        if isinstance(data, list):
             return cls(*data) # Unpack list directly
        elif isinstance(data, dict): # Allow dict for named tuple fields if needed
              return cls.fromDict(data)
        else:
              raise TypeError(f"Expected list or dict for tuple variant, got {type(data).__name__}")

    @classmethod
    def fromDict(cls, data: dict) -> 'MoveDest_Position':
        """Create an instance from a dictionary, handling named fields or list fallback"""
        # Try extracting named fields first (field_0, field_1, ...)
        kwargs = {}

        key = "field_0" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        # Check if we got all fields, otherwise try list unpacking
        if len(kwargs) == 1:
            return cls(**kwargs)
        elif isinstance(data, list) and len(data) == 1: 
            # Simple unpacking for lists
            return cls(*data)
        else:
            raise TypeError(f"Cannot create tuple variant {cls.__name__} from dict/list: {data}")
class MoveDest:
    """Namespace for MoveDest variants. Access variant classes directly as attributes."""
    Entity = MoveDest_Entity  # Complex variant (class reference)
    Position = MoveDest_Position  # Complex variant (class reference)

    @classmethod
    def fromJSON(cls, json_str):
        """Deserialize JSON string to the appropriate variant type"""
        data = json.loads(json_str)
        if isinstance(data, str):
            # Simple string variant
            if hasattr(cls, data):
                return getattr(cls, data)
            return data  # Unknown string variant
        elif isinstance(data, dict):
            # Complex variant with fields
            if "type" in data:
                variant_name = data["type"]
                if hasattr(cls, variant_name):
                    variant_class = getattr(cls, variant_name)
                    # Check if it's a class with fromDict method
                    if inspect.isclass(variant_class) and hasattr(variant_class, 'fromDict'):
                        # Strip the type field before passing to fromDict
                        variant_data = {k: v for k, v in data.items() if k != "type"}
                        return variant_class.fromDict(variant_data)
                    return variant_class  # Return the string constant
        # Default fallback - return None for unknown type
        return None

    @classmethod
    def create(cls, variant_name: str, **kwargs):
        """Factory method to create a variant instance with fields"""
        if hasattr(cls, variant_name):
            variant_class = getattr(cls, variant_name)
            if inspect.isclass(variant_class):  # Only call complex variants (classes)
                return variant_class(**kwargs)
            return variant_class  # Return the string constant
        raise ValueError(f"Unknown variant {variant_name}")