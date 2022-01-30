import pygame
import random

# it is better to have an extra variable, than an extremely long line.


class Bird(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.bird = pygame.image.load("ship1.png")
        # the bird's position
        self.x = SCREENWidth/2
        self.y = SCREENHeight/2
        self.rect = self.bird.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
            self.rect.y += dist
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
            self.rect.y -= dist
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
            self.rect.x += dist
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
            self.rect.x -= dist

        #print("ship")
        #print(self.rect)


    def draw(self, surface):
        """ Draw on surface """

        # blit yourself at your current position
        surface.blit(self.bird, (self.x, self.y))

class Meteriods(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.rock = pygame.image.load("rock.png")
        # the rocks position
        x = random.randint(0,SCREENWidth)
        y = random.randint(0,SCREENHeight)
        self.x = x  #need to update this to start
        self.y = y
        self.rect = self.rock.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        #random movement of rock
        x = random.randint(-5,5)
        y = random.randint(5,5)
        self.x += x
        self.y += y
        #print('x', self.x)
        #print('y', self.y)
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x > SCREENWidth:  #screen wrap
            self.x = random.randint(0,SCREENWidth)
            self.y = 0
            self.rect.y = 0
        if self.y > SCREENHeight:
            self.x = random.randint(0,SCREENWidth)
            self.y = 0
            self.rect.y = 0
        surface.blit(self.rock, (self.x, self.y))
        #print(self.rect)

class EVA(object): # EVA questions
    def __init__(self):
        """ The constructor of the class """
        self.EVA = pygame.image.load("EVA Suit.png")
        self.EVA = pygame.transform.scale(self.EVA,(75,75))
        # the EVA position
        x = random.randint(0,SCREENWidth)
        y = random.randint(0,SCREENHeight)
        self.x = x  #need to update this to start
        self.y = y
        self.rect = self.EVA.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.EVA, (self.x, self.y))

'''def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
'''

if __name__ == "__main__":
    pygame.init()
    SCREENWidth = 600
    SCREENHeight = 800
    screen = pygame.display.set_mode((SCREENHeight, SCREENWidth))

    bird = Bird() # create an instance
    rock1 = Meteriods() # create a rock
    rock2 = Meteriods()
    rock3 = Meteriods()
    eva = EVA() #create an EVA instance
    clock = pygame.time.Clock()
    #question = random.randint(1,6) # initialize catagory
    #for testing
    question = 1

    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                running = False

        bird.handle_keys() # handle the keys

        screen.fill((0,0,0)) # fill the screen with white
        #print("question is ", question)
        # draw only one catagory
        if question == 1:
            EVA.draw(screen)
        #if catagory == 2:

        # search for collision
        if bird.rect.colliderect(rock1.rect):
            print("bird = ", bird.rect)
            print("rock is ", rock1.rect)
            print("Bird hit rock1")
        if bird.rect.colliderect(rock2.rect):
            print("Bird hit rock2")
        if bird.rect.colliderect(rock3.rect):
            print("Bird hit rock3")

        if bird.rect.colliderect(eva.rect) and question == 1:
            print("Bird hit EVA")
            question = 1 #random.randint(1,6)

        bird.draw(screen) # draw the bird to the screen
        rock1.draw(screen)
        rock2.draw(screen)
        rock3.draw(screen)
        pygame.display.update() # update the screen

        clock.tick(60)