from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True, slots=True)
class Range:
    """A dataclass for storing short, medium, and long weapon ranges."""
    short: str
    medium: str
    long: str


@dataclass(frozen=True, slots=True)
class Weapon:
    """A dataclass representing a single OSE weapon."""
    name: str
    cost: int
    weight: int  # Stored in coins
    damage: str
    qualities: List[str] = field(default_factory=list)
    missile_range: Optional[Range] = None


@dataclass(frozen=True, slots=True)
class Armor:
    """A dataclass representing a single OSE armor item."""
    name: str
    ac: str
    cost: int
    weight: int


@dataclass(frozen=True, slots=True)
class Ammunition:
    """A dataclass for ammunition."""
    name: str
    cost: int
    quantity: int


@dataclass(frozen=True, slots=True)
class Item:
    """A general dataclass for adventuring gear and miscellaneous items."""
    name: str
    cost: int
    weight: int = 0


# --- DATA LISTS ---
WEAPONS = [
    Weapon(name='Battle axe', cost=7, weight=50, damage='1d8',
           qualities=['Melee', 'Slow', 'Two-handed']),
    Weapon(name='Club', cost=3, weight=50, damage='1d4',
           qualities=['Blunt', 'Melee']),
    Weapon(name='Crossbow', cost=30, weight=50, damage='1d6',
           qualities=['Reload', 'Slow', 'Two-handed'],
           missile_range=Range(short='5’–80’', medium='81’–160’', long='161’–240’')),
    Weapon(name='Dagger', cost=3, weight=10, damage='1d4',
           qualities=['Melee'],
           missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’')),
    Weapon(name='Hand axe', cost=4, weight=30, damage='1d6',
           qualities=['Melee'],
           missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’')),
    Weapon(name='Holy water (vial)', cost=25, weight=0, damage='1d8',
           qualities=['Splash weapon'],
           missile_range=Range(short='5’–10’', medium='11’–30’', long='31’–50’')),
    Weapon(name='Javelin', cost=1, weight=20, damage='1d4',
           qualities=[],
           missile_range=Range(short='5’–30’', medium='31’–60’', long='61’–90’')),
    Weapon(name='Lance', cost=5, weight=120, damage='1d6',
           qualities=['Charge', 'Melee']),
    Weapon(name='Long bow', cost=40, weight=30, damage='1d6',
           qualities=['Two-handed'],
           missile_range=Range(short='5’–70’', medium='71’–140’', long='141’–210’')),
    Weapon(name='Mace', cost=5, weight=30, damage='1d6',
           qualities=['Blunt', 'Melee']),
    Weapon(name='Oil (flask), burning', cost=2, weight=0, damage='1d8',
           qualities=['Splash weapon'],
           missile_range=Range(short='5’–10’', medium='11’–30’', long='31’–50’')),
    Weapon(name='Pole arm', cost=7, weight=150, damage='1d10',
           qualities=['Brace', 'Melee', 'Slow', 'Two-handed']),
    Weapon(name='Short bow', cost=25, weight=30, damage='1d6',
           qualities=['Two-handed'],
           missile_range=Range(short='5’–50’', medium='51’–100’', long='101’–150’')),
    Weapon(name='Short sword', cost=7, weight=30, damage='1d6',
           qualities=['Melee']),
    Weapon(name='Silver dagger', cost=30, weight=10, damage='1d4',
           qualities=['Melee'],
           missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’')),
    Weapon(name='Sling', cost=2, weight=20, damage='1d4',
           qualities=['Blunt'],
           missile_range=Range(short='5’–40’', medium='41’–80’', long='81’–160’')),
    Weapon(name='Spear', cost=3, weight=30, damage='1d6',
           qualities=['Brace', 'Melee'],
           missile_range=Range(short='5’–20’', medium='21’–40’', long='41’–60’')),
    Weapon(name='Staff', cost=2, weight=40, damage='1d4',
           qualities=['Blunt', 'Melee', 'Slow', 'Two-handed']),
    Weapon(name='Sword', cost=10, weight=60, damage='1d8',
           qualities=['Melee']),
    Weapon(name='Torch', cost=1, weight=0, damage='1d4',
           qualities=['Melee']),
    Weapon(name='Two-handed sword', cost=15, weight=150, damage='1d10',
           qualities=['Melee', 'Slow', 'Two-handed']),
    Weapon(name='War hammer', cost=5, weight=30, damage='1d6',
           qualities=['Blunt', 'Melee']),
]

ARMOR = [
    Armor(name='Leather', ac='7 [12]', cost=20, weight=200),
    Armor(name='Chainmail', ac='5 [14]', cost=40, weight=400),
    Armor(name='Plate mail', ac='3 [16]', cost=60, weight=500),
    Armor(name='Shield', ac='+1 bonus', cost=10, weight=100),
]

AMMUNITION = [
    Ammunition(name='Arrows', cost=5, quantity=20),
    Ammunition(name='Crossbow bolts', cost=10, quantity=30),
    Ammunition(name='Silver tipped arrow', cost=5, quantity=1),
    Ammunition(name='Sling stones', cost=0, quantity=0),
]

ADVENTURING_GEAR = [
    Item(name='Backpack', cost=5, weight=0),
    Item(name='Crowbar', cost=10, weight=0),
    Item(name='Garlic', cost=5, weight=0),
    Item(name='Grappling hook', cost=25, weight=0),
    Item(name='Hammer (small)', cost=2, weight=0),
    Item(name='Holy symbol', cost=25, weight=0),
    Item(name='Holy water (vial)', cost=25, weight=0),
    Item(name='Iron spikes (12)', cost=1, weight=0),
    Item(name='Lantern', cost=10, weight=0),
    Item(name='Mirror (hand-sized, steel)', cost=5, weight=0),
    Item(name='Oil (1 flask)', cost=2, weight=0),
    Item(name='Pole (10’ long, wooden)', cost=1, weight=0),
    Item(name='Rations (iron, 7 days)', cost=15, weight=0),
    Item(name='Rations (standard, 7 days)', cost=5, weight=0),
    Item(name='Rope (50’)', cost=1, weight=0),
    Item(name='Sack (large)', cost=2, weight=0),
    Item(name='Sack (small)', cost=1, weight=0),
    Item(name='Stakes (3) and mallet', cost=3, weight=0),
    Item(name='Thieves’ tools', cost=25, weight=0),
    Item(name='Tinder box (flint & steel)', cost=3, weight=0),
    Item(name='Torches (6)', cost=1, weight=0),
    Item(name='Waterskin', cost=1, weight=0),
    Item(name='Wine (2 pints)', cost=1, weight=0),
    Item(name='Wolfsbane (1 bunch)', cost=10, weight=0),
]

# A consolidated list of all items for easy lookup
ITEMS = WEAPONS + ARMOR + AMMUNITION + ADVENTURING_GEAR


def find_item(name: str) -> Weapon | Armor | Ammunition | Item | None:
    """Finds an item by its name, searching all item types."""
    for item in ITEMS:
        if item.name.lower() == name.lower():
            return item
    return None
