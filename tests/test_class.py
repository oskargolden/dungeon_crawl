from ..sprite import Sprite


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
    assert 'gold_coin' in sprite_obj.inventory
    assert sprite_obj.inventory['gold_coin'] == 0
    assert 'healing_potion' in sprite_obj.inventory
    assert sprite_obj.inventory['healing_potion'] == 0

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

    # Define the expected dictionary for comparison
    expected_dict = {
        "xp": 150,
        "lvl": 3,
        "inventory": {
            'gold_coin': 50,
            'healing_potion': 1,
            'torch': 0,
            # ... all other inventory items with count 0
            'sword': 0, 'shield': 0, 'bow': 0, 'quiver_of_arrows': 0,
            'dagger': 0, 'mace': 0, 'spear': 0, 'light_armor': 0,
            'heavy_armor': 0, 'chain_mail': 0, 'leather_armor': 0,
            'longsword': 0, 'greatsword': 0, 'hand_axe': 0, 'battle_axe': 0,
            'mana_potion': 0, 'rations': 0, 'waterskin': 0,
            'tinderbox': 0, 'rope_50ft': 0, 'bedroll': 0,
            'scroll_of_fireball': 0, 'scroll_of_identify': 0,
            'silver_coin': 0, 'copper_coin': 0,
            'thieves_tools': 0, 'disguise_kit': 0, 'alchemists_supplies': 0,
            'herbalism_kit': 0, 'cartographers_tools': 0, 'instrument': 0,
            'backpack': 0, 'lantern': 0, 'crowbar': 0, 'caltrops': 0,
            'piton': 0, 'hammer': 0, 'mirror': 0, 'perfume': 0,
            'hourglass': 0, 'spyglass': 0,
            'ring_of_protection': 0, 'cloak_of_invisibility': 0,
            'wand_of_magic_missiles': 0, 'potion_of_flying': 0,
            'bag_of_holding': 0,
        },
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
