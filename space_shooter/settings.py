class Settings:

    def __init__(self, mv_game):

        self.game_active = True

        # Clock settings
        self.fps = 60
        self.level_delay = self.fps * 5

        # Screen settings
        self.mv_game = mv_game
        self.screen_width = 1080
        self.screen_height = 640
        self.world_width = 2 * self.screen_width
        self.world_height = 2 * self.screen_height
        self.bg_color = 230, 230, 230

        # Player settings
        self.player_speed = 4

        # Enemy settings
        self.alien_speed = 2

        # Bullet settings
        self.bullet_speed = 8
        self.bullet_color = (255, 0, 255)
        self.bullet_width = 5
        self.bullet_height = 5
        self.frames_alive = self.fps * 3
