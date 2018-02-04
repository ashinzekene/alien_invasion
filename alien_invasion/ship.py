import pygame

class Ship():
    """Contains configurations for the ship""" 
    
    def __init__(self, screen):
        """initializes the ships and sets its position"""

        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its position"""
        self.screen.blit(self.image, self.rect)