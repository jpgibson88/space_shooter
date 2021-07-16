import math
import pygame


def follow_mouse(self):
    """Rotates player sprite to point towards the mouse cursor.
    Used code from StackOverflow post:
    https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    relative_x, relative_y = mouse_x - self.rect.x, mouse_y - self.rect.y
    angle = (180 / math.pi) * -math.atan2(relative_y, relative_x)
    self.image = pygame.transform.rotate(self.original_image, int(angle))

def check_edges(sprite, screen_rect):
    sprite_height = sprite.image.get_rect().height
    if sprite.world_rect.top <= 0:
        return True
    elif sprite.world_rect.bottom > sprite.settings.screen_height:
        return True
    return False

def world_wrap(self):
    if self.world_rect.left >= self.settings.world_width:
        self.world_rect.left -= self.settings.world_width
    if self.world_rect.left < 0:
        self.world_rect.left += self.settings.world_width
    if self.world_rect.bottom < 0:
        self.world_rect.bottom += self.settings.world_height
        self.world_rect.left -= self.settings.world_width
    if self.world_rect.bottom >= self.settings.world_height:
        self.world_rect.bottom -= self.settings.world_height
        self.world_rect.left += self.settings.world_width