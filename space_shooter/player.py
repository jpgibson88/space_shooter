import math

import pygame
from pygame.sprite import Sprite

import utils


class Player(Sprite):

    def __init__(self, mv_game):
        super().__init__()
        self.screen = mv_game.screen
        self.settings = mv_game.settings
        self.screen_rect = mv_game.screen.get_rect()

        image_conversion = 2.25
        self.original_image = pygame.image.load("images/player.png").convert()
        self.original_image_rect = self.original_image.get_rect()
        self.image = pygame.transform.smoothscale(self.original_image, (int(self.original_image_rect.width / image_conversion),
                                                                        int(self.original_image_rect.height / image_conversion)))
        self.image.set_colorkey((0, 0, 0))
        # self.original_image.set_colorkey((230, 230, 230))
        self.world_rect = self.image.get_rect()
        self.world_rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_up and self.world_rect.top > 0:
            self.world_rect.y -= self.settings.player_speed
        if self.moving_down and self.world_rect.bottom <= self.settings.screen_height - 20:
            self.world_rect.y += self.settings.player_speed
        if self.moving_right:
            self.world_rect.x += self.settings.player_speed
        if self.moving_left:
            self.world_rect.x -= self.settings.player_speed

        if self.world_rect.left >= self.settings.world_width:
            self.world_rect.left -= self.settings.world_width
        if self.world_rect.left < 0:
            self.world_rect.left += self.settings.world_width
        # utils.follow_mouse(self)

    def blitme(self):
        self.screen.blit(self.image, self.world_rect)