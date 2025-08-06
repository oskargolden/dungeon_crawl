from dataclasses import dataclass, field
from typing import List

# Import your core classes
from game_logic.maps.layered_map import LayeredMap
from game_logic.sprite import Sprite
from game_logic.monster import Monster


@dataclass
class GameState:
    """Manages all the data for the current state of the game.

    This class acts as a central container for the game map, the player,
    a list of all NPCs on the map, and other global game information like
    the turn count or whether the player is currently in combat.

    Attributes:
        current_map (LayeredMap): The LayeredMap object for the current level.
        player (Sprite): The player's Sprite instance.
        monsters (List[Monster]): A list of all monster instances on the map.
        is_in_combat (bool): A flag to track if combat is active.
        turn_count (int): The current turn number.
    """
    current_map: LayeredMap
    player: Sprite
    monsters: List[Monster] = field(default_factory=list)
    is_in_combat: bool = False
    turn_count: int = 0
