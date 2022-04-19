import pygame
import time

from pygame import display
from pygame.transform import scale

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def display_text(screen, loction, text, size, color = WHITE, ttf = None, bold = False, italic = False):
    
    textfont = pygame.font.Font(ttf, size)
    textfont.set_bold(bold)
    textfont.set_italic(italic)
    textimage = textfont.render(text, True, color)
    screen.blit(textimage, loction)

def display_fps(screen, setting, factor):
    
    factor[0] += 1
    now = time.time()
    fps = int(factor[0] / (now - factor[1]))
    display_text(screen, setting.FPS_POS, str(fps), setting.FPS_SIZE, color = BLACK)

def display_bullet(screen, setting, ship):

    if ship.reload:
        display_text(screen, setting.RELOAD_POS, setting.RELOAD_SLOGAN, setting.RELOAD_SIZE, color=BLACK)
    else:
        left = setting.BULLET_COUNT - ship.loaded_bullet
        output = str(left) + '/' + str(setting.BULLET_COUNT)
        display_color = RED if left <= 5 else BLACK
        display_text(screen, setting.BULLET_POS, output, setting.BULLET_NUMBER_SIZE, color = display_color)

def display_deadline(screen, setting):

    deadline = pygame.Surface(setting.DEADLINE_SIZE)
    deadline.fill(BLACK)
    screen.blit(deadline, setting.DEADLINE_POS)

def display_ship_left(screen, setting, stats, ship):

    left = stats.ship_left
    for i in range(0, left):
        x = setting.GAP + (ship.rect.width + setting.GAP) * i
        y = setting.FPS_SIZE
        screen.blit(ship.image, (x, y))


def display_score(screen, setting, stats):

    textfont = pygame.font.Font(None, setting.SCORE_SIZE)
    score = round(stats.score)
    textimage = textfont.render(str(score), 1, BLUE)
    text_rect = textimage.get_rect()
    text_rect.centerx = setting.WIDTH / 2
    text_rect.y = setting.GAP
    screen.blit(textimage, text_rect)

def display_slogan(screen, setting):

    textfont = pygame.font.Font(None, setting.FAIL_SIZE)
    if setting.FAIL:
        output = "YOU DIED"
        color = RED
    else:
        output = "WELCOME"
        color = BLACK
    textimage = textfont.render(output, 1, color)
    textimage_rect = textimage.get_rect()
    textimage_rect.centerx = setting.WIDTH / 2
    textimage_rect.y = setting.GAP + setting.FAIL_SIZE
    screen.blit(textimage, textimage_rect)

def display_max_score(screen, setting):
    
    output = int(round(setting.MAX_SCORE, -1))
    display_text(screen, setting.MS_POS, setting.MS_TEXT, setting.MS_SIZE, BLACK)
    display_text(screen, setting.MS_N_POS, str(output), setting.MS_SIZE, BLACK)

def display_level(screen, setting, stats):

    output = "level: " + str(stats.level)
    display_text(screen, setting.LEVEL_POS, output, setting.MS_SIZE, BLACK)