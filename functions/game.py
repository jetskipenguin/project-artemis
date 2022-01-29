from .models import Player
import pygame
import sys
import math
import random

def start_game():

    pygame.init()

    display = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player(400, 300, 32, 32)

    # Start game loop
    while True:
        display.fill((24,164,86))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        pygame.draw.rect(display, (255,255,255), (player.x, player.y, 16, 16))

        if keys[pygame.K_a]:
            player.x -= 5


        if keys[pygame.K_d]:
            player.x += 5

        if keys[pygame.K_w]:
            player.y += 5

        if keys[pygame.K_s]:
            player.y -= 5


        player.main(display)


        clock.tick(60)
        pygame.display.update()
