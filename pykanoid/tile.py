"""self.py by Robert O'Shea 2021
Implements the breakable tile for Pykanoid
"""
import random

import pygame


class Tile(pygame.sprite.Sprite):
    """
    Tile that can be broken by the ball.
    """
    COLORS = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (0, 255, 255), (255, 0, 255)
    ]
    WIDTH = 30
    HEIGHT = 15

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.surf = pygame.Surface((width, height))
        self.surf.fill(random.choice(self.COLORS))
        self.rect = self.surf.get_rect(center=(width / 2, height / 2))
        self.rect.x, self.rect.y = x, y

    def setPos(self, x, y):
        self.x, self.y = x, y
        self.rect.x = self.rect.y = y

    def update(self):
        """
        Update method that is called every tick
        """
