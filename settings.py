import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Settings():

        def __init__(self):

                self.WIDTH = 1200
                self.HEIGHT = 800
                self.BACK_GROUND = (230, 230, 230)
                self.GAP = 10

                self.RUN_FACTOR = 60
                self.FPS_POS = (0, 0)
                self.FPS = 60
                self.FPS_SIZE = 20
                
                self.SHIP_SPEED_FACTOR = 5
                self.SHIP_LIMIT = 3

                self.BULLET_SIZE = (3, 10)
                self.BULLET_COLOR = (60, 60, 60)
                self.BULLET_SPEED_FACTOR = 12 * self.RUN_FACTOR / self.FPS
                self.BULLET_COUNT = 30
                self.BULLET_NUMBER_SIZE = 40
                self.BULLET_POS = (self.WIDTH - self.BULLET_NUMBER_SIZE * 2, self.GAP)

                self.ALIEN_SPEED_FACTOR = 1 * self.RUN_FACTOR / self.FPS
                self.ALIEN_DROP_FACTOR = 15 * self.RUN_FACTOR / self.FPS
                self.ALIEN_DIRECTION = 1
                self.ALIEN_ACC = 1.1

                self.RELOAD_TIME_AUTO = 3
                self.RELOAD_TIME_MANUAL = 2.4
                self.RELOAD_SLOGAN = 'Reloading...'
                self.RELOAD_SIZE = 40
                self.RELOAD_NUM_SIZE = 30
                self.RELOAD_POS = (self.WIDTH - self.RELOAD_SIZE * 4, self.GAP)
                self.RELOAD_TIMER_POS = (self.WIDTH - self.RELOAD_SIZE * 4, self.GAP + self.RELOAD_SIZE)

                self.DEADLINE_SIZE = (self.WIDTH, 1)
                self.DEADLINE_POS = (0, self.HEIGHT - 60)

                self.BUTTON_WIDTH = 200
                self.BUTTON_HEIGHT = 50
                self.BUTTON_TEXT_SIZE = 60

                self.PLAY_TEXT = "PLAY"

                self.LEFT_SHIP_SIZE = 40
                self.LEFT_SHIP_POS = (self.WIDTH - self.LEFT_SHIP_SIZE * 2.5, self.GAP * 3 + self.RELOAD_SIZE)

                self.FAIL = 0
                self.FAIL_SIZE = 120

                self.SCORE_SIZE = 60
                self.SCORE_POINT = 50
                self.SCORE_ACC = 1.5
                self.MAX_SCORE = 0
                self.MS_TEXT = "MAX"
                self.MS_SIZE = 30
                self.MS_POS = (self.WIDTH - self.RELOAD_SIZE * 2, self.GAP * 3 + self.RELOAD_SIZE)
                self.MS_N_POS = (self.WIDTH - self.RELOAD_SIZE * 2, self.GAP * 3 + self.RELOAD_SIZE * 2)
                self.LEVEL_POS = (self.WIDTH - self.RELOAD_SIZE * 2, self.GAP * 3 + self.RELOAD_SIZE * 3)

                self.GAME_PLAY = 0

SHIPPATH = "H:\\Project\\Python\\alien_invasion\\ship.bmp"

class Ship():

        def __init__(self, screen, setting):

                self.screen = screen
                self.screen_rect = screen.get_rect()
                self.image = pygame.image.load(SHIPPATH)
                self.rect = self.image.get_rect()

                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
                self.centerx = float(self.rect.centerx)
                #self.rect.centerx只能储存整数，故另设变量储存

                self.move_right = 0
                self.move_left = 0

                self.speed_factor = setting.SHIP_SPEED_FACTOR

                self.add_bullet = 0
                self.shoot_mode = 0

                self.reload = 0
                self.loaded_bullet = 0
                self.reload_time = 0
                self.reload_type = 0

        def update(self):

                if self.move_right and self.rect.right < self.screen_rect.right:
                        self.centerx += self.speed_factor
                if self.move_left and self.rect.left > self.screen_rect.left:
                        self.centerx -= self.speed_factor
                self.rect.centerx = self.centerx

        def blit(self):

                self.screen.blit(self.image,self.rect)

        def empty(self):
                
                self.rect.centerx = self.screen_rect.centerx
                self.rect.bottom = self.screen_rect.bottom
                self.centerx = float(self.rect.centerx)

                self.add_bullet = 0
                self.shoot_mode = 0
                
                self.reload = 0
                self.loaded_bullet = 0
                self.reload_time = 0
                self.reload_type = 0


class Bullet(pygame.sprite.Sprite):

        def __init__(self, screen, setting, ship):

                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

                self.image = pygame.Surface(setting.BULLET_SIZE)
                self.image.fill(setting.BULLET_COLOR)

                self.rect = self.image.get_rect()
                self.rect.centerx = ship.rect.centerx
                self.rect.top = ship.rect.top

                self.y = float(self.rect.y)
                self.speed_factor = setting.BULLET_SPEED_FACTOR

        def update(self):

                self.y -= self.speed_factor
                self.rect.y = self.y
                

ALIENPATH = 'H:\\Project\\Python\\alien_invasion\\alien.bmp'

class Alien(pygame.sprite.Sprite):

        def __init__(self, screen ,setting):

                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

                self.image = pygame.image.load(ALIENPATH)

                self.rect = self.image.get_rect()
                self.rect.x = self.rect.width
                self.rect.y = self.rect.height

                self.x = float(self.rect.x)
                self.y = float(self.rect.x)

                self.speed_factor = setting.ALIEN_SPEED_FACTOR
                self.drop_factor = setting.ALIEN_DROP_FACTOR
                self.acc = setting.ALIEN_ACC

        def blit(self):

                self.screen.blit(self.image, self.rect)

        def check_edge(self):

                screen_rect = self.screen.get_rect()
                return self.rect.right >= screen_rect.right - self.rect.width * 2 or self.rect.left <= screen_rect.left

        def update(self, setting):

                self.x += (self.speed_factor * setting.ALIEN_DIRECTION)
                self.rect.x = self.x

class Button:

        def __init__(self, screen, setting, text):

                self.screen = screen
                self.screen_rect = self.screen.get_rect()

                self.width = setting.BUTTON_WIDTH
                self.height = setting.BUTTON_HEIGHT
                
                self.image = pygame.Surface((self.width, self.height))
                self.image.fill(RED)
                self.font = pygame.font.Font(None, setting.BUTTON_TEXT_SIZE)
                self.text_image = self.font.render(text, 1, WHITE)
                
                self.rect = self.image.get_rect()
                self.text_rect = self.text_image.get_rect()
                self.rect.centerx = setting.WIDTH / 2
                self.rect.centery = setting.HEIGHT / 2
                self.text_rect.centerx = self.rect.centerx
                self.text_rect.centery = self.rect.centery

        def blit(self):
                
                self.screen.blit(self.image, self.rect)
                self.screen.blit(self.text_image, self.text_rect)
                
