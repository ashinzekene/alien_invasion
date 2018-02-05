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


def update_bullets(bullets):
    bullets.update()
    # removing unviewable bullets
    for bullet in bullets.copy():
        if bullet.rect.y <= 2:
            bullets.remove(bullet)


def fire_bullet(ai_settings, bullets, ship, screen):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """Create full list of aliens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space / (2 * alien_width))

    # create the first row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
