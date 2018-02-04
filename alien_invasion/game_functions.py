import sys
import pygame

def check_events(ship):
    """Respond to keypress and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_RIGHT:
                ship.moving_right = True
            if event.key ==  pygame.K_LEFT:
                ship.moving_left = True
            if event.key ==  pygame.K_UP:
                ship.moving_up = True
            if event.key ==  pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            ship.moving_right = False
            ship.moving_left = False
            ship.moving_up = False
            ship.moving_down = False
                
def update_screen(ai_settings, screen, ship):
    """Updates image son the screen and flips to the next screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()