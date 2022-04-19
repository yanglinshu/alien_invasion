import pygame
import sys
import time

from settings import Button
from settings import Settings
from settings import Ship

from run_game import check_events
from run_game import illuminate
from run_game import run_game

from gamestats import game_stats

from illuminate import display_slogan

def check_click(screen, setting, button_play, x, y):
    
    if(button_play.rect.collidepoint(x, y)):
        game_play(screen, setting)

def check_key(screen, setting, button_play):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_RETURN:
                game_play(screen, setting)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x ,y = pygame.mouse.get_pos()
            check_click(screen, setting, button_play, x, y)


def main(screen, setting):

    button_play = Button(screen, setting, setting.PLAY_TEXT)
    
    while 1:
        
        check_key(screen, setting,button_play)

        screen.fill(setting.BACK_GROUND)
        display_slogan(screen, setting)

        button_play.blit()
        pygame.display.flip()

def game_play(screen, setting):

        pygame.mouse.set_visible(0)

        stats = game_stats(setting)
        ship=Ship(screen, setting)        
        bullet_group = pygame.sprite.Group()
        alien_group = pygame.sprite.Group()

        clock = pygame.time.Clock()
        fps_factor = [0, time.time()]

        while 1:

            clock.tick(setting.FPS)
                
            screen.fill(setting.BACK_GROUND)
            illuminate(screen, setting, fps_factor, ship)

            check_events(screen, setting, ship, bullet_group)
            run_game(screen, setting, stats, ship, bullet_group, alien_group)

            if (not stats.game_active):
                    setting.FAIL = 1
                    pygame.mouse.set_visible(1)
                    return

def alien_invasion():
        
        pygame.init()

        setting = Settings()

        screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
        pygame.display.set_caption("Alien Invasion")

        while 1: main(screen, setting)
                

alien_invasion()