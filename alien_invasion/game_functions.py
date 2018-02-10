import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, bullets, play_button, screen, ship, stats):
    """Respond to keypress and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_key_down(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_events_key_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


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


def update_screen(ai_settings, aliens, bullets, play_button, screen, ship,
                  stats):
    """Updates images on the screen and flips to the next screen"""
    if not stats.game_active:
        play_button.draw_button()

    screen.fill(ai_settings.bg_color)
    aliens.draw(screen)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(ai_settings, aliens, bullets, screen, ship):
    bullets.update()
    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship)
    # removing unviewable bullets
    for bullet in bullets.copy():
        if bullet.rect.y <= 2:
            bullets.remove(bullet)


def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship):
    # Check for collision with aliens
    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, aliens, screen, ship)
        ai_settings.alien_speed_factor += 0.2
        ai_settings.fleet_drop_speed += 3
        ai_settings.ship_speed_factor += 0.5
        ai_settings.bullet_limit += 0.5


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
    number_aliens_y = get_number_aliens_y(ai_settings, alien_height,
                                          ship_height)

    for alien_number in range(number_aliens_x):
        for row_number in range(number_aliens_y):
            create_alien(ai_settings, alien_number, aliens, screen, row_number)


def create_alien(ai_settings, alien_number, aliens, screen, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # left_margin + alien_space ( 2 alien width) * alien number
    alien.x = ai_settings.fleet_x_margin + 2 * alien_width * alien_number
    # top_margin + alien_space .....
    alien.y = ai_settings.fleet_y_margin + 2 * alien_height * row_number
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
    available_space_y = ai_settings.screen_height - (
        3 * alien_height) - ship_height
    number_of_aliens = int(available_space_y / (2 * alien_height))
    return number_of_aliens


def update_aliens(ai_settings, aliens, bullets, screen, ship, stats):
    """Check if fleet is at the edge then update"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats)

    # Check for ship alien collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, aliens, bullets, screen, stats, ship)


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


def ship_hit(ai_settings, aliens, bullets, screen, stats, ship):
    """Responds to ship being hit by an alien"""
    # Decrement ships left
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new alien fleet
        create_fleet(ai_settings, aliens, screen, ship)

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats):
    """Detect aliens that get to the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat as if the aliens hit the ship
            ship_hit(ai_settings, aliens, bullets, screen, stats, ship)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Starts a game when the player clicks"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

