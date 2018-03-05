class Settings():
    """A class conatining the settings for the alien invasion game"""

    def __init__(self):

        # screen settings
        self.screen_width = 1024
        self.screen_height = 660
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 0.7
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_x_margin = 70
        self.fleet_y_margin = 70
        # +1 right, -1 left
        self.fleet_direction = 1

        # for increasing values per level
        self.speed_up_scale = 1.1
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throghout the game"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self, speed = 1.1):
        self.ship_speed_factor *= 1.1
        self.bullet_speed_factor *= 1.1
        self.alien_speed_factor *= 1.1
        self.alien_points = int(self.alien_points * self.score_scale)
