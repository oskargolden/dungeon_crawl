from dataclasses import dataclass, asdict, field
from game_logic.actor import NPCActor



@dataclass
class Monster(NPCActor):
    """Represents a monster in the game world, inheriting from NPCActor."""
    
    # Additional attributes specific to monsters can be added here
    attack_power: int = 5
    defense: int = 2
    loot: str = "None"

