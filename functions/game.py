from .models import Bird, Highscore_Counter, Meteriods, Question_Object, Life_Counter
import pygame
import sys
import webbrowser
import random
from copy import deepcopy

def start_screen(display, clock):
    # Instructions
    instructions = ['Dodge Asteroids and Navigate to NASA', 'Equipment to Answer Questions and Earn Points!']
    prompt = 'Click anywhere to start!'

    # Font and Colors
    color = (255, 255, 255)
    font = 'Corbel'
    smallfont = pygame.font.SysFont(font, 32)

    # Render Texts
    instruction_texts = [smallfont.render(instructions[0], True, color), smallfont.render(instructions[1], True, color)]
    prompt_text = smallfont.render(prompt, True, color)

    # Text Coordinates
    width = display.get_width()
    height = display.get_height()
    instruction_coords = [(width/2 - 250, height/2 - 150), (width/2 - 250, height/2 - 100)]
    prompt_coords = (width/2 - 200, height/2)

    background = pygame.image.load('sprites/background.jpg')

    # Start screen
    while True:
        display.fill((0,0,0))
        display.blit(background, [0,0])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(0, len(instruction_texts)):
            display.blit(instruction_texts[i], instruction_coords[i])
        display.blit(prompt_text, prompt_coords)
        
        clock.tick(60)
        pygame.display.update()

def create_new_object(display, curr_category):
    if curr_category == 0:
        return Question_Object(display, 'EVA')
    elif curr_category == 1:
        return Question_Object(display, 'HLS')
    elif curr_category == 2:
        return Question_Object(display, 'Lunar Base')
    elif curr_category == 3:
        return Question_Object(display, 'Lunar Gateway')
    elif curr_category == 4:
        return Question_Object(display, 'Orion')
    elif curr_category == 5:
        return Question_Object(display, 'Artemis')
    else:
        return Question_Object(display, 'Moon')

def start_game():
    # Init Stuff
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    start_screen(display, clock)

    width = display.get_width()
    height = display.get_height()

    # Initialize Objects
    player = Bird(display)

    score = Highscore_Counter(width/2 + 100, height/2 - 300, 0)
    life_counter = Life_Counter(width/2 - 100, height/2 - 300, 300)

    rocks = []
    for i in range(0, 3):
        rocks.append(Meteriods(display))

    # Create instance of each question type
    # objects = [eva, hls, lunar_base, lunar_gateway, orion_capsule, artemis, moon]
    curr_category = random.randint(0, 6)
    object = create_new_object(display, curr_category)
    
    background = pygame.image.load('sprites/background.jpg')

    # Start game loop
    while True:
        pygame.display.set_caption('D.I.A.N.A | Dodging In-game Asteroids Near Artemis')
        display.fill((0,0,0))
        display.blit(background, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.handle_keys()
        life_counter.draw(display)
        score.draw(display)
        object.draw(display)

        if player.rect.colliderect(object.rect):
            print("Collided with {}".format(object))
            seed = random.randint(1, len(object.questions)-1)
            q = False

            new_list = deepcopy(object.answers[seed])
            random.shuffle(object.answers[seed])
            
            q = question(object.questions[seed], object.answers[seed], new_list[0], object.links)
            print(object.type)
            
            curr_category = random.randint(0, 6)
            object = create_new_object(display, curr_category)

            if q == True:
                score.increment()

        for i in rocks:
            if player.rect.colliderect(i.rect):
                life_counter.decrement()

        player.draw(display)
        for i in rocks:
            i.draw(display)
        
        if life_counter.count < 0:
            return 0

        clock.tick(60)
        pygame.display.update()

# returns pygame font object in correct size depending on character count
def resizeFont(user_input, font):
    if len(user_input) > 60:
        return pygame.font.SysFont(font, 18)
    if len(user_input) > 50:
        return pygame.font.SysFont(font, 22)
    elif len(user_input) > 40:
        return pygame.font.SysFont(font, 26)
    elif len(user_input) > 30:
        return pygame.font.SysFont(font, 30)
    elif len(user_input) > 20:
        return pygame.font.SysFont(font, 36)
    else:
        return pygame.font.SysFont(font, 38)

# display question and answer choices
def question(question: str, choices, correct_choice, weblink=None):
    pygame.init()

    # set window icon
    icon = pygame.image.load('sprites\\window_icon.png')
    pygame.display.set_icon(icon)

    # Screen Resolution
    res = (720,520)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('Question')
    
    #### Colors
    # Text Color
    color = (255, 255, 255)
    # Hover Color
    hover_color = (0, 0, 204)
    # Button Color
    color_dark = (0, 0, 153)
    # Background Color
    background_color = (0,0,0)

    # Fonts
    font = 'Corbel'
    smallfont = pygame.font.SysFont(font, 32)
    # Sizes text accordingly
    new_font = resizeFont(question, font)

    # Screen Widths
    width = screen.get_width()
    height = screen.get_height()
    
    # Text
    question_text = new_font.render(question, True, color)
    texts = []
    for i in range(0, 4):
        print(choices)
        new_font = resizeFont(choices[i], font)
        texts.append(new_font.render(choices[i], True, color))

    # Stores positions of buttons and text
    choice_coordinates = [(width/2 - 250, height/2 - 50), (width/2 + 100, height/2 - 50), (width/2 - 250, height/2 + 50), (width/2 + 100, height/2 + 50)]
    question_coord = (width/2 - 300, height/2 - 150)

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

    # Stores positions of buttons and text
    choice_coordinates = [(20, 91), (20, 174), (20, 257), (20, 340)]
    question_coord = (20, 8)

    # Stores Height and Width of Answer Buttons
    button_width = 680
    button_height = 75

    # Weblink Stuff
    weblink_text = smallfont.render('Hint', True, color)
    weblink_width = 680
    weblink_height = 75
    weblink_color = (230, 65, 65)
    weblink_hover_color = (239, 102, 102)
    weblink_coords = (20 , 423)

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
                    try:
                        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(weblink)
                    except:
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
