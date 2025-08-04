import pytest
from dungeon_crawl.game_logic.sprite import Sprite
from dungeon_crawl.config.items import ITEMS


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
    assert len(sprite_obj.inventory) == len(ITEMS)
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

    # Test that non-default fields are None
    assert sprite_obj.x is None
    assert sprite_obj.y is None
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
        x=50,
        y=100,
        health=500,
        speed=10,
        xp=150,
        lvl=3
    )
    sprite_obj.inventory['gold_coin'] = 50
    sprite_obj.inventory['healing_potion'] = 1
    sprite_obj.wearing['chest'] = 'leather_vest'
    sprite_obj.stats['strength'] = 12

    # Dynamically build the expected inventory based on the ITEMS list.
    # This is the key change that makes the test more maintainable.
    expected_inventory = {item.name: 0 for item in ITEMS}
    expected_inventory['gold_coin'] = 50
    expected_inventory['healing_potion'] = 1

    expected_dict = {
        "xp": 150,
        "lvl": 3,
        "inventory": expected_inventory,
        "wearing": {
            'head': None, 'chest': 'leather_vest', 'arms': None, 'wrists': None,
            'hands': None, 'legs': None, 'feet': None, 'neck': None,
            'finger_left': None, 'finger_right': None, 'waist': None,
            'shoulders': None, 'back': None,
        },
        "stats": {
            'strength': 12, 'dexterity': 0, 'constitution': 0,
            'intelligence': 0, 'wisdom': 0, 'charisma': 0
        },
        "skills": {
            'acrobatics': 0, 'athletics': 0, 'deception': 0,
            'insight': 0, 'intimidation': 0, 'investigation': 0,
            'perception': 0, 'persuasion': 0, 'stealth': 0,
            'survival': 0,
        },
        "x": 50,
        "y": 100,
        "health": 500,
        "speed": 10,
    }

    # Call the method to get the dict from class instance
    sprite_dict = sprite_obj.to_dict()

    # Assert that the output dictionary matches the expected dictionary
    assert sprite_dict == expected_dict
