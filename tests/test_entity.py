import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.sprite import Sprite
from game_logic.entities import Entity, ItemEntity
from game_logic.game_object import GameObject


def test_entity_creation_and_inheritance(basic_sprite: Sprite):
    """
    Tests that a fixture creating an Entity (via its subclass Sprite)
    is created correctly and follows the expected inheritance chain.
    """
    # Test that the fixture is a subclass of both Entity and Sprite
    assert isinstance(basic_sprite, Entity)
    assert isinstance(basic_sprite, Sprite)

    # Test that the base template is a GameObject
    assert isinstance(basic_sprite.base, GameObject)


def test_entity_attributes(basic_sprite: Sprite):
    """
    Tests that the attributes of a created Entity have the correct
    values and types.
    """
    # Test the VALUE of an attribute
    assert basic_sprite.base.name == "Hero"
    assert basic_sprite.x == 5

    assert isinstance(basic_sprite.base.name, str)
    assert isinstance(basic_sprite.x, int)

    assert basic_sprite.base.name == "Hero"
    assert basic_sprite.custom_name is None
