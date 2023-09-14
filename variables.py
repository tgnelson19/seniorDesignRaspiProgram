import pygame
from background import Background
from button import Buttons
from itemEntry import ItemEntry

class Variables():

    def __init__(self):
        
        pygame.init() #Initializes a window
        
        self.sW, self.sH = 800,480 #Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock() #Main time keeper

        self.done = False #Determines if the game is over or not
        self.mouseDown = False
        
        self.fontSize = 30
        self.font = pygame.font.Font('media/coolveticarg.otf', self.fontSize)
        
        self.screen = pygame.display.set_mode([self.sW, self.sH]) #Makes a screen that's that wide
        
        self.background = Background()
        
        self.addExampleEntry = Buttons(580,60,160,100,100,100,100,"Add Entry", 20, 255,255,255)

        self.buttonList = [self.addExampleEntry]
        
        exampleEntry = ItemEntry()
        
        self.entryList = [exampleEntry]
        
        
    def doAnUpdate(self):
        
        self.background.drawMainBackground(self.screen) # Draws the background first of everything
        self.eventHandler() # Updates with any potential user interaction
        
        if len(self.buttonList) != 0:
            
            for button in self.buttonList:
                button.drawButton(self.screen)
        
        
        if(self.addExampleEntry.isClicked(self.mouseDown)):
            newEntry = ItemEntry()
            self.entryList.append(newEntry)
            
            
        if len(self.entryList) != 0:
            
            anchX = 60
            anchY = 60
            
            for entry in self.entryList:
                entry.showItemInList(anchX, anchY, self.screen)
                anchY += 80
        

        
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
        
    
        
