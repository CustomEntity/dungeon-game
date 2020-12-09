from typing import Union

import pygame
from pygame import Surface
from pygame.event import EventType
from pygame.surface import SurfaceType


class Scene(pygame.sprite.Sprite):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__()
        self.screen = screen
        self.game = game
        self.objects = pygame.sprite.Group()

    def on_tick(self):
        pass

    def on_key_input(self, event: EventType):
        pass

    def render_scene(self):
        pass

class Button()
