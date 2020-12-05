from typing import List, Any, Union

import pygame
from pygame.surface import SurfaceType
from pygame.surface import Surface

from src.scene.main_menu_scene import MainMenuScene
from src.scene.scene import Scene

SCREEN_SIZE = (1280, 720)


class Game:

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()

        self.screen: Union[Surface, SurfaceType] = self.setup_displaymode()

        pygame.display.set_caption('Le Royaume de Vanedia')
        pygame.display.set_icon(pygame.image.load("../resources/images/game_icon.png"))

        self.main_menu_scene: Scene = MainMenuScene(screen=self.screen)
        self.main_menu_scene.render_scene()

        self.current_scene = self.main_menu_scene

    def start(self):
        self._game_loop()

    def show_scene(self, scene: Scene):
        self.current_scene = scene
        scene.render_scene()

    def quit(self):
        pygame.quit()

    def setup_displaymode(self):
        flags = pygame.DOUBLEBUF
        return pygame.display.set_mode(SCREEN_SIZE, flags)

    def _game_loop(self):


        try:
            while True:
                fps = int(self.clock.get_fps())
                events: List[Any] = pygame.event.get()

                pygame.display.update()
        except Exception as e:
            print("Game crashed with an unexpected error! {}".format(e))
            raise e


