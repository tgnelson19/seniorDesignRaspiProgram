import pygame
from button import Buttons
from variables import Variables

pygame.init() #Initializes a window

vars = Variables() #Variable Holster Object

while not vars.done: #Loop to render each frame

    vars.doAnUpdate()