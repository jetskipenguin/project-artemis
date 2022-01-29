from .models import Player
import pygame
import sys
import webbrowser

def start_game():

    # Init Stuff
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player(400, 300, 32, 32)

    # Start game loop
    while True:
        display.fill((24,164,86))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(display, (255,255,255), (player.x, player.y, 16, 16))

        player.move(pygame.key.get_pressed())

        clock.tick(60)
        pygame.display.update()

# display question and answer choices
def question(question: str, choices, correct_choice, weblink=None):
    pygame.init()

    # Screen Resolution
    res = (720,720)
    screen = pygame.display.set_mode(res)

    #### Colors
    # Text Color
    color = (255, 255, 255)
    # Hover Color
    hover_color = (108, 184, 216)
    # Button Color
    color_dark = (19, 149, 205)
    # Background Color
    background_color = (0,0,0)

    # Fonts
    smallfont = pygame.font.SysFont('Corbel',35)

    # Screen Widths
    width = screen.get_width()
    height = screen.get_height()
    
    # Text
    question_text = smallfont.render(question, True, color)
    texts = []
    for i in range(0, 4):
        texts.append(smallfont.render(choices[i], True, color))

    # Stores positions of buttons and text
    choice_coordinates = [(width/2 - 250, height/2 - 50), (width/2 + 100, height/2 - 50), (width/2 - 250, height/2 + 50), (width/2 + 100, height/2 + 50)]
    question_coord = (width/2 - 150, height/2 - 150)

    # Stores Height and Width of Answer Buttons
    button_width = 225
    button_height = 75
    
    # Weblink Stuff
    weblink_text = smallfont.render('Hint', True, color)
    weblink_width = 100
    weblink_height = 100
    weblink_color = (230, 65, 65)
    weblink_hover_color = (239, 102, 102)
    weblink_coords = (width/2 , height/2 + 150)

    while True:
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()
                
            # checks if a mouse is clicked
            for i in range(0, 4):
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if choice_coordinates[i][0] <= mouse[0] <= choice_coordinates[i][0] + button_width and choice_coordinates[i][1] <= mouse[1] <= choice_coordinates[i][1] + button_height:
                        if choices[i] == correct_choice:
                            question_text = smallfont.render('Correct!', True, color)
                            return True
                        else:
                            question_text = smallfont.render('Incorrect!', True, color)
                            return False
                    
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if weblink_coords[0] <= mouse[0] <= weblink_coords[0] + weblink_width and weblink_coords[1] <= mouse[1] <= weblink_coords[1] + weblink_height:        
                    webbrowser.open(weblink)

        # fills the screen with a color
        screen.fill(background_color)

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()
        
        # Draws button for question 1, changes color when mouse hovers
        for i in range(0, 4):
            # If mouse hovering over button
            if choice_coordinates[i][0] <= mouse[0] <= choice_coordinates[i][0] + button_width and choice_coordinates[i][1] <= mouse[1] <= choice_coordinates[i][1] + button_height:
                pygame.draw.rect(screen,hover_color,[choice_coordinates[i][0], choice_coordinates[i][1],button_width,button_height])
            else:
                # If mouse not hovering over button
                pygame.draw.rect(screen,color_dark,[choice_coordinates[i][0], choice_coordinates[i][1],button_width,button_height])

        # Draw rectangle for hint
        if weblink_coords[0] <= mouse[0] <= weblink_coords[0] + weblink_width and weblink_coords[1] <= mouse[1] <= weblink_coords[1] + weblink_height:
            pygame.draw.rect(screen, weblink_hover_color, [weblink_coords[0], weblink_coords[1], weblink_width, weblink_height])
        else:
            pygame.draw.rect(screen, weblink_color, [weblink_coords[0], weblink_coords[1], weblink_width, weblink_height])

        # Render text onto screen
        screen.blit(question_text, question_coord)
        for i in range(0, 4):
            screen.blit(texts[i], choice_coordinates[i])
            if weblink:
                screen.blit(weblink_text, weblink_coords)
        
        # updates the frames of the game
        pygame.display.update()
