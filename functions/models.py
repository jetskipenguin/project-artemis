import pygame
import sys
import math
import random

# animation stuff
#player_walk_images = [pygame.image.load("player_walk_0.png"), pygame.image.load("player_walk_1.png"),
#pygame.image.load("player_walk_2.png"), pygame.image.load("player_walk_3.png")]

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height