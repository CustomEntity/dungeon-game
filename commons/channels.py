from typing import Optional
import pygame

MUSIC_CHANNEL: Optional[pygame.mixer.Channel] = None
AMBIENT_CHANNEL: Optional[pygame.mixer.Channel] = None
AMBIENT_CHANNEL2: Optional[pygame.mixer.Channel] = None


def init_channels():
    global MUSIC_CHANNEL, AMBIENT_CHANNEL, AMBIENT_CHANNEL2
    pygame.mixer.init()

    MUSIC_CHANNEL = pygame.mixer.Channel(0)
    AMBIENT_CHANNEL = pygame.mixer.Channel(1)
    AMBIENT_CHANNEL2 = pygame.mixer.Channel(2)
