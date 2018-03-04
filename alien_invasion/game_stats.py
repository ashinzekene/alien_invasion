class GameStats():
    def __init__(self, ai_settings):
        """Initialize the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_paused = False
        # Start game as inactive
        self.game_active = False
        self.game_over = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that change throughout the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
