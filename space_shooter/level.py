from space_shooter import Background


class Level:
    """Class to represent a level. Takes the path to a background image,
    the number of waves to generate, and a tuple representing the number of enemies
    of each type generated per wave.
    Enemy tuple format: (asteroids, aliens, big_aliens)"""
    def __init__(self, bg_path, number_of_waves, enemy_tuple):
        self.background = Background(bg_path)
        self.waves = number_of_waves

        # Tuple containing the number of enemies per wave.
        # format: (asteroids, aliens, big_aliens)
        self.enemies = enemy_tuple
        self.alpha_fade_out = 255
        self.alpha_fade_in = 0
        self.background.image.set_alpha(self.alpha_fade_in)
        self.fading_in = True

    def image_fade_out(self):
        self.alpha_fade_out -= 1
        self.background.image.set_alpha(self.alpha_fade_out // 2)

    def image_fade_in(self):
        self.alpha_fade_in += 1
        self.background.image.set_alpha(self.alpha_fade_in // 2)
        if self.alpha_fade_in > 255:
            self.fading_in = False

