# `config/monster_catalogue.py`
"""A catalogue of all monster templates in the game."""

from config.templates import MonsterTemplate, MonsterBehavior
from config.templates import MonsterType, SpecialAbility

# -----------------------------------------------------------
# The Monster Catalog
# -----------------------------------------------------------

# --- Humanoids ---
GOBLIN = MonsterTemplate(
    name="Goblin", symbol="g", description="A small, cruel green-skinned humanoid.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.HOSTILE,
    base_health=10, base_attack=4, base_defense=2,
    base_stats={'strength': 8, 'dexterity': 16},
    loot_table=["Dagger", "Copper Coins"]
)
HOBGOBLIN = MonsterTemplate(
    name="Hobgoblin", symbol="h", description="A larger, more disciplined cousin of the goblin.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.HOSTILE,
    base_health=20, base_attack=7, base_defense=5,
    base_stats={'strength': 14, 'dexterity': 12},
    loot_table=["Short sword", "Leather Armor"]
)
ORC = MonsterTemplate(
    name="Orc", symbol="o", description="A brutish, pig-faced humanoid built for war.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.HOSTILE,
    base_health=25, base_attack=8, base_defense=6,
    base_stats={'strength': 16, 'dexterity': 10},
    loot_table=["Battle axe", "Tattered Hide"]
)
KOBOLD = MonsterTemplate(
    name="Kobold", symbol="k", description="A small, reptilian humanoid that yaps and scurries.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.HOSTILE,
    base_health=8, base_attack=3, base_defense=2,
    base_stats={'strength': 6, 'dexterity': 15},
    loot_table=["Sling stones", "A shiny rock"]
)
LIZARDFOLK = MonsterTemplate(
    name="Lizardfolk", symbol="l", description="A territorial, reptilian humanoid armed with a crude spear.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.NEUTRAL,
    base_health=30, base_attack=7, base_defense=5,
    base_stats={'strength': 15, 'dexterity': 10},
    loot_table=["Spear", "Animal Hide"]
)
GNOLL = MonsterTemplate(
    name="Gnoll", symbol="G", description="A savage, hyena-headed humanoid that giggles with malice.",
    monster_type=MonsterType.HUMANOID, behavior=MonsterBehavior.HOSTILE,
    base_health=35, base_attack=9, base_defense=4,
    base_stats={'strength': 16, 'dexterity': 12},
    loot_table=["Spear", "Cracked Bones"]
)

# --- Undead ---
SKELETON = MonsterTemplate(
    name="Skeleton", symbol="s", description="A reanimated skeleton, rattling as it moves.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=15, base_attack=5, base_defense=3,
    base_stats={'strength': 12, 'dexterity': 14},
    loot_table=["Rusty Sword", "Bone Fragments"]
)
ZOMBIE = MonsterTemplate(
    name="Zombie", symbol="z", description="A slow, shambling corpse that groans with hunger.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=22, base_attack=6, base_defense=2,
    base_stats={'strength': 14, 'dexterity': 6},
    loot_table=["Tattered Clothes"]
)
GHOUL = MonsterTemplate(
    name="Ghoul", symbol="u", description="A twisted, corpse-eating undead with paralyzing claws.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=30, base_attack=8, base_defense=4,
    base_stats={'strength': 13, 'dexterity': 15},
    loot_table=["Grave dirt", "Tarnished Ring"],
    special_abilities=[SpecialAbility.PARALYZE]
)
WIGHT = MonsterTemplate(
    name="Wight", symbol="W", description="An intelligent, malevolent undead that drains life with its touch.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=45, base_attack=10, base_defense=6,
    base_stats={'strength': 15, 'dexterity': 14},
    loot_table=["Ancient Coin", "Blackened Amulet"],
    special_abilities=[SpecialAbility.LIFE_DRAIN]
)
GHOST = MonsterTemplate(
    name="Ghost", symbol="H", description="A sorrowful, incorporeal spirit.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.NEUTRAL,
    base_health=40, base_attack=9, base_defense=8,
    base_stats={'strength': 1, 'dexterity': 16},
    loot_table=[]
)
VAMPIRE_SPAWN = MonsterTemplate(
    name="Vampire Spawn", symbol="V", description="A lesser vampire, bound to the will of its master.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=60, base_attack=12, base_defense=7,
    base_stats={'strength': 16, 'dexterity': 16},
    loot_table=["Fine Clothes", "Ornate Dagger"],
    special_abilities=[SpecialAbility.LIFE_DRAIN]
)
MUMMY = MonsterTemplate(
    name="Mummy", symbol="M", description="A preserved corpse animated by dark magic, trailing wrappings.",
    monster_type=MonsterType.UNDEAD, behavior=MonsterBehavior.HOSTILE,
    base_health=75, base_attack=14, base_defense=8,
    base_stats={'strength': 17, 'dexterity': 8},
    loot_table=["Funerary Mask", "Ancient Scroll"]
)

# --- Beasts & Monstrosities ---
GIANT_RAT = MonsterTemplate(
    name="Giant Rat", symbol="r", description="An unusually large and aggressive rodent.",
    monster_type=MonsterType.BEAST, behavior=MonsterBehavior.HOSTILE,
    base_health=7, base_attack=3, base_defense=1,
    base_stats={'strength': 7, 'dexterity': 15},
    loot_table=["Rat Pelt"]
)
GIANT_SPIDER = MonsterTemplate(
    name="Giant Spider", symbol="S", description="A monstrous arachnid that spins thick webs.",
    monster_type=MonsterType.BEAST, behavior=MonsterBehavior.HOSTILE,
    base_health=26, base_attack=7, base_defense=4,
    base_stats={'strength': 14, 'dexterity': 16},
    loot_table=["Spider Silk", "Poison Gland"]
)
WOLF = MonsterTemplate(
    name="Wolf", symbol="w", description="A cunning predator that often hunts in packs.",
    monster_type=MonsterType.BEAST, behavior=MonsterBehavior.NEUTRAL,
    base_health=18, base_attack=6, base_defense=3,
    base_stats={'strength': 12, 'dexterity': 15},
    loot_table=["Wolf Pelt"]
)
DIRE_WOLF = MonsterTemplate(
    name="Dire Wolf", symbol="W", description="An enormous, primeval wolf with a savage bite.",
    monster_type=MonsterType.BEAST, behavior=MonsterBehavior.HOSTILE,
    base_health=40, base_attack=10, base_defense=4,
    base_stats={'strength': 17, 'dexterity': 15},
    loot_table=["Dire Wolf Pelt", "Large Fang"]
)
GELATINOUS_CUBE = MonsterTemplate(
    name="Gelatinous Cube", symbol="C", description="A transparent, ten-foot cube of acid that silently scours dungeon halls.",
    monster_type=MonsterType.OOZE, behavior=MonsterBehavior.HOSTILE,
    base_health=80, base_attack=10, base_defense=1,
    base_stats={'strength': 14, 'dexterity': 3},
    loot_table=["Engulfed Item", "Corroded Coin"]
)
OWLBEAR = MonsterTemplate(
    name="Owlbear", symbol="O", description="A ferocious predator with the body of a bear and the head of an owl.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.HOSTILE,
    base_health=60, base_attack=14, base_defense=6,
    base_stats={'strength': 20, 'dexterity': 12},
    loot_table=["Owlbear Claw", "Feathers"]
)
BASILISK = MonsterTemplate(
    name="Basilisk", symbol="B", description="A magical reptile whose gaze can turn flesh to stone.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.HOSTILE,
    base_health=55, base_attack=11, base_defense=7,
    base_stats={'strength': 16, 'dexterity': 8},
    loot_table=["Basilisk Eye"],
    special_abilities=[SpecialAbility.PETRIFY]
)
HARPY = MonsterTemplate(
    name="Harpy", symbol="Y", description="A winged creature with the body of a vulture and the head of a woman.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.HOSTILE,
    base_health=38, base_attack=8, base_defense=4,
    base_stats={'strength': 12, 'dexterity': 16},
    loot_table=["Shiny Trinket", "Tangled Hair"]
)
CENTAUR = MonsterTemplate(
    name="Centaur", symbol="N", description="A creature with the upper body of a human and the lower body of a horse.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.NEUTRAL,
    base_health=45, base_attack=10, base_defense=5,
    base_stats={'strength': 18, 'dexterity': 14},
    loot_table=["Long Bow", "Herbal Pouch"]
)
MINOTAUR = MonsterTemplate(
    name="Minotaur", symbol="T", description="A massive bull-headed man that navigates labyrinths with deadly skill.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.HOSTILE,
    base_health=70, base_attack=15, base_defense=7,
    base_stats={'strength': 18, 'dexterity': 11},
    loot_table=["Great Axe", "Nose Ring"]
)

# --- Oozes & Slimes ---
GREEN_SLIME = MonsterTemplate(
    name="Green Slime", symbol="~", description="A dripping, protoplasmic creature that corrodes organic matter.",
    monster_type=MonsterType.OOZE, behavior=MonsterBehavior.HOSTILE,
    base_health=20, base_attack=5, base_defense=0,
    base_stats={'strength': 1, 'dexterity': 1},
    loot_table=[]
)
GRAY_OOZE = MonsterTemplate(
    name="Gray Ooze", symbol="~", description="An ooze that resembles wet stone, corroding metal on contact.",
    monster_type=MonsterType.OOZE, behavior=MonsterBehavior.HOSTILE,
    base_health=40, base_attack=8, base_defense=2,
    base_stats={'strength': 12, 'dexterity': 6},
    loot_table=[]
)

# --- Elementals & Constructs ---
GARGOYLE = MonsterTemplate(
    name="Gargoyle", symbol="g", description="A stone predator that perches on ledges, often mistaken for a statue.",
    monster_type=MonsterType.CONSTRUCT, behavior=MonsterBehavior.GUARD,
    base_health=52, base_attack=10, base_defense=9,
    base_stats={'strength': 15, 'dexterity': 11},
    loot_table=["Stone Shard"]
)
IRON_GOLEM = MonsterTemplate(
    name="Iron Golem", symbol="I", description="A towering automaton of solid iron, animated by powerful magic.",
    monster_type=MonsterType.CONSTRUCT, behavior=MonsterBehavior.GUARD,
    base_health=200, base_attack=25, base_defense=15,
    base_stats={'strength': 24, 'dexterity': 9},
    loot_table=["Heartstone"]
)
WATER_ELEMENTAL = MonsterTemplate(
    name="Water Elemental", symbol="E", description="A swirling vortex of living water.",
    monster_type=MonsterType.ELEMENTAL, behavior=MonsterBehavior.HOSTILE,
    base_health=90, base_attack=14, base_defense=8,
    base_stats={'strength': 18, 'dexterity': 14},
    loot_table=["Pure Water"]
)
FIRE_ELEMENTAL = MonsterTemplate(
    name="Fire Elemental", symbol="F", description="A being of pure flame that dances and burns.",
    monster_type=MonsterType.ELEMENTAL, behavior=MonsterBehavior.HOSTILE,
    base_health=85, base_attack=16, base_defense=6,
    base_stats={'strength': 10, 'dexterity': 17},
    loot_table=["Cinder"]
)

# --- Giants & Dragons ---
HILL_GIANT = MonsterTemplate(
    name="Hill Giant", symbol="H", description="A dim-witted, brutish giant who loves to smash things.",
    monster_type=MonsterType.GIANT, behavior=MonsterBehavior.HOSTILE,
    base_health=100, base_attack=18, base_defense=8,
    base_stats={'strength': 21, 'dexterity': 8},
    loot_table=["Greatclub", "Boulders", "Sack of Junk"]
)
ETTIN = MonsterTemplate(
    name="Ettin", symbol="T", description="A two-headed giant, each head with its own brutish personality.",
    monster_type=MonsterType.GIANT, behavior=MonsterBehavior.HOSTILE,
    base_health=90, base_attack=16, base_defense=7,
    base_stats={'strength': 21, 'dexterity': 8},
    loot_table=["Morningstar", "Javelin"]
)
WYVERN = MonsterTemplate(
    name="Wyvern", symbol="v", description="A lesser, two-legged cousin of the dragon with a venomous stinger.",
    monster_type=MonsterType.DRAGON, behavior=MonsterBehavior.HOSTILE,
    base_health=110, base_attack=16, base_defense=9,
    base_stats={'strength': 19, 'dexterity': 10},
    loot_table=["Wyvern Stinger", "Large Scales"]
)
YOUNG_RED_DRAGON = MonsterTemplate(
    name="Young Red Dragon", symbol="D", description="A vain and terrible red dragon, breathing gouts of flame.",
    monster_type=MonsterType.DRAGON, behavior=MonsterBehavior.HOSTILE,
    base_health=180, base_attack=22, base_defense=12,
    base_stats={'strength': 23, 'dexterity': 10},
    loot_table=["Dragon Scale", "Piles of Gold", "Magic Item"]
)

# --- Aberrations ---
MIMIC = MonsterTemplate(
    name="Mimic", symbol="C", description="A monstrous predator that perfectly imitates inanimate objects.",
    monster_type=MonsterType.ABERRATION, behavior=MonsterBehavior.HOSTILE,
    base_health=60, base_attack=10, base_defense=6,
    base_stats={'strength': 17, 'dexterity': 12},
    loot_table=["Adhesive Goop", "Random Item"]
)
RUST_MONSTER = MonsterTemplate(
    name="Rust Monster", symbol="m", description="A bizarre creature with feathery antennae that corrodes ferrous metals.",
    monster_type=MonsterType.ABERRATION, behavior=MonsterBehavior.NEUTRAL,
    base_health=27, base_attack=5, base_defense=5,
    base_stats={'strength': 13, 'dexterity': 12},
    loot_table=[]
)
CARRION_CRAWLER = MonsterTemplate(
    name="Carrion Crawler", symbol="c", description="A massive, multi-legged scavenger whose tentacles paralyze its prey.",
    monster_type=MonsterType.ABERRATION, behavior=MonsterBehavior.HOSTILE,
    base_health=51, base_attack=8, base_defense=6,
    base_stats={'strength': 14, 'dexterity': 13},
    loot_table=[],
    special_abilities=[SpecialAbility.PARALYZE]
)
DISPLACER_BEAST = MonsterTemplate(
    name="Displacer Beast", symbol="d", description="A sleek, six-legged panther-like creature that projects an illusion of itself.",
    monster_type=MonsterType.MONSTROSITY, behavior=MonsterBehavior.HOSTILE,
    base_health=85, base_attack=14, base_defense=10,
    base_stats={'strength': 18, 'dexterity': 15},
    loot_table=["Displacer Hide"]
)
BEHOLDER = MonsterTemplate(
    name="Beholder", symbol="X", description="A floating orb of flesh with a large central eye and ten smaller eyestalks.",
    monster_type=MonsterType.ABERRATION, behavior=MonsterBehavior.HOSTILE,
    base_health=180, base_attack=10, base_defense=12,
    base_stats={'strength': 10, 'dexterity': 14},
    loot_table=["Beholder Eyestalk"]
)
MIND_FLAYER = MonsterTemplate(
    name="Mind Flayer", symbol="f", description="A horrific, squid-headed humanoid with terrifying mental powers.",
    monster_type=MonsterType.ABERRATION, behavior=MonsterBehavior.HOSTILE,
    base_health=70, base_attack=12, base_defense=8,
    base_stats={'strength': 11, 'dexterity': 12},
    loot_table=["Mind Flayer Tentacle"]
)

# -----------------------------------------------------------
# 3. Master Dictionary for Easy Lookup
# -----------------------------------------------------------
MONSTERS = {
    "Goblin": GOBLIN, "Hobgoblin": HOBGOBLIN, "Orc": ORC, "Kobold": KOBOLD,
    "Lizardfolk": LIZARDFOLK, "Gnoll": GNOLL, "Skeleton": SKELETON, "Zombie": ZOMBIE,
    "Ghoul": GHOUL, "Wight": WIGHT, "Ghost": GHOST, "Vampire Spawn": VAMPIRE_SPAWN,
    "Mummy": MUMMY, "Giant Rat": GIANT_RAT, "Giant Spider": GIANT_SPIDER, "Wolf": WOLF,
    "Dire Wolf": DIRE_WOLF, "Gelatinous Cube": GELATINOUS_CUBE, "Owlbear": OWLBEAR,
    "Basilisk": BASILISK, "Harpy": HARPY, "Centaur": CENTAUR, "Minotaur": MINOTAUR,
    "Green Slime": GREEN_SLIME, "Gray Ooze": GRAY_OOZE, "Gargoyle": GARGOYLE,
    "Iron Golem": IRON_GOLEM, "Water Elemental": WATER_ELEMENTAL, "Fire Elemental": FIRE_ELEMENTAL,
    "Hill Giant": HILL_GIANT, "Ettin": ETTIN, "Wyvern": WYVERN, "Young Red Dragon": YOUNG_RED_DRAGON,
    "Mimic": MIMIC, "Rust Monster": RUST_MONSTER, "Carrion Crawler": CARRION_CRAWLER,
    "Displacer Beast": DISPLACER_BEAST, "Beholder": BEHOLDER, "Mind Flayer": MIND_FLAYER
}
