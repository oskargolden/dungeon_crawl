from dataclasses import dataclass
from typing import Optional
from game_logic.game_object import GameObject


@dataclass
class Entity:
    """
    Represents a single, unique instance of an object in the game world.

    An Entity is a mutable object that represents a unique item, character, or
    object with a state in the game (e.g., its position on the map). It is
    created by combining a frozen GameObject template (for its base properties)
    with mutable, instance-specific data (like coordinates).

    This is the base class for all other mutable entities, such as ActorEntity
    or ItemEntity.

    Attributes:
        base (GameObject): The immutable `GameObject` template that defines
            the intrinsic properties (name, symbol, etc.) of this entity.
        x (Optional[int]): The entity's current x-coordinate on the map.
            Is `None` if the entity is not on the map (e.g., in an inventory).
        y (Optional[int]): The entity's current y-coordinate on the map.
            Is `None` if the entity is not on the map.
        z (Optional[int]): The entity's current z-coordinate on the map.
            Is `None` if the entity is not on the map.     
        custom_name (Optional[str]): An optional unique name for this entity 
            Example: "Excalibur" for a sword, or "Bob" for a character.
    """
    base: GameObject          # A reference to its frozen template
    x: Optional[int] = None   # Its current x-coordinate (can be changed)
    y: Optional[int] = None   # Its current y-coordinate (can be changed)
    z: Optional[int] = None   # Its current z-coordinate (can be changed)
    # Add an optional field to store a unique name
    custom_name: Optional[str] = None


@dataclass
class ItemEntity(Entity):
    """
    Represents a unique, mutable instance of an item in the game world.

    This class inherits from Entity, gaining a template and a location, and
    adds its own mutable state, such as durability.

    Attributes:
        current_durability (int): The current durability of the item. This
            can be modified as the item is used.
    """
    # Example of a mutable property unique to item instances
    current_durability: int = 100
