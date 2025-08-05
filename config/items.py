from dataclasses import dataclass, field
from typing import List, Optional
from game_logic.game_object import GameObject


@dataclass(frozen=True, slots=True)
class Range:
    """A dataclass for storing short, medium, and long weapon ranges."""
    short: str
    medium: str
    long: str


# Each of the following classes now inherits from GameObject
@dataclass(frozen=True, slots=True)
class Weapon(GameObject):
    """A dataclass representing a single weapon."""
    cost: int
    weight: int
    damage: str
    qualities: List[str] = field(default_factory=list)
    missile_range: Optional[Range] = None


@dataclass(frozen=True, slots=True)
class Armor(GameObject):
    """A dataclass representing a single armor item."""
    ac: str
    cost: int
    weight: int


@dataclass(frozen=True, slots=True)
class Ammunition(GameObject):
    """A dataclass for ammunition."""
    cost: int
    quantity: int


@dataclass(frozen=True, slots=True)
class Item(GameObject):
    """A general dataclass for adventuring gear and miscellaneous items."""
    cost: int
    weight: int = 0


# --- DATA LISTS ---
WEAPONS: List[Weapon] = [
    Weapon(
        name='Battle axe',
        symbol='P',
        description='A heavy axe that requires two hands.',
        cost=7,
        weight=50,
        damage='1d8',
        qualities=['Melee', 'Slow', 'Two-handed'],
    ),
    Weapon(
        name='Club',
        symbol='!',
        description='A simple, heavy piece of wood.',
        cost=3,
        weight=50,
        damage='1d4',
        qualities=['Blunt', 'Melee'],
    ),
    Weapon(
        name='Crossbow',
        symbol='}',
        description='A powerful ranged weapon that requires reloading.',
        cost=30,
        weight=50,
        damage='1d6',
        qualities=['Reload', 'Slow', 'Two-handed'],
        missile_range=Range(short='5’–80’', medium='81’–160’', long='161’–240’'),
    ),
    Weapon(
        name='Dagger',
        symbol='†',
        description='A small knife, easily concealed.',
        cost=3,
        weight=10,
        damage='1d4',
        qualities=['Melee'],
        missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’'),
    ),
    Weapon(
        name='Hand axe',
        symbol='p',
        description='A small, one-handed axe that can be thrown.',
        cost=4,
        weight=30,
        damage='1d6',
        qualities=['Melee'],
        missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’'),
    ),
    Weapon(
        name='Holy water (thrown)',
        symbol='i',
        description='Water blessed by a cleric, harmful to undead.',
        cost=25,
        weight=0,
        damage='1d8',
        qualities=['Splash weapon'],
        missile_range=Range(short='5’–10’', medium='11’–30’', long='31’–50’'),
    ),
    Weapon(
        name='Javelin',
        symbol='/',
        description='A light spear designed for throwing.',
        cost=1,
        weight=20,
        damage='1d4',
        qualities=[],
        missile_range=Range(short='5’–30’', medium='31’–60’', long='61’–90’'),
    ),
    Weapon(
        name='Lance',
        symbol='>',
        description='A long spear used from horseback.',
        cost=5,
        weight=120,
        damage='1d6',
        qualities=['Charge', 'Melee'],
    ),
    Weapon(
        name='Long bow',
        symbol=')',
        description='A tall bow that fires arrows with great force.',
        cost=40,
        weight=30,
        damage='1d6',
        qualities=['Two-handed'],
        missile_range=Range(short='5’–70’', medium='71’–140’', long='141’–210’'),
    ),
    Weapon(
        name='Mace',
        symbol='!',
        description='A blunt club with a heavy, often flanged, head.',
        cost=5,
        weight=30,
        damage='1d6',
        qualities=['Blunt', 'Melee'],
    ),
    Weapon(
        name='Oil (flask), burning',
        symbol='i',
        description='A flask of flammable oil.',
        cost=2,
        weight=0,
        damage='1d8',
        qualities=['Splash weapon'],
        missile_range=Range(short='5’–10’', medium='11’–30’', long='31’–50’'),
    ),
    Weapon(
        name='Pole arm',
        symbol='P',
        description='A long pole with a blade, such as a halberd.',
        cost=7,
        weight=150,
        damage='1d10',
        qualities=['Brace', 'Melee', 'Slow', 'Two-handed'],
    ),
    Weapon(
        name='Short bow',
        symbol=')',
        description='A small bow, suitable for use in tight quarters.',
        cost=25,
        weight=30,
        damage='1d6',
        qualities=['Two-handed'],
        missile_range=Range(short='5’–50’', medium='51’–100’', long='101’–150’'),
    ),
    Weapon(
        name='Short sword',
        symbol='/',
        description='A one-handed sword, shorter than a longsword.',
        cost=7,
        weight=30,
        damage='1d6',
        qualities=['Melee'],
    ),
    Weapon(
        name='Silver dagger',
        symbol='†',
        description='A dagger with a silver blade, effective against lycanthropes.',
        cost=30,
        weight=10,
        damage='1d4',
        qualities=['Melee'],
        missile_range=Range(short='5’–10’', medium='11’–20’', long='21’–30’'),
    ),
    Weapon(
        name='Sling',
        symbol='s',
        description='A simple leather strap for hurling stones.',
        cost=2,
        weight=20,
        damage='1d4',
        qualities=['Blunt'],
        missile_range=Range(short='5’–40’', medium='41’–80’', long='81’–160’'),
    ),
    Weapon(
        name='Spear',
        symbol='/',
        description='A pole with a pointed tip, can be braced or thrown.',
        cost=3,
        weight=30,
        damage='1d6',
        qualities=['Brace', 'Melee'],
        missile_range=Range(short='5’–20’', medium='21’–40’', long='41’–60’'),
    ),
    Weapon(
        name='Staff',
        symbol='|',
        description='A sturdy wooden staff.',
        cost=2,
        weight=40,
        damage='1d4',
        qualities=['Blunt', 'Melee', 'Slow', 'Two-handed'],
    ),
    Weapon(
        name='Sword',
        symbol='/',
        description='A standard longsword.',
        cost=10,
        weight=60,
        damage='1d8',
        qualities=['Melee'],
    ),
    Weapon(
        name='Torch',
        symbol='i',
        description='A burning torch that can be used as a makeshift weapon.',
        cost=1,
        weight=0,
        damage='1d4',
        qualities=['Melee'],
    ),
    Weapon(
        name='Two-handed sword',
        symbol='P',
        description='A massive sword that requires two hands.',
        cost=15,
        weight=150,
        damage='1d10',
        qualities=['Melee', 'Slow', 'Two-handed'],
    ),
    Weapon(
        name='War hammer',
        symbol='!',
        description='A one-handed hammer designed for combat.',
        cost=5,
        weight=30,
        damage='1d6',
        qualities=['Blunt', 'Melee'],
    ),
]

ARMOR: List[Armor] = [
    Armor(
        name='Leather',
        symbol='[',
        description='Armor made from stiff, boiled leather.',
        ac='7 [12]',
        cost=20,
        weight=200,
    ),
    Armor(
        name='Chainmail',
        symbol='[',
        description='A heavy shirt of interlocking metal rings.',
        ac='5 [14]',
        cost=40,
        weight=400,
    ),
    Armor(
        name='Plate mail',
        symbol='[',
        description='A full suit of metal plate armor.',
        ac='3 [16]',
        cost=60,
        weight=500,
    ),
    Armor(
        name='Shield',
        symbol=']',
        description='A personal shield that provides an AC bonus.',
        ac='+1 bonus',
        cost=10,
        weight=100,
    ),
]

AMMUNITION: List[Ammunition] = [
    Ammunition(
        name='Arrows',
        symbol='=',
        description='A bundle of 20 arrows for a bow.',
        cost=5,
        quantity=20,
    ),
    Ammunition(
        name='Crossbow bolts',
        symbol='-',
        description='A bundle of 30 bolts for a crossbow.',
        cost=10,
        quantity=30,
    ),
    Ammunition(
        name='Silver tipped arrow',
        symbol='=',
        description='A single arrow with a silver tip.',
        cost=5,
        quantity=1,
    ),
    Ammunition(
        name='Sling stones',
        symbol='o',
        description='A pouch of suitable stones for a sling.',
        cost=0,
        quantity=0,
    ),
]

ADVENTURING_GEAR: List[Item] = [
    Item(
        name='Backpack',
        symbol='"',
        description='A leather pack for carrying items.',
        cost=5,
        weight=0,
    ),
    Item(
        name='Crowbar',
        symbol='T',
        description='A heavy iron bar for prying.',
        cost=10,
        weight=0,
    ),
    Item(
        name='Garlic',
        symbol='%',
        description='A pungent herb, said to ward off vampires.',
        cost=5,
        weight=0,
    ),
    Item(
        name='Grappling hook',
        symbol='&',
        description='A hook on a rope, for climbing.',
        cost=25,
        weight=0,
    ),
    Item(
        name='Hammer (small)',
        symbol='t',
        description='A small hammer for nails and spikes.',
        cost=2,
        weight=0,
    ),
    Item(
        name='Holy symbol',
        symbol='+',
        description='A divine focus for a cleric.',
        cost=25,
        weight=0,
    ),
    Item(
        name='Holy water (vial)',
        symbol='i',
        description='A vial of blessed water.',
        cost=25,
        weight=0,
    ),
    Item(
        name='Iron spikes (12)',
        symbol=':',
        description='A dozen iron spikes.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Lantern',
        symbol='L',
        description='A lantern to light the dark.',
        cost=10,
        weight=0,
    ),
    Item(
        name='Mirror (hand-sized, steel)',
        symbol='o',
        description='A small steel mirror.',
        cost=5,
        weight=0,
    ),
    Item(
        name='Oil (1 flask)',
        symbol='i',
        description='A flask of oil for a lantern.',
        cost=2,
        weight=0,
    ),
    Item(
        name='Pole (10’ long, wooden)',
        symbol='_',
        description='A 10-foot wooden pole.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Rations (iron, 7 days)',
        symbol='=',
        description='A week of dry, long-lasting rations.',
        cost=15,
        weight=0,
    ),
    Item(
        name='Rations (standard, 7 days)',
        symbol='=',
        description='A week of standard traveling rations.',
        cost=5,
        weight=0,
    ),
    Item(
        name='Rope (50’)',
        symbol='~',
        description='A 50-foot coil of hempen rope.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Sack (large)',
        symbol='"',
        description='A large burlap sack.',
        cost=2,
        weight=0,
    ),
    Item(
        name='Sack (small)',
        symbol='"',
        description='A small burlap sack.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Stakes (3) and mallet',
        symbol='T',
        description='Three wooden stakes and a mallet.',
        cost=3,
        weight=0,
    ),
    Item(
        name='Thieves’ tools',
        symbol='&',
        description='A set of lockpicks and other tools.',
        cost=25,
        weight=0,
    ),
    Item(
        name='Tinder box (flint & steel)',
        symbol='*',
        description='Used to start a fire.',
        cost=3,
        weight=0,
    ),
    Item(
        name='Torches (6)',
        symbol='i',
        description='A bundle of six torches.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Waterskin',
        symbol='b',
        description='A skin for carrying water.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Wine (2 pints)',
        symbol='b',
        description='A skin of cheap wine.',
        cost=1,
        weight=0,
    ),
    Item(
        name='Wolfsbane (1 bunch)',
        symbol='%',
        description='A bundle of wolfsbane flowers.',
        cost=10,
        weight=0,
    ),
]

# This consolidated list works as before.
ITEMS = WEAPONS + ARMOR + AMMUNITION + ADVENTURING_GEAR


def find_item(name: str) -> Optional[GameObject]:
    """Finds an item by its name, searching all item types."""
    for item in ITEMS:
        if item.name.lower() == name.lower():
            return item
    return None
