import sys
import os
import random
from game_logic.sprite import Sprite


def main():
    sprite_obj = Sprite()
    sprite_dict = sprite_obj.to_dict()
    print(sprite_dict)


if __name__ == "__main__":
    main()
