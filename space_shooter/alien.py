import random

import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2

import utils


class Alien(Sprite):

    def __init__(self, mv_game):
        super().__init__()
        self.screen = mv_game.screen
        self.settings = mv_game.settings
        self.mv_game = mv_game

        self.image = pygame.image.load("images/alien_ship.png").convert()
        self.original_image = self.image.copy()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, False, True)
        self.world_rect = self.image.get_rect()

        self.world_rect.x = self.world_rect.width
        self.world_rect.y = self.world_rect.height

        # self.player_start = pygame.math.Vector2(mv_game.player.world_rect.center)
        # self.start = Vector2(self.world_rect.x, self.world_rect.y)
        # self.position = pygame.math.Vector2(self.start)
        # self.distance = self.player_start - self.start
        # self.speed = self.distance.normalize() * self.settings.alien_speed

        # self.position += self.speed
        # self.world_rect.x, self.world_rect.y = self.position.x, self.position.y

    def update(self):
        # self.position += self.speed
        # self.distance = Vector2(self.mv_game.player.world_rect.x, self.mv_game.player.world_rect.y) - Vector2(self.world_rect.x, self.world_rect.y)
        # self.world_rect.x, self.world_rect.y = self.position.x, self.position.y

        self.world_rect.x -= self.settings.alien_speed
        utils.world_wrap(self)


class BigAlien(Alien):

    def __init__(self, mv_game):
        super().__init__(mv_game)
        self.image = pygame.transform.scale2x(pygame.image.load("images/big_alien_ship.png").convert())
        self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()

        self.world_rect.x = self.world_rect.width
        self.world_rect.y = self.world_rect.height

        self.moving_down = False
        self.moving_up = True

    def update(self):
        self.world_rect.x -= self.settings.alien_speed / 2
        if self.moving_up:
            self.world_rect.y -= self.settings.alien_speed
        if self.moving_down:
            self.world_rect.y += self.settings.alien_speed
        if utils.check_edges(self, self.screen):
            self._flip_direction()

        utils.world_wrap(self)

    def _flip_direction(self):
        self.moving_up = not self.moving_up
        self.moving_down = not self.moving_down


class Asteroid(Alien):

    def __init__(self, mv_game):
        super().__init__(mv_game)
        # self.image = pygame.transform.smoothscale(self.image, (self.world_rect.width // 2, self.world_rect.height // 2))
        self.image = pygame.image.load("images/asteroid.png").convert()
        self.original_image = self.image.copy()
        self.rotation_angle = 5
        self.world_rect = self.image.get_rect()

        self.world_rect.x = self.world_rect.width
        self.world_rect.y = self.world_rect.height

        self.vertical_direction = random.randrange(-self.settings.alien_speed * 2, self.settings.alien_speed * 2)
        self.horizontal_direction = random.randrange(0, self.settings.alien_speed)

    def update(self):
        self.world_rect.x -= self.horizontal_direction
        self.world_rect.y += self.vertical_direction
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        self.rotation_angle += random.random() * 3
        utils.world_wrap(self)
