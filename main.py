from dungeon_game import Game
import subprocess
import sys

if __name__ == '__main__':

    try:
        import pygame as pg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])

    print("Starting the game..")
    game = Game()
    game.start()