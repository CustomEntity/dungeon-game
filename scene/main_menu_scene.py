import os
from typing import Union

import pygame
from pygame.event import EventType
from pygame.surface import Surface
from pygame.surface import SurfaceType

from .scene import Scene, Button, Image


class MainMenuScene(Scene):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.begin_game_button = None
        self.option_button = None
        self.leave_button = None
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/Nemo Nightmares.ttf").replace("\\", "/"), 48)

    def on_tick(self):
        # if self.leave_button.collidepoint(pygame.mouse.get_pos()):
        #     leave_text = self.font.render("Quitter le jeu", True, (28, 147, 235))
        #     self.leave_button = self.screen.blit(leave_text, leave_text.get_rect(
        #         center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100)))
        pass

    def on_key_input(self, event: EventType):
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if self.leave_button.collidepoint(pygame.mouse.get_pos()):
        #         self.game.quit()
        pass

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
            text=self.font.render("Commencer la partie", True, (255, 255, 255)),
            text_hovered=self.font.render("Commencer la partie", True, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 10),
            font=self.font
        ))

        self.add_object_to_render(Button(
            text=self.font.render("Options", True, (255, 255, 255)),
            text_hovered=self.font.render("Options", True, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 60),
            font=self.font
        ))

        self.add_object_to_render(Button(
            text=self.font.render("Quitter le jeu", True, (255, 255, 255)),
            text_hovered=self.font.render("Quitter le jeu", True, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100),
            font=self.font,
            callback=self.game.quit
        ))

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.abspath("./resources/sounds/sound.wav").replace("\\", "/"))
        pygame.mixer.music.play(-1)
