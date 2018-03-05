import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create  bullet object at the ship's position"""
        super().__init__()
        self.screen = screen

        # Create a bullet at Rect 0,0 then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store position of bullet as float
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """update position of bullet"""
        self.y -= self.speed_factor
        # update speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)