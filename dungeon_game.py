import os
import sys
from typing import List, Any, Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from scene.credit_scene import CreditScene
from scene.scene import Scene

import commons.channels as channels
import json_package.game_manager as game_manager

SCREEN_SIZE = (1280, 720)


class Game:

    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        pygame.init()

        self.screen: Union[Surface, SurfaceType] = self.setup_displaymode()

        pygame.display.set_caption('Le Royaume de Vanedia')
        pygame.display.set_icon(pygame.image.load("resources/images/game_icon.png"))

        game_manager.load_story()

        channels.init_channels()

        self.current_scene = CreditScene(game=self, screen=self.screen)
        self.current_scene.render_scene()

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
            pygame.time.set_timer(pygame.USEREVENT + 1, 1)
            milis = 0
            while self.running:
                self.clock.tick()
                events: List[Any] = pygame.event.get()

                for event in events:
                    if event.type == pygame.USEREVENT + 1:
                        milis = milis + 1
                        self.current_scene.on_milis(milis)
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    self.current_scene.on_key_input(event)

                self.screen.fill((0, 0, 0))
                self.current_scene.objects.update(self.current_scene, events)
                self.current_scene.objects.draw(self.screen)
                self.current_scene.on_tick()

                pygame.event.pump()

                pygame.display.update()
                pygame.display.flip()

            self.quit()
        except Exception as e:
            print("Game crashed with an unexpected error! {}".format(e))
            raise e
