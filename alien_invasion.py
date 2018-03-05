import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf


def run_game():
    pygame.init()
    pygame.display.set_caption("ALIEN INVASION")


    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)   

    play_button = Button(ai_settings, "PLAY", screen)
    stats = GameStats(ai_settings)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    ship = Ship(ai_settings, screen)

    # Create a fleet of alien ships
    gf.create_fleet(ai_settings, aliens, screen, ship)

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, aliens, bullets, play_button, sb, screen, ship, stats)
        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(ai_settings, aliens, bullets, sb, screen, ship, stats)
            gf.update_aliens(ai_settings, aliens, bullets, play_button, sb, screen, ship, stats)
            
        gf.update_screen(ai_settings, aliens, bullets, play_button, sb, screen, ship, stats)


run_game()