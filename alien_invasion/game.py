import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game():
    pygame.init()
    pygame.display.set_caption("ALIEN INVASION")
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)

    ship = Ship(ai_settings, screen)
    

    # Start the main loop of the game
    while True:
        gf.check_events(ship)
        ship.update(ai_settings)
        gf.update_screen(ai_settings, screen, ship)


run_game()