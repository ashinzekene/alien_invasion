class GameStats():
    def __init__(self, ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game as inactive
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that change throughout the game"""
        self.ship_left = self.ai_settings.ship_limit
        
