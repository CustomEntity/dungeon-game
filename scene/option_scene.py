import os
from typing import Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from . import main_menu_scene
from .scene import Scene, Button, Image


class OptionScene(Scene):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 30)

    def render_scene(self):
        background_image = pygame.transform.scale(pygame.image.load("./resources/images/main_menu_background.jpg"),
                                                  (1280, 720))
        background_object = self.screen.blit(background_image, (0, 0))

        self.add_object_to_render(Image(background_image, background_object))

        self.add_object_to_render(Button(
            text=self.font.render("Option 2: on", False, (255, 255, 255)),
            text_hovered=self.font.render("» Option 2: on", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 10),
            font=self.font,
            callback=lambda: self.game.show_scene(main_menu_scene.MainMenuScene(self.game, self.screen))
        ))
        self.add_object_to_render(Button(
            text=self.font.render("Option 1: off", False, (255, 255, 255)),
            text_hovered=self.font.render("» Option 1: off", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 30),
            font=self.font,
            callback=lambda: self.game.show_scene(main_menu_scene.MainMenuScene(self.game, self.screen))
        ))
        self.add_object_to_render(Button(
            text=self.font.render("« Retour", False, (255, 255, 255)),
            text_hovered=self.font.render("« Retour", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100),
            font=self.font,
            callback=lambda: self.game.show_scene(main_menu_scene.MainMenuScene(self.game, self.screen))
        ))
