import os
from typing import Union

import pygame
from pygame import Surface
from pygame.event import EventType
from pygame.surface import SurfaceType
from PIL import Image as pilimg, ImageSequence


class Scene(object):

    def __init__(self, game, screen: Union[Surface, SurfaceType]):
        self.screen = screen
        self.game = game
        self.hovering_button = False
        self.objects = pygame.sprite.Group()

    def on_tick(self):
        pass

    def on_key_input(self, event: EventType):
        pass

    def render_scene(self):
        pass

    def add_object_to_render(self, sprite):
        self.objects.add(sprite)

    @staticmethod
    def load_gif(filename):
        pil_image = pilimg.open(filename)
        frames = []
        for frame in ImageSequence.Iterator(pil_image):
            frame = frame.convert('RGBA')
            pygame_image = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode).convert_alpha()
            frames.append(pygame_image)
        return frames


class AnimatedImage(pygame.sprite.Sprite):
    def __init__(self, rect, images, speed):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = rect
        self.image_index = 0
        self.speed = speed
        self.current = 0

    def update(self, scene, events):
        self.current = self.current + 1
        if self.current != self.speed:
            return
        else:
            self.current = 0
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.image = self.images[self.image_index]


class Image(pygame.sprite.Sprite):

    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect


class Button(pygame.sprite.Sprite):

    def __init__(self,
                 rect=None,
                 rect_color=None,
                 rect_position=(0, 0),
                 text=None,
                 text_hovered=None,
                 font=None,
                 click_callback=None):
        super().__init__()
        self.rect = rect
        self.rect_color = rect_color
        self.rect_position = rect_position
        self.text = text
        self.text_hovered = text_hovered
        self.font = font

        if text is not None and rect is None:
            self.rect = text.get_rect(center=rect_position)

        self.original = self.text
        self.hovered = self.text_hovered

        self.image = self.original
        self.click_callback = click_callback

    def update(self, scene, events):
        is_colliding = self.rect.collidepoint(pygame.mouse.get_pos())
        already_hovering = scene.hovering_button

        if is_colliding and not already_hovering:
            self.image = self.hovered
            scene.hovering_button = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and is_colliding:
                    if self.click_callback is not None:
                        pygame.mixer.music.load(os.path.abspath("./resources/sounds/click.mp3").replace("\\", "/"))
                        pygame.mixer.music.play(start=0.6)
                        self.click_callback()

        elif is_colliding and already_hovering:
            self.image = self.original
            scene.hovering_button = True
        else:
            self.image = self.original
            scene.hovering_button = False


class SwitchButton(pygame.sprite.Sprite):

    def __init__(self, current_button, buttons):
        super().__init__()
        self.buttons = buttons
        self.current_button = current_button
        self.image = self.current_button.image
        self.rect = self.current_button.rect

    def set_current_button(self, button):
        self.current_button = button

    def update(self, scene, events):
        is_colliding = self.rect.collidepoint(pygame.mouse.get_pos())
        already_hovering = scene.hovering_button

        if is_colliding and not already_hovering:
            self.image = self.current_button.hovered
            scene.hovering_button = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and is_colliding:
                    if self.current_button.click_callback is not None:
                        pygame.mixer.music.load(os.path.abspath("./resources/sounds/click.mp3").replace("\\", "/"))
                        pygame.mixer.music.play(start=0.6)
                        self.current_button.click_callback()

        elif is_colliding and already_hovering:
            self.image = self.current_button.original
            scene.hovering_button = True
        else:
            self.image = self.current_button.original
            scene.hovering_button = False
