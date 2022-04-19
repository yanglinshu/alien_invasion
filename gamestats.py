import pygame
import time

class game_stats():

    def __init__(self, setting):

        self.ship_limit = setting.SHIP_LIMIT
        self.ship_left = self.ship_limit
        self.game_active = 1
        self.score = 0
        self.level = 0