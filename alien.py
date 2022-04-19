import pygame

from settings import Ship
from settings import Alien

def alienx(setting, width):

    spacex = setting.WIDTH - 3 * width
    alien_number = int(spacex / (2 * width))
    return alien_number

def alieny(setting, alien_height, ship_height):

    spacey = setting.HEIGHT - 3 * alien_height - ship_height * 2
    alien_row = int(spacey / (2 * alien_height))
    return alien_row

def add_alien(screen, setting, stats, alien_group, ycnt, xcnt):
    new_alien = Alien(screen, setting)
    new_alien.x = new_alien.rect.width + 2 * new_alien.rect.width * xcnt
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.rect.height * 2 + 2* new_alien.rect.height * ycnt
    new_alien.speed_factor = new_alien.speed_factor * (new_alien.acc ** stats.level)
    new_alien.drop_factor = new_alien.drop_factor * (new_alien.acc ** stats.level)
    alien_group.add(new_alien)

def add_fleet(screen, setting, stats, alien_group):

    alien_info = Alien(screen, setting)
    ship_info = Ship(screen, setting)
    alien_row = alieny(setting, alien_info.rect.height, ship_info.rect.height)
    alien_number = alienx(setting, alien_info.rect.width)
    for ycnt in range(0, alien_row):
        for xcnt in range(0, alien_number):
            add_alien(screen, setting, stats, alien_group, ycnt, xcnt)

def change_direction(setting, alien_group):

    for alien in alien_group.sprites():
        alien.rect.y += alien.drop_factor
    setting.ALIEN_DIRECTION *= -1

def check_collision(screen, setting, stats, bullet_group, alien_group):
    collision = pygame.sprite.groupcollide(bullet_group, alien_group, 1, 1)
    if collision:
        for alien in collision.values():
            stats.score += len(alien) * setting.SCORE_POINT * (setting.SCORE_ACC ** (stats.level - 1))
    if len(alien_group) == 0:
        stats.level += 1
        add_fleet(screen, setting, stats, alien_group)
        bullet_group.empty()

def check_edge(setting, alien_group):

    for alien in alien_group.sprites():
        if(alien.check_edge()):
            change_direction(setting, alien_group)
            return

def alien_update(screen, setting, stats, bullet_group, alien_group):
    
    check_edge(setting, alien_group)
    alien_group.update(setting)
    check_collision(screen, setting, stats, bullet_group, alien_group)
    alien_group.draw(screen)

