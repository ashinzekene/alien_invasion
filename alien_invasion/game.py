import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    pygame.display.set_caption("ALIEN INVASION")
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)

    ship = Ship(screen)
    

    # Start the main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ship.blitme()
        pygame.display.flip()


run_game()