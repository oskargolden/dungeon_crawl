from dataclasses import dataclass, asdict, field
from game_logic.NPC_actor import NPCActor



@dataclass
class Monster(NPCActor):
    """Represents a monster in the game world, inheriting from NPCActor."""
    
    # Additional attributes specific to monsters can be added here
    attack_power: int = 1
    defense: int = 1
    loot: str = "None"

