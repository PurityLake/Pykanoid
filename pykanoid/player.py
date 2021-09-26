"""self.py by Robert O'Shea 2021
Implements the player which is the board at the bottom
of the screen
"""
import pygame
from pygame.locals import K_LEFT, K_RIGHT

from .ball import Ball


class Player(pygame.sprite.Sprite):
    """
    Sprite that hits the ball towards tiles
    """
    COLOR = (255, 255, 255)

    WIDTH = 70
    HEIGHT = 15
    HALF_H = HEIGHT / 2
    HALF_W = WIDTH / 2

    SPEED = 5

    def __init__(self, scr_width, scr_height):
        super().__init__()
        self.scr_width, self.scr_height = scr_width, scr_height
        self.surf = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surf.fill(self.COLOR)
        self.rect = self.surf.get_rect()
        self.rect.x = scr_width / 2 - self.HALF_W
        self.rect.y = scr_height - 30
        self.delta = 0

    def draw(self, surf_target):
        surf_target.blit(self.surf, self.rect)

    def update(self):
        """
        Update method that is called every tick
        """
        self.delta = 0

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.delta = -1
            self.rect.x -= self.SPEED
        elif pressed_keys[K_RIGHT]:
            self.delta = 1
            self.rect.x += self.SPEED

        if self.rect.x < 0:
            self.rect.x = 0
            self.delta = 0
        elif self.rect.x + self.WIDTH > self.scr_width:
            self.rect.x = self.scr_width - self.WIDTH
            self.delta = 0
