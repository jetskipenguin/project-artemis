from .models import Player
import pygame
import sys
import math
import random

def start_game():

    # Init Stuff
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

# display question and answer choices
def question(question: str, choices):
    pygame.init()

    # Screen Resolution
    res = (720,720)
    screen = pygame.display.set_mode(res)

    # Colors
    color = (255,255,255)
    hover_color = (255, 0, 0)
    color_dark = (0, 255, 0)

    # Fonts
    smallfont = pygame.font.SysFont('Corbel',35)

    # Screen Widths
    width = screen.get_width()
    height = screen.get_height()

    # rendering a text written in
    # this font
    quit = smallfont.render('quit' , True , color)
    
    # Text
    question_text = smallfont.render(question, True, color)
    texts = []
    for i in range(0, 4):
        texts.append(smallfont.render(choices[0], True, color))

    # Stores positions of buttons and text
    choice_coordinates = [(width/2 - 250, height/2 - 50), (width/2 + 100, height/2 - 50), (width/2 - 250, height/2 + 50), (width/2 + 100, height/2 + 50)]

    # Stores Height and Width of Answer Buttons
    button_width = 225
    button_height = 75
    
    while True:
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()
                
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if choice_coordinates[0][0] <= mouse[0] <= choice_coordinates[0][0] + button_width and choice_coordinates[0][1] <= mouse[1] <= choice_coordinates[0][1] + button_height:
                    pass
                    
        # fills the screen with a color
        screen.fill((60,25,60))

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()
        
        # Draws button for question 1, changes color when mouse hovers
        for i in range(0, 4):
            if choice_coordinates[i][0] <= mouse[0] <= choice_coordinates[i][0] + button_width and choice_coordinates[i][1] <= mouse[1] <= choice_coordinates[i][1] + button_height:
                pygame.draw.rect(screen,hover_color,[choice_coordinates[i][0], choice_coordinates[i][1],button_width,button_height])
            else:
                pygame.draw.rect(screen,color_dark,[choice_coordinates[i][0], choice_coordinates[i][1],button_width,button_height])

        # Render text onto screen
        # screen.blit(quit , (width/2+50,height/2))
        screen.blit(question_text, (width/2 - 150, height/2 - 150))
        for i in range(0, 3):
            screen.blit(texts[i], choice_coordinates[i])
        
        # updates the frames of the game
        pygame.display.update()
