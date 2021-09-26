"""ball.py by Robert O'Shea 2021
Implements ball to break tiles
"""

import pygame


class Ball(pygame.sprite.Sprite):
    COLOR = (0, 0, 0)
    WIDTH, HEIGHT = 15, 15
    HALF_W, HALF_H = WIDTH / 2, HEIGHT / 2
    X_SPEED, Y_SPEED = 3, 2.5

    def __init__(self, scr_width, scr_height):
        super().__init__()
        self.x_dir, self.y_dir = 1, 1
        self.x = scr_width / 2 - self.HALF_W
        self.y = scr_height / 2 - self.HALF_H
        self.scr_width, self.scr_height = scr_width, scr_height
        self.surf = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surf.fill(self.COLOR)
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x += self.X_SPEED * self.x_dir
        self.y += self.Y_SPEED * self.y_dir
        
        if self.x < 0:
            self.x = 0
            self.x_dir = -self.x_dir
        elif self.x + self.WIDTH > self.scr_width:
            self.x = self.scr_width - self.WIDTH
            self.x_dir = -self.x_dir

        if self.y_dir == -1 and self.y < 0:
            self.y = 0
            self.y_dir = -self.y_dir
        elif self.y + self.HEIGHT > self.scr_height:
            self.y = self.scr_width + self.HEIGHT
            self.y_dir = -self.y_dir

        self.rect.x, self.rect.y = self.x, self.y

    def draw(self, target_surf):
        target_surf.blit(self.surf, self.rect)