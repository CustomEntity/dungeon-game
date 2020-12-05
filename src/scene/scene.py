from abc import abstractmethod
from typing import Any, List, Union

from pygame import Surface
from pygame.surface import SurfaceType


class Scene:

    def __init__(self, screen: Union[Surface, SurfaceType]):
        self.screen = screen

    def on_key_input(self, events: List[Any]):
        pass

    def render_scene(self):
        pass
