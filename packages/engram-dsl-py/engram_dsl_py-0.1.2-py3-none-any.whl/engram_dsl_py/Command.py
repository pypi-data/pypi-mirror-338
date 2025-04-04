from __future__ import annotations

import json
import sys
from pathlib import Path
from dataclasses import *
from typing import Any, List, Optional, Type, TypedDict
from typing import TYPE_CHECKING
from typing import TypedDict

# Add current directory to Python path to facilitate imports
_current_file = Path(__file__).resolve()
_current_dir = _current_file.parent
if str(_current_dir) not in sys.path:
    sys.path.append(str(_current_dir))

# Forward references for type checking only
if TYPE_CHECKING:
    from Contact import Contact
    from DialogueNode import DialogueNode
    from Faction import Faction
    from Message import Message
    from MoveDest import MoveDest
    from NPC import NPC
    from Objective import Objective
    from PhoneChoice import PhoneChoice
    from Position import Position
    from PositionLog import PositionLog
    from Quest import Quest
    from TYPE import TYPE


import inspect
from uuid import UUID as Uuid



@dataclass
class Command_Move(
    # Dataclass for the 'Move' variant
):
    npc_id: Uuid
    dest: Optional[MoveDest]

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
    def fromJSON(cls, json_str: str) -> 'Command_Move':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_Move':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "npc_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "dest" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_SpawnNPCs(
    # Dataclass for the 'SpawnNPCs' variant
):
    npcs: List[NPC]

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
    def fromJSON(cls, json_str: str) -> 'Command_SpawnNPCs':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_SpawnNPCs':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "npcs" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_DespawnNPCs(
    # Dataclass for the 'DespawnNPCs' variant
):
    npcs: List[Uuid]

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
    def fromJSON(cls, json_str: str) -> 'Command_DespawnNPCs':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_DespawnNPCs':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "npcs" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_SetAttitude(
    # Dataclass for the 'SetAttitude' variant
):
    id: Uuid
    attitude: str

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
    def fromJSON(cls, json_str: str) -> 'Command_SetAttitude':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_SetAttitude':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "attitude" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_Print(
    # Dataclass for the 'Print' variant
):
    data: str

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
    def fromJSON(cls, json_str: str) -> 'Command_Print':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_Print':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "data" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_RegisterLocation(
    # Dataclass for the 'RegisterLocation' variant
):
    id: Uuid
    position: Position
    distance: float

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
    def fromJSON(cls, json_str: str) -> 'Command_RegisterLocation':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_RegisterLocation':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "position" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "distance" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_UpdateDialogue(
    # Dataclass for the 'UpdateDialogue' tuple variant
):
    field_0: DialogueNode

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
    def fromJSON(cls, json_str: str) -> 'Command_UpdateDialogue':
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
    def fromDict(cls, data: dict) -> 'Command_UpdateDialogue':
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
@dataclass
class Command_CreateQuest(
    # Dataclass for the 'CreateQuest' tuple variant
):
    field_0: Quest

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
    def fromJSON(cls, json_str: str) -> 'Command_CreateQuest':
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
    def fromDict(cls, data: dict) -> 'Command_CreateQuest':
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
@dataclass
class Command_CreateObjective(
    # Dataclass for the 'CreateObjective' variant
):
    quest_id: Uuid
    objective: Objective

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
    def fromJSON(cls, json_str: str) -> 'Command_CreateObjective':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_CreateObjective':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "quest_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "objective" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_CompleteObjective(
    # Dataclass for the 'CompleteObjective' variant
):
    id: Uuid
    did_fail: bool

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
    def fromJSON(cls, json_str: str) -> 'Command_CompleteObjective':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_CompleteObjective':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "did_fail" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_IncrementObjectiveCounter(
    # Dataclass for the 'IncrementObjectiveCounter' variant
):
    objective_id: Uuid

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
    def fromJSON(cls, json_str: str) -> 'Command_IncrementObjectiveCounter':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_IncrementObjectiveCounter':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "objective_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_CompleteQuest(
    # Dataclass for the 'CompleteQuest' variant
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
    def fromJSON(cls, json_str: str) -> 'Command_CompleteQuest':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_CompleteQuest':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_DeleteQuest(
    # Dataclass for the 'DeleteQuest' variant
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
    def fromJSON(cls, json_str: str) -> 'Command_DeleteQuest':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_DeleteQuest':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_UnregisterLocation(
    # Dataclass for the 'UnregisterLocation' variant
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
    def fromJSON(cls, json_str: str) -> 'Command_UnregisterLocation':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_UnregisterLocation':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_AttachDialogue(
    # Dataclass for the 'AttachDialogue' variant
):
    npc_id: Uuid
    dialogue: DialogueNode

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
    def fromJSON(cls, json_str: str) -> 'Command_AttachDialogue':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_AttachDialogue':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "npc_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "dialogue" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_CreateContact(
    # Dataclass for the 'CreateContact' tuple variant
):
    field_0: Contact

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
    def fromJSON(cls, json_str: str) -> 'Command_CreateContact':
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
    def fromDict(cls, data: dict) -> 'Command_CreateContact':
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
@dataclass
class Command_UpdateMessage(
    # Dataclass for the 'UpdateMessage' tuple variant
):
    field_0: Message

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
    def fromJSON(cls, json_str: str) -> 'Command_UpdateMessage':
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
    def fromDict(cls, data: dict) -> 'Command_UpdateMessage':
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
@dataclass
class Command_UpdateChoice(
    # Dataclass for the 'UpdateChoice' tuple variant
):
    field_0: PhoneChoice

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
    def fromJSON(cls, json_str: str) -> 'Command_UpdateChoice':
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
    def fromDict(cls, data: dict) -> 'Command_UpdateChoice':
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
@dataclass
class Command_ReplaceChoices(
    # Dataclass for the 'ReplaceChoices' variant
):
    contact_id: Uuid
    messages: List[Message]
    choices: List[PhoneChoice]

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
    def fromJSON(cls, json_str: str) -> 'Command_ReplaceChoices':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_ReplaceChoices':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "contact_id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "messages" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "choices" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_DeleteContact(
    # Dataclass for the 'DeleteContact' variant
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
    def fromJSON(cls, json_str: str) -> 'Command_DeleteContact':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_DeleteContact':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "id" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_SetOTP(
    # Dataclass for the 'SetOTP' variant
):
    otp: Optional[str]

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
    def fromJSON(cls, json_str: str) -> 'Command_SetOTP':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_SetOTP':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "otp" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_UpdatePositionLogs(
    # Dataclass for the 'UpdatePositionLogs' variant
):
    updated: List[PositionLog]
    deleted: List[Uuid]

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
    def fromJSON(cls, json_str: str) -> 'Command_UpdatePositionLogs':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_UpdatePositionLogs':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "updated" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        key = "deleted" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
@dataclass
class Command_CreateFactions(
    # Dataclass for the 'CreateFactions' variant
):
    factions: List[Faction]

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
    def fromJSON(cls, json_str: str) -> 'Command_CreateFactions':
        """Deserialize JSON string to a new instance"""
        data = json.loads(json_str)
        return cls.fromDict(data)

    @classmethod
    def fromDict(cls, data: dict) -> 'Command_CreateFactions':
        """Create an instance from a dictionary, handling nested types"""
        kwargs = {}

        key = "factions" 
        value = data.get(key)
        if value is not None:
            kwargs[key] = value
        # else: field will be None or default if Optional/has default
        return cls(**kwargs)
class Command:
    """Namespace for Command variants. Access variant classes directly as attributes."""
    Move = Command_Move  # Complex variant (class reference)
    SpawnNPCs = Command_SpawnNPCs  # Complex variant (class reference)
    DespawnNPCs = Command_DespawnNPCs  # Complex variant (class reference)
    SetAttitude = Command_SetAttitude  # Complex variant (class reference)
    Print = Command_Print  # Complex variant (class reference)
    ClearNPCs = "ClearNPCs"  # Simple variant (string constant)
    RegisterLocation = Command_RegisterLocation  # Complex variant (class reference)
    UpdateDialogue = Command_UpdateDialogue  # Complex variant (class reference)
    CreateQuest = Command_CreateQuest  # Complex variant (class reference)
    CreateObjective = Command_CreateObjective  # Complex variant (class reference)
    CompleteObjective = Command_CompleteObjective  # Complex variant (class reference)
    IncrementObjectiveCounter = Command_IncrementObjectiveCounter  # Complex variant (class reference)
    CompleteQuest = Command_CompleteQuest  # Complex variant (class reference)
    DeleteQuest = Command_DeleteQuest  # Complex variant (class reference)
    UnregisterLocation = Command_UnregisterLocation  # Complex variant (class reference)
    AttachDialogue = Command_AttachDialogue  # Complex variant (class reference)
    CreateContact = Command_CreateContact  # Complex variant (class reference)
    UpdateMessage = Command_UpdateMessage  # Complex variant (class reference)
    UpdateChoice = Command_UpdateChoice  # Complex variant (class reference)
    ReplaceChoices = Command_ReplaceChoices  # Complex variant (class reference)
    DeleteContact = Command_DeleteContact  # Complex variant (class reference)
    SetOTP = Command_SetOTP  # Complex variant (class reference)
    UpdatePositionLogs = Command_UpdatePositionLogs  # Complex variant (class reference)
    CreateFactions = Command_CreateFactions  # Complex variant (class reference)

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