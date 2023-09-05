import pygame
from button import Buttons
from variables import Variables
from background import Background

###
# Window Initializers
###
pygame.init() #Initializes a window

vars = Variables() #Variable Holster Object
screen = pygame.display.set_mode([vars.sW, vars.sH]) #Makes a screen that's that wide

background = Background()

while not vars.done: #Determines what is rendered each frame

    vars.eventHandler()
    background.drawMainBackground(screen)
    vars.finishPaint(screen)

    