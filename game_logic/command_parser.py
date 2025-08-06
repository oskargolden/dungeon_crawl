"""
This module is responsible for parsing raw player input into structured commands
that the game engine can understand and act upon.
"""
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class Command:
    """Represents a parsed player command.

    Attributes:
        verb (str): The primary action word (e.g., 'move', 'get', 'attack').
        noun (Optional[str]): The target of the action (e.g., 'north', 'sword').
    """
    verb: str
    noun: Optional[str] = None


class CommandParser:
    """Parses raw string input from the player into Command objects."""

    def __init__(self):
        # A dictionary to map synonyms (aliases) to a standard verb.
        self.synonyms: Dict[str, str] = {
            "n": "move", "north": "move", "s": "move", "south": "move",
            "e": "move", "east": "move", "w": "move", "west": "move",
            "go": "move",
            "get": "take", "pickup": "take",
            "look": "examine", "l": "examine",
            "inv": "inventory", "i": "inventory",
            "quit": "exit", "q": "exit",
            "fight": "attack", "hit": "attack",
        }

    def parse(self, input_str: str) -> Optional[Command]:
        """Parses a raw string into a Command object.

        Args:
            input_str (str): The raw text input from the player.

        Returns:
            Optional[Command]: A Command object if the input is valid,
                otherwise None.
        """
        words = input_str.lower().strip().split()
        if not words:
            return None

        # Find the verb, converting synonyms to their base command
        verb = words[0]
        if verb in self.synonyms:
            verb = self.synonyms[verb]

        # The noun is everything else joined together
        noun = ' '.join(words[1:]) if len(words) > 1 else None

        # Special handling for movement where the direction is the verb
        if verb == "move" and noun is None:
            direction_map = {"n": "north", "s": "south", "e": "east", "w": "west"}
            original_verb = words[0]
            if original_verb in direction_map:
                noun = direction_map[original_verb]
            elif original_verb in direction_map.values():
                noun = original_verb

        return Command(verb=verb, noun=noun)
