import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, mv_game, mouse_pos):
        super().__init__()
        self.screen = mv_game.screen
        self.settings = mv_game.settings
        self.color = self.settings.bullet_color

        self.image = pygame.image.load("images/thrust3.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()
        self.world_rect.center = mv_game.player.world_rect.center
        self.start = pygame.math.Vector2(mv_game.player.world_rect.center)
        self.position = pygame.math.Vector2(self.start)
        self.distance = mouse_pos - self.start
        self.speed = self.distance.normalize() * self.settings.bullet_speed
        self.frames_left = self.settings.frames_alive

    def update(self):
        # self.position += self.speed
        # self.world_rect.x, self.world_rect.y = self.position.x, self.position.y

        self.world_rect.x += self.settings.bullet_speed

        if self.world_rect.left >= self.settings.world_width:
            self.position.x -= self.settings.world_width
            self.world_rect.left -= self.settings.world_width
        if self.world_rect.left < 0:
            self.position.x += self.settings.world_width
            self.world_rect.left += self.settings.world_width

        self.frames_left -= 1
        if self.frames_left == 0:
            self.kill()

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.world_rect)