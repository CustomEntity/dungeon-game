import os
from typing import Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from . import option_scene
from . import in_game_scene
from .scene import Scene, Button, Image


class MainMenuScene(Scene):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 30)

    def render_scene(self):
        background_image = pygame.transform.scale(pygame.image.load("./resources/images/main_menu_background.jpg"),
                                                  (1280, 720))
        background_object = self.screen.blit(background_image, (0, 0))

        logo = pygame.transform.scale(pygame.image.load("./resources/images/logo.gif").convert_alpha(), (500, 200))
        logo_object = self.screen.blit(logo,
                                       logo.get_rect(
                                           center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 200)))

        self.add_object_to_render(Image(background_image, background_object))
        self.add_object_to_render(Image(logo, logo_object))
        self.add_object_to_render(Button(
            text=self.font.render("Commencer la partie", False, (255, 255, 255)),
            text_hovered=self.font.render("» Commencer la partie", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 10),
            font=self.font,
            click_callback=lambda: self.game.show_scene(in_game_scene.InGameScene(self.game, self.screen))
        ))

        self.add_object_to_render(Button(
            text=self.font.render("Options", False, (255, 255, 255)),
            text_hovered=self.font.render("» Options", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 60),
            font=self.font,
            click_callback=lambda: self.game.show_scene(option_scene.OptionScene(self.game, self.screen))
        ))

        self.add_object_to_render(Button(
            text=self.font.render("Quitter le jeu", False, (255, 255, 255)),
            text_hovered=self.font.render("» Quitter le jeu", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100),
            font=self.font,
            click_callback=lambda: self.game.quit()
        ))
