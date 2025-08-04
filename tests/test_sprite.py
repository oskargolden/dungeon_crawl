import sys
import os
import pytest

# Add the parent directory to the path so we can import from project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_logic.sprite import Sprite
from config.items import ITEMS


def test_sprite_default_values():
    """
    This test confirms that a new Sprite object is correctly initialized
    with the expected default values for its attributes.
    """
    sprite_obj = Sprite()

    # Test that mutable fields are initialized correctly with new instances
    assert sprite_obj.xp == 0
    assert sprite_obj.lvl == 0
    assert isinstance(sprite_obj.inventory, dict)
    # Use the actual inventory length (should be 54 now that duplicates are fixed)
    assert len(sprite_obj.inventory) == len(set(item.name for item in ITEMS))
    for item in ITEMS:
        assert item.name in sprite_obj.inventory
        assert sprite_obj.inventory[item.name] == 0

    assert isinstance(sprite_obj.wearing, dict)
    assert 'head' in sprite_obj.wearing and sprite_obj.wearing['head'] is None
    assert 'chest' in sprite_obj.wearing and sprite_obj.wearing['chest'] is None

    assert isinstance(sprite_obj.stats, dict)
    assert 'strength' in sprite_obj.stats and sprite_obj.stats['strength'] == 0
    assert 'dexterity' in sprite_obj.stats and sprite_obj.stats['dexterity'] == 0

    assert isinstance(sprite_obj.skills, dict)
    assert 'acrobatics' in sprite_obj.skills and sprite_obj.skills['acrobatics'] == 0
    assert 'stealth' in sprite_obj.skills and sprite_obj.skills['stealth'] == 0
    # Test the additional fields
    assert sprite_obj.x is None
    assert sprite_obj.y is None
    assert sprite_obj.z is None
    assert sprite_obj.health is None
    assert sprite_obj.speed is None


def test_sprite_to_dict_method():
    """
    This test confirms that the to_dict method correctly converts a Sprite
    object to a dictionary. It also tests if setting non-default values
    works as expected.
    """
    # Create an instance with some custom values
    sprite_obj = Sprite(
        xp=150,
        lvl=3
    )
    # Use actual items from your ITEMS list instead of fake ones
    # Let's modify some real items from your inventory
    sprite_obj.inventory['Sword'] = 1  # Give the sprite a sword
    sprite_obj.inventory['Chainmail'] = 1  # Give the sprite chainmail
    sprite_obj.wearing['chest'] = 'Chainmail'  # Equip the chainmail
    sprite_obj.stats['strength'] = 12

    # Get the actual sprite dict to compare against
    sprite_dict = sprite_obj.to_dict()
    # Verify the basic structure and values we set
    assert sprite_dict['xp'] == 150
    assert sprite_dict['lvl'] == 3
    assert sprite_dict['wearing']['chest'] == 'Chainmail'
    assert sprite_dict['stats']['strength'] == 12
    # Verify the additional fields exist and are None
    assert sprite_dict['x'] is None
    assert sprite_dict['y'] is None
    assert sprite_dict['z'] is None
    assert sprite_dict['health'] is None
    assert sprite_dict['speed'] is None
    # Verify inventory modifications
    assert sprite_dict['inventory']['Sword'] == 1
    assert sprite_dict['inventory']['Chainmail'] == 1
    # Verify the structure types
    assert isinstance(sprite_dict['inventory'], dict)
    assert isinstance(sprite_dict['wearing'], dict)
    assert isinstance(sprite_dict['stats'], dict)
    assert isinstance(sprite_dict['skills'], dict)
    # Verify that unmodified items remain at 0
    assert sprite_dict['inventory']['Battle axe'] == 0
    assert sprite_dict['inventory']['Club'] == 0
    # Verify that unmodified stats remain at 0
    assert sprite_dict['stats']['dexterity'] == 0
    assert sprite_dict['stats']['constitution'] == 0


def test_sprite_inventory_consistency():
    """
    Test that the inventory contains exactly the items from the ITEMS list.
    """
    sprite_obj = Sprite()
    # Get all unique item names from ITEMS
    expected_items = set(item.name for item in ITEMS)
    actual_items = set(sprite_obj.inventory.keys())
    # They should be exactly the same
    assert expected_items == actual_items
    # Should have exactly 54 items (no duplicates)
    assert len(sprite_obj.inventory) == 54
