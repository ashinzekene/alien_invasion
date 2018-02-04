import pygame

class Ship():
    """Contains configurations for the ship""" 
    
    def __init__(self, ai_settings, screen):
        """initializes the ships and sets its position"""

        self.screen = screen
        self.ai_settings =ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        # movements
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        

    def blitme(self):
        """Draw the ship at its position"""
        self.screen.blit(self.image, self.rect)

    def update(self, ai_settings):
        if self.moving_up:
            self.rect.bottom -= ai_settings.ship_speed_factor
        if self.moving_down:
            self.rect.bottom += ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= ai_settings.ship_speed_factor
        if self.moving_right:
            self.center += ai_settings.ship_speed_factor
            
        # Update ship center from float center
        self.rect.centerx = self.center