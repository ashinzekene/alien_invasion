class Settings():
    """A class conatining the settings for the alien invasion game""" 
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 640
        self.bg_color = (230, 230, 230)      
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)