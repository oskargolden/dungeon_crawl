from dataclasses import dataclass
from game_logic.sprite import Sprite


@dataclass
class NPCActor(Sprite):
    """
    Represents a Non-Player Character in the game.

    This is the base class for all computer-controlled actors, such as
    monsters, shopkeepers, or quest givers. It inherits all the properties
    of a Sprite (like health, stats, and an inventory).
    """
    # You could add attributes common to all NPCs here later,
    # for example, a 'dialogue_tree' or 'faction' attribute.
    pass
