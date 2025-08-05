import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.sprite import Sprite
from game_logic.entities import ItemEntity


def test_sprite_creation_from_fixture(basic_sprite: Sprite):
    """Tests if the basic_sprite fixture is created correctly."""
    assert basic_sprite.base.name == "Hero"
    assert basic_sprite.health == 100
    assert basic_sprite.x == 5
    assert isinstance(basic_sprite.inventory, list)
    assert len(basic_sprite.inventory) == 0


def test_add_item_to_inventory(basic_sprite: Sprite, sword_template):
    """Tests adding an item to the sprite's inventory."""
    assert len(basic_sprite.inventory) == 0

    # Create a unique instance of the sword to add
    sword_instance = ItemEntity(base=sword_template)

    # Add the item
    basic_sprite.inventory.append(sword_instance)

    # The inventory should now have one item
    assert len(basic_sprite.inventory) == 1
    assert basic_sprite.inventory[0].base.name == "Sword"
