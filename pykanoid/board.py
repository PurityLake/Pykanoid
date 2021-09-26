"""board.py by Robert O'Shea 2021
Defines the board of tiles the player hits
"""

import pygame

from .tile import Tile


class Board:
    DEFAULT_BOARD = [
        [1, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1]
    ]
    DEFAULT_PADDING_X = 5
    DEFAULT_PADDING_Y = 5

    def __init__(self, scr_width, scr_height, x_start=0, y_start=0, board=DEFAULT_BOARD):
        self.scr_width, self.scr_height = scr_width, scr_height
        self.x_start, self.y_start = x_start, y_start

        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        
        self._calculate_tile_width()

        self.sprite_group = pygame.sprite.Group()

        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if col == 1:
                    self.sprite_group.add(
                        Tile(self.x_start + x * self.tile_width + x * self.DEFAULT_PADDING_X,
                             self.y_start + y * Tile.HEIGHT + y * self.DEFAULT_PADDING_Y,
                             width=self.tile_width))

    def draw(self, surf_target):
        for tile in self.sprite_group:
            surf_target.blit(tile.surf, tile.rect)

    def _calculate_width(self):
        self.scr_width -= self.x_start * 2

    def _calculate_tile_width(self):
        self._calculate_width()

        self.tile_width = self.scr_width / self.cols - self.DEFAULT_PADDING_X

    def __iter__(self):
        return iter(self.sprite_group)
