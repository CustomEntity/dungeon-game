import os
from typing import Union

import pygame
from pygame.surface import Surface
from pygame.surface import SurfaceType

from . import main_menu_scene
from .scene import Scene, Button, Image, SwitchButton

import json


class OptionScene(Scene):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 30)
        self.music_button = None

    def render_scene(self):
        background_image = pygame.transform.scale(pygame.image.load("./resources/images/main_menu_background.jpg"),
                                                  (1280, 720))
        background_object = self.screen.blit(background_image, (0, 0))

        self.add_object_to_render(Image(background_image, background_object))

        data = json.load(open('./resources/settings.json'))

        music_on_button = Button(
            text=self.font.render("Musique: on", False, (0, 200, 0)),
            text_hovered=self.font.render("» Musique: on", False, (0, 115, 0)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 10),
            font=self.font,
            click_callback=lambda: (
                self.music_button.set_current_button(self.music_button.buttons['off']),
                self.set_setting(data, 'music', False),
                pygame.mixer.stop(),
            )
        )
        music_off_button = Button(
            text=self.font.render("Musique: off", False, (255, 0, 0)),
            text_hovered=self.font.render("» Musique: off", False, (115, 0, 0)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 10),
            font=self.font,
            click_callback=lambda: (
                self.music_button.set_current_button(self.music_button.buttons['on']),
                self.set_setting(data, 'music', True),
                pygame.mixer.stop(),
                pygame.mixer.Channel(0).play(self.game.game_sound, True)
            )
        )

        self.music_button = SwitchButton(
            music_on_button if data['music'] else music_off_button,
            {"on": music_on_button, "off": music_off_button}
        )

        self.add_object_to_render(self.music_button)

        self.add_object_to_render(Button(
            text=self.font.render("« Retour", False, (255, 255, 255)),
            text_hovered=self.font.render("« Retour", False, (12, 73, 122)),
            rect_position=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100),
            font=self.font,
            click_callback=lambda: self.game.show_scene(main_menu_scene.MainMenuScene(self.game, self.screen))
        ))

    def set_setting(self, data, setting, value):
        data[setting] = value
        self.save_settings(data)

    def save_settings(self, data):
        with open('./resources/settings.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
