import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing a single alien"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load an image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start a new alient near the top of the screen
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width

        # store float position of alien
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)