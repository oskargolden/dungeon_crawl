
from dataclasses import dataclass
from config.monster import Monster # type: ignore


@dataclass
class Skeleton(Monster):
    """Represents a skeleton monster in the game world, inheriting from Monster."""
    
    # Additional attributes specific to skeletons can be added here
    bone_count: int = 206
    