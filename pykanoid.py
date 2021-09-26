"""pykanoid.py by Robert O'Shea 2021
Main driver of the game
"""

import sys

import pygame
from pygame.locals import *
from pygame.math import Vector2

from pykanoid.ball import Ball
from pykanoid.board import Board
from pykanoid.player import Player
from pykanoid.tile import Tile

class Pykanoid:
    """
    The Pykanoid game class
    """
    BACKGROUND_COLOR = (100, 100, 100)
    WIDTH, HEIGHT = 800, 600
    FPS = 60

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.display_surf = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pykanoid")

        self.player = Player(self.WIDTH, self.HEIGHT)
        self.ball = Ball(self.WIDTH, self.HEIGHT)
        self.board = Board(self.WIDTH, self.HEIGHT, x_start=10, y_start=50)

        self.start = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()

            self.clock.tick(self.FPS)

    def draw(self):
        self.display_surf.fill(self.BACKGROUND_COLOR)
        
        self.player.draw(self.display_surf)
        self.ball.draw(self.display_surf)
        self.board.draw(self.display_surf)

        pygame.display.update()

    def update(self):
        if self.start:
            self.player.update()
            self.ball.update()

            if pygame.sprite.collide_rect(self.player, self.ball):
                self.ball.y_dir = -1
                if self.ball.y < self.player.rect.y + Player.HEIGHT \
                    and self.ball.y + Ball.HEIGHT > self.player.rect.y:
                    x_min_bool = self.ball.x + Ball.WIDTH + 5 > self.player.rect.x
                    x_max_bool = self.ball.x - 5 < self.player.rect.x + Player.WIDTH
                    if x_min_bool or x_max_bool:
                        if self.player.delta != 0:
                            self.ball.x_dir = self.player.delta
                        else:
                            self.ball.x_dir = -self.ball.x_dir

            tiles_hit = pygame.sprite.spritecollide(self.ball, self.board.sprite_group, True)

            for tile in tiles_hit:
                self.ball.y_dir = -self.ball.y_dir
                if self.ball.y < tile.y and self.ball.y + Ball.HEIGHT > tile.y:
                    x_min_bool = self.ball.x + Ball.WIDTH + 5 > tile.x
                    x_max_bool = self.ball.x - 5 < tile.x + Tile.WIDTH
                    if not (x_min_bool or x_max_bool):
                        self.ball.x_dir = -self.ball.x_dir
                        #self.ball.y_dir = -self.ball.y_dir
                self.board.sprite_group.remove(tile)
        else:
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[K_SPACE]:
                self.start = True

if __name__ == "__main__":
    Pykanoid().run()
