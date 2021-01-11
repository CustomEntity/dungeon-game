import json

from dungeon_game import Game
import subprocess
import sys

from json_package.progression_manager import Progression, ProgressionEncoder, from_json

if __name__ == '__main__':

    try:
        import pygame as pg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])

    # jstr = "{\"chapter\": 1, \"action\": [0, 0]}"
    # progress = json.loads(jstr, object_hook=from_json)
    #
    # print(progress.get_current_chapter())

    Progression()

    # print("Starting the game..")
    # game = Game()
    # game.start()
