import sys
import pygame

def check_events(ship):
    """Respond to keypress and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_key_down(event, ship)
        elif event.type == pygame.KEYUP:
            check_events_key_up(event, ship)
                
def check_events_key_up(event, ship):
    # Responds to key releases
    if event.key ==  pygame.K_RIGHT:
        ship.moving_right = False
    if event.key ==  pygame.K_LEFT:
        ship.moving_left = False
    if event.key ==  pygame.K_UP:
        ship.moving_up = False
    if event.key ==  pygame.K_DOWN:
        ship.moving_down = False  
    
def check_events_key_down(event, ship):
    # Responds to key releases
    if event.key ==  pygame.K_RIGHT:
        ship.moving_right = True
    if event.key ==  pygame.K_LEFT:
        ship.moving_left = True
    if event.key ==  pygame.K_UP:
        ship.moving_up = True
    if event.key ==  pygame.K_DOWN:
        ship.moving_down = True  
    
def update_screen(ai_settings, screen, ship):
    """Updates image son the screen and flips to the next screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()