from .models import Player
import pygame
import sys
import math
import random

def game():

    pygame.init()

    display = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player(400, 300, 32, 32)
    display_scroll = [0,0]

    # Start game loop
    while True:
        display.fill((24,164,86))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

        keys = pygame.key.get_pressed()

        pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

        if keys[pygame.K_a]:
            display_scroll[0] -= 5

            player.moving_left = True

        if keys[pygame.K_d]:
            display_scroll[0] += 5

            player.moving_right = True

        if keys[pygame.K_w]:
            display_scroll[1] -= 5

        if keys[pygame.K_s]:
            display_scroll[1] += 5


        player.main(display)


        clock.tick(60)
        pygame.display.update()
