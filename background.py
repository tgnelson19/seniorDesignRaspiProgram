import pygame

class Background:
    def __init__(self):
        self.frontUIBackground = pygame.Rect(0, 0, 800, 480)  #Backgroung rectangle 
        self.leftUIFrame = pygame.Rect(20, 20, 520, 440)  #The left UI frame placement
        self.rightUIFrame = pygame.Rect(560, 20, 220, 440)  #The right UI frame

    def drawMainBackground(self, screen):
        pygame.draw.rect(screen, (200, 200, 50), self.frontUIBackground) #Paints background with given RGB
        pygame.draw.rect(screen, (200, 200, 200), self.leftUIFrame) #Paints left UI frame with given RGB
        pygame.draw.rect(screen, (200, 200, 200), self.rightUIFrame) #Paints right UI frame with given RGB
