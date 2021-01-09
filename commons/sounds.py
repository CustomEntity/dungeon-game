from typing import Optional
import pygame

__all__: list['Sound'] = []


class Sound(object):

    def __init__(self, path: str):
        __all__.append(self)
        self.path = path
        self.sound: Optional[pygame.mixer.Sound] = None

    def get(self):
        if self.sound is None:
            self.load()
        return self.sound

    def load(self):
        if not self.sound:
            self.sound = pygame.mixer.Sound(self.path)

    def un_load(self):
        del self.sound
        self.sound = None

    def __str__(self):
        print("Sound : {}".format(self.path))


MAIN_MENU = Sound('./resources/sounds/main-menu-sound.wav')
CLICK = Sound('./resources/sounds/click.mp3')
