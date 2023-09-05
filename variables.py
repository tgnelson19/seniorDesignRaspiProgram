import pygame

class Variables():

    def __init__(self):
        self.sW, self.sH = 400,300 #Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock() #Main time keeper

        self.done = False #Determines if the game is over or not
        self.mouseDown = False
        
        self.fontSize = 30
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)

    def eventHandler(self):

        self.clock.tick(30) #Keeps program to only 30 frames per second

        for event in pygame.event.get(): #Main event handler

            if event.type == pygame.QUIT: self.done = True #Close the entire program

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: self.done = True
                
            if event.type == pygame.MOUSEBUTTONDOWN: self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP: self.mouseDown = False

    def finishPaint(self, screen):

        pygame.display.flip() #Displays currently drawn frame
        screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
