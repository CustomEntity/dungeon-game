import os
from typing import Union

import pygame
from pygame.event import EventType

from . import pause_menu_scene
from .scene import Scene, Image, Button
from pygame.surface import Surface
from pygame.surface import SurfaceType


class InGameScene(Scene):
    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 30)

    def on_key_input(self, event: EventType):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Pause du jeu")
                self.game.show_scene(pause_menu_scene.PauseMenuScene(self.game, self.screen))

    def render_scene(self):
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(2).unpause()

        if not pygame.mixer.Channel(2).get_busy():
            pygame.mixer.Channel(2).play(
                pygame.mixer.Sound(os.path.abspath("./resources/sounds/ambiences/clock.wav").replace("\\", "/")))

        background_image = pygame.transform.scale(pygame.image.load("./resources/images/area-background/bedroom.jpg"),
                                                  (1280, 720))
        background_object = self.screen.blit(background_image, (0, 0))

        self.add_object_to_render(Image(background_image, background_object))
