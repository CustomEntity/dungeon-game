import subprocess
import sys

import pykson
from dungeon_game import Game
from game.actions.action import Action
from game.chapter import Chapter
from game.story import Story




if __name__ == '__main__':

    try:
        import pygame as pg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])

    print("Starting the game..")
    game = Game()
    game.start()

