import subprocess
import sys

from dungeon_game import Game

if __name__ == '__main__':

    try:
        import pygame as pg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])



    print("Starting the game..")
    game = Game()
    game.start()


    # st = Story([Chapter("Chapitre 1", [Action("Discussion", "Contenu")]),
    #             Chapter("Chapitre 2", [Action("Discussion1", "Contenu1")]),
    #             Chapter("Chapitre 3", [Action("Discussion1", "Contenu1")])
    #             ])
    #
    # with open('./resources/story.json', 'w') as outfile:
    #     pykson.Pykson().to_json_file(st, outfile)
