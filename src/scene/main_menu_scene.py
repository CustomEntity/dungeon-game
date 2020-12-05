from typing import Any, List

import os
import pygame

from .scene import Scene


class MainMenuScene(Scene):

    def on_key_input(self, events: List[Any]):
        print("KEY INPUT")

    def render_scene(self):
        background_image = pygame.transform.scale(pygame.image.load("../resources/images/main_menu_background.jpg"),
                                                  (1280, 720))
        font = pygame.font.Font("../resources/fonts/Nemo Nightmares.ttf", 64)
        self.screen.blit(background_image, (0, 0))

        begin_game_text = font.render("Commencer la partie", True, (250, 250, 250))
        begin_game = self.screen.blit(begin_game_text, begin_game_text.get_rect(
            center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 25)))

        option_text = font.render("Options", True, (250, 250, 250))
        option = self.screen.blit(option_text, option_text.get_rect(
            center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 75)))

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.abspath("../resources/sounds/sound.wav").replace("\\", "/"))
        pygame.mixer.music.play(-1)
