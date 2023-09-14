import pygame
from background import Background

class Variables():

    def __init__(self):
        self.sW, self.sH = 800,480 #Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock() #Main time keeper

        self.done = False #Determines if the game is over or not
        self.mouseDown = False
        
        self.fontSize = 30
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)
        
        self.screen = pygame.display.set_mode([self.sW, self.sH]) #Makes a screen that's that wide
        
        self.background = Background()

    def doAnUpdate(self):
        
        self.eventHandler() # Updates with any potential user interaction
        
        

        self.background.drawMainBackground(self.screen) # Draws the background
        self.finishPaint() # Paints whatever is desired to be painted on the screen

    def eventHandler(self):

        self.clock.tick(30) #Keeps program to only 30 frames per second

        for event in pygame.event.get(): #Main event handler

            if event.type == pygame.QUIT: self.done = True #Close the entire program

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: self.done = True
                
            if event.type == pygame.MOUSEBUTTONDOWN: self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP: self.mouseDown = False

    def finishPaint(self):

        pygame.display.flip() #Displays currently drawn frame
        self.screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
        
    
        
