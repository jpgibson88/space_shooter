import random
import sys
import time

import pygame

import utils
import level

from pygame.sprite import Sprite, Group, GroupSingle
from pygame.math import Vector2
from settings import Settings
from player import Player
from bullet import Bullet
from alien import Alien, BigAlien, Asteroid
from wormhole import Wormhole


class Spaceshooter:

    def __init__(self):
        pygame.init()

        # Initialize game settings and screen
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Spaceshooter")
        self.clock = pygame.time.Clock()
        self.wormhole_activated = False
        self.game_over = False

        # Initialize sprite groups
        self.player = Player(self)
        self.player_group = Group(self.player)
        self.bullets = Group()
        self.aliens = Group()
        self.wormhole_group = GroupSingle()

        # Initialize levels list
        self.levels = self._generate_levels()
        self.level_index = 0
        self.current_level = self.levels[self.level_index]
        self.delay_frames_left = self.settings.level_delay

        self.static_sprites = Group(self.levels[self.level_index].background)

        # Initialize viewport
        self.viewport = Viewport(self)
        self.viewport.update(self.player)
        self._update_screen()


    # Core game loop
    def run_game(self):

        while not self.game_over:
            self._check_events()
            if self.settings.game_active:
                self.player_group.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()

                if not self.aliens:
                    if self.current_level.waves > 0:
                        self.create_wave()
                    elif self.level_index < len(self.levels) - 1:
                        if not self.wormhole_group.sprite:
                            self.wormhole_group.add(Wormhole(self))
                        if self.wormhole_activated:
                            if self.delay_frames_left > 0:
                                self.delay_frames_left -= 1
                                self.current_level.image_fade_out()
                            else:
                                self._next_level()

    # Screen updates
    def _update_screen(self):

        self.screen.fill((0, 0, 0))
        if self.current_level.fading_in:
            self.current_level.image_fade_in()
        self.viewport.draw_group(self.static_sprites, self.screen)
        self.viewport.draw_group(self.player_group, self.screen)
        self.viewport.draw_group(self.bullets, self.screen)
        self.viewport.draw_group(self.aliens, self.screen)
        if self.level_index < len(self.levels) and self.current_level.waves <= 0:
            self.viewport.draw_group(self.wormhole_group, self.screen)
            self.check_wormhole_collision()
        self.check_collisions()
        self.viewport.update(self.player)
        pygame.display.flip()
        self.clock.tick(self.settings.fps)

    def check_collisions(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        player_collision = pygame.sprite.groupcollide(self.player_group, self.aliens, True, True)
        if player_collision:
            self.settings.game_active = False

    def check_wormhole_collision(self):
        wormhole_collision = pygame.sprite.groupcollide(self.player_group, self.wormhole_group, False, False)
        if wormhole_collision:
            self.wormhole_activated = True

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if utils.check_edges(bullet, bullet.world_rect):
                bullet.kill()

    def _update_aliens(self):
        self.aliens.update()

    # Object creation

    def _generate_levels(self):
        level1 = level.Level("images/orange.png", 2, (10, 5, 2))
        level2 = level.Level("images/black.png", 3, (80, 0, 0))
        return [level1, level2]

    def create_wave(self):
        """Creates a wave of enemies with the number of enemies passed in the enemy_tuple.
        Enemy tuple should be formatted as: (asteroids, aliens, big_aliens)"""
        # Enemy tuple should be formatted as:
        #   (asteroids, aliens, big_aliens)
        self.current_level.waves -= 1
        for i in range(self.current_level.enemies[0]):
            self._create_alien(Asteroid(self))
        for i in range(self.current_level.enemies[1]):
            self._create_alien(Alien(self))
        for i in range(self.current_level.enemies[2]):
            self._create_alien(BigAlien(self))

    def _create_alien(self, alien):
        x_pos = self.player.world_rect.x + self.settings.world_width / 2 + random.randrange(0, 100)
        alien.x, alien.y = random.randrange(x_pos, x_pos + 400),\
            random.randrange(0, self.settings.screen_height - alien.image.get_height())
        alien.world_rect.x, alien.world_rect.y = alien.x, alien.y
        self.aliens.add(alien)

    def _fire_bullet(self, mouse_pos):
        new_bullet = Bullet(self, mouse_pos)
        self.bullets.add(new_bullet)

    def _next_level(self):
        self.level_index += 1
        if self.level_index >= len(self.levels):
            self.game_over = True
            self.settings.game_active = False
            return
        self.wormhole_group.empty()
        self.wormhole_activate = False
        self.current_level = self.levels[self.level_index]
        self.static_sprites.empty()
        self.static_sprites.add(self.current_level.background)

    # Event handling

    def _is_game_over(self):
        return self.level_index < len(self.levels) and self.current_level.waves > 0

    def _check_events(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._fire_bullet(pygame.mouse.get_pos())

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            print("debugging")


class Background(Sprite):
    def __init__(self, img_path, *args):
        super().__init__(*args)
        self.image = pygame.image.load(img_path).convert()
        self.image = pygame.transform.smoothscale(self.image, (2160, 1280))
        self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()


class Viewport:
    def __init__(self, mv_game):
        self.left = 0
        self.settings = mv_game.settings

    def update(self, sprite):
        self.left = sprite.world_rect.left - 300
        if self.left > self.settings.world_width:
            self.left -= self.settings.world_width
        if self.left < 0:
            self.left += self.settings.world_width

    def compute_rect(self, group, dx=0):
        for sprite in group:
            sprite.rect = sprite.world_rect.move(-self.left + dx, 0)

    def draw_group(self, group, surface):
        self.compute_rect(group)
        group.draw(surface)
        self.compute_rect(group, self.settings.world_width)
        group.draw(surface)

if __name__ == '__main__':
    mv_game = Spaceshooter()
    mv_game.run_game()
