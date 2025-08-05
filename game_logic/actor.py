# In a new file, e.g., game_logic/actor.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from game_logic.sprite import Sprite  # Import the new base class


@dataclass
class NPCActor(Sprite):
    """
    Represents any creature or character that can act, have stats,
    and carry an inventory. Inherits from GameObject.
    """
    

    

   

    
