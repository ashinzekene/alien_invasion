import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Contains configurations for the ship"""

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        """initializes the ships and sets its position"""

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.float_centerx = float(self.rect.centerx)
        self.float_centery = float(self.rect.centery)
        # movements
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def blitme(self):
        """Draw the ship at its position"""
        self.screen.blit(self.image, self.rect)

    def update(self, ai_settings):
        if self.moving_up and self.rect.top > 0:
            self.float_centery -= ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.float_centery += ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.float_centerx -= ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.float_centerx += ai_settings.ship_speed_factor

        # Update ship center from float center
        self.rect.centerx = self.float_centerx
        self.rect.centery = self.float_centery

    def center_ship(self):
        """Center the ship on the screen"""
        self.float_centerx = self.screen_rect.centerx
        self.float_centery =  self.screen_rect.bottom - (1/2 * self.rect.height)