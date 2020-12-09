import sys
from typing import List, Any, Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from scene.main_menu_scene import MainMenuScene
from scene.scene import Scene

SCREEN_SIZE = (1280, 720)


class Game:

    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        pygame.init()

        self.screen: Union[Surface, SurfaceType] = self.setup_displaymode()

        pygame.display.set_caption('Le Royaume de Vanedia')
        pygame.display.set_icon(pygame.image.load("resources/images/game_icon.png"))

        self.main_menu_scene: Scene = MainMenuScene(game=self, screen=self.screen)
        self.main_menu_scene.render_scene()

        self.current_scene = self.main_menu_scene

    def start(self):
        self.running = True
        self._game_loop()

    def show_scene(self, scene: Scene):
        self.current_scene = scene
        scene.render_scene()

    def quit(self):
        pygame.quit()
        sys.exit()

    @staticmethod
    def setup_displaymode():
        flags = pygame.DOUBLEBUF
        return pygame.display.set_mode(SCREEN_SIZE, flags)

    def _game_loop(self):
        try:

            while self.running:
                events: List[Any] = pygame.event.get()

                for event in events:
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    self.current_scene.on_key_input(event)

                self.current_scene.on_tick()
                self.screen.fill((0, 0, 0))
                self.current_scene.objects.update(self.current_scene, events)
                self.current_scene.objects.draw(self.screen)

                pygame.display.update()
                self.clock.tick(60)

            self.quit()
        except Exception as e:
            print("Game crashed with an unexpected error! {}".format(e))
            raise e