import pygame
import random

class Bird(object):  # represents the bird, not the game
    def __init__(self, display):
        """ The constructor of the class """
        self.bird = pygame.image.load("sprites/ship1.png")
        # the bird's position
        self.x = display.get_width()/2
        self.y = display.get_height()/2
        self.rect = self.bird.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # Player Movement
    def handle_keys(self):
        key = pygame.key.get_pressed()
        # bird speed
        dist = 10

        # move bird based on keyboard input
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.y += dist
            self.rect.y += dist
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.y -= dist
            self.rect.y -= dist
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.x += dist
            self.rect.x += dist
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= dist
            self.rect.x -= dist
    
    def draw(self, surface):
        surface.blit(self.bird, (self.x, self.y))

class Meteriods(object):  # represents the bird, not the game
    def __init__(self, display):
        """ The constructor of the class """
        self.rock = pygame.image.load("sprites/rock.png")
        # screen width
        self.width = display.get_width()
        self.height = display.get_height()
        # the rocks position
        x = random.randint(0,self.width)
        y = random.randint(0,self.height)
        self.x = x  #need to update this to start
        self.y = y
        self.rect = self.rock.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, surface):
        # random movement of rock
        x = random.randint(-5,5)
        y = random.randint(5,5)

        self.x += x
        self.y += y
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x > self.width:  #screen wrap
            self.x = random.randint(0,self.width)
            self.y = 0
            self.rect.y = 0
        if self.y > self.height:
            self.x = random.randint(0,self.width)
            self.y = 0
            self.rect.y = 0
        surface.blit(self.rock, (self.x, self.y))
        #print(self.rect)

class EVA(object): # EVA questions
    def __init__(self, display):
        """ The constructor of the class """
        self.EVA = pygame.image.load("sprites/EVA Suit.png")
        self.EVA = pygame.transform.scale(self.EVA,(75,75))

        # screen width
        self.width = display.get_width()
        self.height = display.get_height()

        # the EVA position
        x = random.randint(0,self.width)
        y = random.randint(0,self.height)
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

class Highscore_Counter:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count
        
        # Set Fonts and Colors
        self.font = pygame.font.SysFont('Corbel', 32)
        self.text = self.font.render('Highscore {}'.format(self.count) , True, (255,255,255))

    def decrement(self):
        print("AHHHHH")
        self.count -= 1
        self.text = self.font.render('Highscore {}'.format(self.count) , True, (255,255,255))

    def draw(self, display):
        display.blit(self.text, (self.x, self.y))