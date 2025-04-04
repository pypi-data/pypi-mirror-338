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
    from TYPE import TYPE


import inspect
from uuid import UUID as Uuid



@dataclass
class Trigger_NPCKilled(
    # Dataclass for the 'NPCKilled' variant
):
    id: Uuid

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
    def fromJSON(cls, json_str: str) -> 'Trigger_NPCKilled':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Trigger_NPCKilled':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Trigger_DialogueOptionChosen(
    # Dataclass for the 'DialogueOptionChosen' variant
):
    id: Uuid

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
    def fromJSON(cls, json_str: str) -> 'Trigger_DialogueOptionChosen':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Trigger_DialogueOptionChosen':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Trigger_InProximity(
    # Dataclass for the 'InProximity' variant
):
    id: Uuid

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
    def fromJSON(cls, json_str: str) -> 'Trigger_InProximity':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Trigger_InProximity':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Trigger_PhoneReplyChosen(
    # Dataclass for the 'PhoneReplyChosen' variant
):
    id: Uuid

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
    def fromJSON(cls, json_str: str) -> 'Trigger_PhoneReplyChosen':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Trigger_PhoneReplyChosen':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
class Trigger:
    """Namespace for Trigger variants. Access variant classes directly as attributes."""
    NPCKilled = Trigger_NPCKilled  # Complex variant (class reference)
    DialogueOptionChosen = Trigger_DialogueOptionChosen  # Complex variant (class reference)
    InProximity = Trigger_InProximity  # Complex variant (class reference)
    PhoneReplyChosen = Trigger_PhoneReplyChosen  # Complex variant (class reference)

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