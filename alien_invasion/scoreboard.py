import pygame.font

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_settins, screen , stats):
        """Initialize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settins
        self.stats = stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the inital score image
        self.prep_score()
        self.prep_high_score()

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score= round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, False, self.ai_settings.bg_color)

        # center high score at center-top of screen 
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_rect.top
        

    def prep_score(self):
        """Turn scoreboard into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score) + " pts"
        self.score_image = self.font.render(score_str, False, self.text_color,
                                            self.ai_settings.bg_color)

        # Display score at topright of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Show score on scoreboard"""
        # print("Seee scoreboard")
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        