import pygame
from button import Buttons
from variables import Variables
from background import Background

###
# Window Initializers
###
pygame.init() #Initializes a window

vars = Variables() #Variable Holster Object
background = Background()

screen = pygame.display.set_mode([vars.sW, vars.sH]) #Makes a screen that's that wide

while not vars.done: #Determines what is rendered each frame

    vars.eventHandler()
    background.drawMainBackground(screen)
    