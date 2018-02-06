import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_key_down(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_events_key_up(event, ship)


def check_events_key_up(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_q:
        sys.exit()


def check_events_key_down(event, ai_settings, screen, ship, bullets):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        # create a new bullet and add it to the bullet group
        fire_bullet(ai_settings, bullets, ship, screen)


def update_screen(ai_settings, aliens, bullets, screen, ship):
    """Updates image son the screen and flips to the next screen"""
    screen.fill(ai_settings.bg_color)
    aliens.draw(screen)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()

    # Check for collision with aliens
    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)
    
    # removing unviewable bullets
    for bullet in bullets.copy():
        if bullet.rect.y <= 2:
            bullets.remove(bullet)


def fire_bullet(ai_settings, bullets, ship, screen):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, aliens, screen, ship):
    """Create full list of aliens"""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    # create the first row of aliens
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width, screen)
    number_aliens_y = get_number_aliens_y(ai_settings, alien_height, ship_height)

    for alien_number in range(number_aliens_x):
        for row_number in range(number_aliens_y):
            create_alien(ai_settings, alien_number, aliens, screen, row_number)


def create_alien(ai_settings, alien_number, aliens, screen, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # left_margin + alien_space ( 2 alien width) * alien number
    alien.x = alien_width + 2 * alien_width * alien_number
    # top_margin + alien_space .....
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width, screen):
    """Deteermine the number of aliens tht fit into a row"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, alien_height, ship_height):
    """Determine the number of alien columns to fit screen"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_of_aliens = int(available_space_y / (2 * alien_height))
    return number_of_aliens


def update_aliens(ai_settings, aliens):
    """Check if fleet is at the edge then update"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    # MODIFY LATER TO CHANGE DIRECTION OF ONLY ONE ALIEN
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # chnage direction
    ai_settings.fleet_direction *= -1