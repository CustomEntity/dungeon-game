import os
from typing import Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from scene.main_menu_scene import MainMenuScene
from scene.scene import Scene, Image, Rectangle, Text


class CreditScene(Scene):
    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 70)

    def on_milis(self, milis):
        if milis % 2000 == 0:
            self.game.show_scene(MainMenuScene(game=self.game, screen=self.screen))

    def render_scene(self):
        customentity_image = pygame.transform.scale(pygame.image.load("./resources/images/customentity.png"),
                                                    (959, 540))
        customentity_object = self.screen.blit(customentity_image,
                                               (0, self.screen.get_height() / 7))

        self.add_object_to_render(Rectangle(1280, 720, 0, 0, (0, 0, 0)))
        self.add_object_to_render(Image(customentity_image, customentity_object))
        self.add_object_to_render(Text(self.font.render("Une Production de", True, (255, 255, 255)),
            (self.screen.get_width() - 350, self.screen.get_height() / 3)))

        self.add_object_to_render(Text(self.font.render("CustomEntity", True, (255, 255, 255)),
                                       (self.screen.get_width() - 350, self.screen.get_height() / 1.7)))

