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
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False

    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0

        self.animation_count += 1

        # if self.moving_right:
        #     display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (32, 42)), (self.x, self.y))
        # elif self.moving_left:
        #     display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (32, 42)), (self.x, self.y))
        # else:
        #     display.blit(pygame.transform.scale(player_walk_images[0], (32, 42)), (self.x, self.y))

        self.handle_weapons(display)

        self.moving_right = False
        self.moving_left = False