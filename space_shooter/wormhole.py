import pygame.image
from pygame.sprite import Sprite


class Wormhole(Sprite):

    def __init__(self, mv_game):
        super().__init__()
        self.screen = mv_game.screen
        self.image = pygame.transform.scale2x(pygame.image.load("images/wormhole.png"))
        self.world_rect = self.image.get_rect()
        self.world_rect.x = mv_game.player.world_rect.x + 500
        self.world_rect.y = mv_game.player.world_rect.y

    def update(self):
        self.world_rect.x -= 1