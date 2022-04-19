import pygame
import sys

from time import sleep

from bullet import add_bullet
from bullet import bullet_update
from bullet import manual_reload

from alien import alien_update

from illuminate import display_fps
from illuminate import display_bullet
from illuminate import display_deadline
from illuminate import display_ship_left
from illuminate import display_score
from illuminate import display_max_score
from illuminate import display_level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def check_key(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.move_right ^= 1
    elif event.key == pygame.K_LEFT:
        ship.move_left ^= 1
    elif event.key == pygame.K_SPACE:
        if ship.shoot_mode and (not ship.reload):
            ship.add_bullet ^= 1

def check_quit(event):

    if event.type == pygame.QUIT:
        sys.exit() 
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()

def check_events(screen, setting, ship, bullet_group):

    for event in pygame.event.get():
        check_quit(event)
        if event.type == pygame.KEYDOWN:
            check_key(event, ship)
            if event.key == pygame.K_SPACE:
                if (not ship.shoot_mode) and (not ship.reload):
                    add_bullet(screen, setting, ship, bullet_group)
            elif event.key == pygame.K_b:
                ship.shoot_mode ^= 1
            elif event.key == pygame.K_r:
                manual_reload(ship)
        elif event.type == pygame.KEYUP:
            check_key(event, ship)

def clear_data(stats, ship, alien_group, bullet_group):

    ship.empty()
    alien_group.empty()
    bullet_group.empty()


def check_death(setting, stats, ship, alien_group, bullet_group):

    for alien in alien_group:
        if alien.rect.bottom >= setting.DEADLINE_POS[1]:
            stats.ship_left -= 1
            clear_data(stats, ship, alien_group, bullet_group)
            sleep(0.5)
            if (not stats.ship_left):
                setting.MAX_SCORE = max(setting.MAX_SCORE, stats.score)
                stats.game_active = 0
            return

def illuminate(screen, setting, fps_factor, ship):

    display_fps(screen, setting, fps_factor)
    display_bullet(screen, setting, ship)
    display_deadline(screen, setting)
    
def show_stats(screen, setting, stats, ship):

    display_ship_left(screen, setting, stats, ship)
    display_max_score(screen, setting)
    display_score(screen, setting, stats)
    display_level(screen, setting, stats)

def run_game(screen, setting, stats, ship, bullet_group, alien_group):
    
    bullet_update(screen, setting, ship, bullet_group)

    alien_update(screen, setting, stats, bullet_group, alien_group)

    check_death(setting, stats, ship, alien_group, bullet_group)

    ship.blit()
    ship.update()

    show_stats(screen, setting, stats, ship)

    pygame.display.flip()