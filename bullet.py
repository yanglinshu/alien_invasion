import pygame
import time

from settings import Bullet
from illuminate import display_text

BLACK = (0, 0, 0)

def add_bullet(screen, setting, ship, bullet_group):

    ship.loaded_bullet += 1
    new_bullet = Bullet(screen, setting, ship)
    bullet_group.add(new_bullet)

def remove_sprite(screen, bullet_group):
    
    screen_rect = screen.get_rect()
    for bullet in bullet_group:
        if bullet.rect.top < screen_rect.top:
            bullet_group.remove(bullet)

def check_bullet(setting, ship):

    left = setting.BULLET_COUNT - ship.loaded_bullet
    if left == 0 and (not ship.reload):
        ship.reload = 1
        ship.reload_time = time.time()
        ship.reload_type = 1

def get_reload_time(setting, ship):

    if ship.reload:
        if ship.reload_type == 1:
            return setting.RELOAD_TIME_AUTO
        else:
            return setting.RELOAD_TIME_MANUAL
    else:
        return 0


def check_reload_end(screen, setting, ship):

    now = time.time()
    left_time = now - ship.reload_time
    reload_time = get_reload_time(setting, ship)
    if ship.reload and (left_time < reload_time):
        output_num = int((reload_time - left_time) * 100) / 100
        output = 'in ' + str(output_num) + ' s'
        display_text(screen, setting.RELOAD_TIMER_POS, output, setting.RELOAD_NUM_SIZE, color=BLACK)
        return True
    else:
        return False

def load_bullet(screen, setting, ship, bullet_group):

    is_reload = check_reload_end(screen, setting, ship)
    if (not ship.reload):
        if ship.shoot_mode and ship.add_bullet:
            add_bullet(screen, setting, ship, bullet_group)
    elif (not is_reload):
        ship.reload = 0
        ship.add_bullet = 0
        ship.loaded_bullet = 0
        ship.reload_type = 0
        
def manual_reload(ship):
    
    if (not ship.reload):
        ship.reload = 1
        ship.reload_time = time.time()
        ship.reload_type = 2

def bullet_update(screen, setting, ship, bullet_group):

    load_bullet(screen, setting, ship, bullet_group)
    check_bullet(setting, ship)
    bullet_group.update()
    remove_sprite(screen, bullet_group)
    bullet_group.draw(screen)