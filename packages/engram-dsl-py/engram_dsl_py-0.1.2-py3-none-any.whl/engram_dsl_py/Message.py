from __future__ import annotations

import json
import sys
from pathlib import Path
from dataclasses import *
from typing import Any
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
class Message:
    id: Uuid
    text: str
    did_send: bool

    def toJSON(self) -> str:
        """Serialize this dataclass to a JSON string."""
        return json.dumps(self._serialize())

    def _serialize(self) -> dict:
        """Convert this dataclass to a serializable dictionary."""
        result = {}
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
    def fromJSON(cls, json_str: str) -> 'Message':
        """Deserialize JSON string to a new instance."""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Message':
        """Create an instance from a dictionary.
           Recursively converts nested dictionaries if necessary.
        """
        if data is None:
            return cls()
            
        kwargs = {}
        for f in fields(cls):
            key = f.name
            value = data.get(key)
            if value is not None:
                # Handle complex types
                if hasattr(f.type, 'fromDict') and isinstance(value, dict):
                    kwargs[key] = f.type.fromDict(value)
                elif isinstance(value, list) and hasattr(f.type, '__origin__') and f.type.__origin__ is list:
                    # Handle lists - try to deserialize items if they seem to be complex objects
                    element_type = getattr(f.type, '__args__', [Any])[0]
                    if hasattr(element_type, 'fromDict'):
                        kwargs[key] = [element_type.fromDict(item) if isinstance(item, dict) else item 
                                      for item in value]
                    else:
                        kwargs[key] = value
                else:
                    # Use value directly
                    kwargs[key] = value
        
        return cls(**kwargs)