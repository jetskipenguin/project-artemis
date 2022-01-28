import pygame
import sys
import math
import random

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_walk_images = [pygame.image.load("player_walk_0.png"), pygame.image.load("player_walk_1.png"),
pygame.image.load("player_walk_2.png"), pygame.image.load("player_walk_3.png")]

player_weapon = pygame.image.load("shotgun.png").convert()
player_weapon.set_colorkey((255,255,255))

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
    def handle_weapons(self, display):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

        display.blit(player_weapon_copy, (self.x+15-int(player_weapon_copy.get_width()/2), self.y+25-int(player_weapon_copy.get_height()/2)))


    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0

        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (32, 42)), (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (32, 42)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_walk_images[0], (32, 42)), (self.x, self.y))

        self.handle_weapons(display)

        self.moving_right = False
        self.moving_left = False