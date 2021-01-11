import os
from typing import Union

import pygame
from pygame.event import EventType
from pygame.surface import Surface
from pygame.surface import SurfaceType

from json_package import game_manager
from . import pause_menu_scene
from .scene import Scene, Image, Text, Rectangle


class InGameScene(Scene):
    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        super().__init__(game, screen)
        self.font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 30)
        self.smaller_font = pygame.font.Font(os.path.abspath("./resources/fonts/bb.otf").replace("\\", "/"), 26)
        self.top_bar = Rectangle(self.screen.get_width(), 80, 0, 0, 'black')
        self.bottom_bar = Rectangle(self.screen.get_width(), 80, 0, self.screen.get_height() - 80, 'black')

        self.chapter_text = Text(
            self.font.render(game_manager.get_current_action_object().chapter, False, (255, 255, 255)),
            (self.screen.get_width() / 2, self.screen.get_height() / 2 - 320))

        self.coin_chapter_text = Text(
            self.smaller_font.render(game_manager.get_current_action_object().chapter, False, (255, 255, 255)),
            (225, self.screen.get_height() / 2 - 340))

    def on_key_input(self, event: EventType):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Pause du jeu")
                self.game.show_scene(pause_menu_scene.PauseMenuScene(self.game, self.screen))

    def on_milis(self, milis):
        if milis % 50 == 0:
            if self.top_bar.y <= -100 and self.is_rendered(self.top_bar):
                self.remove_object_to_render(self.top_bar)
                self.remove_object_to_render(self.bottom_bar)
                self.remove_object_to_render(self.chapter_text)
                self.add_object_to_render(self.coin_chapter_text)

                big_talk_ui_image = pygame.transform.scale(
                    pygame.image.load("./resources/images/ui/big_talk_ui.png"),
                    (540, 220))
                big_talk_ui_object = self.screen.blit(big_talk_ui_image,
                                                      (self.screen.get_width() / 3.5, self.screen.get_height() - 250))

                self.add_object_to_render(Image(big_talk_ui_image, big_talk_ui_object))
            else:
                self.top_bar.y -= 3.5
                self.bottom_bar.y += 3.5

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

        self.add_object_to_render(self.top_bar)
        self.add_object_to_render(self.bottom_bar)
        self.add_object_to_render(self.chapter_text)
