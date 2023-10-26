import pygame

class Background:
    def __init__(self):
        #self.bigBackBackground = pygame.Rect(0, 0, 800, 480)  # Background Color Block
        self.frontUIBackground = pygame.Rect(0, 0, 800, 480)  # Foreground Background Color Block
        self.leftUIFrame = pygame.Rect(20, 20, 520, 440)  # The left UI frame
        self.rightUIFrame = pygame.Rect(560, 20, 220, 440)  # The right UI frame
        

    def drawMainBackground(self, screen):
       #pygame.draw.rect(screen, (40, 40, 40), self.bigBackBackground)
        pygame.draw.rect(screen, (200, 200, 50), self.frontUIBackground)
        pygame.draw.rect(screen, (200, 200, 200), self.leftUIFrame)
        pygame.draw.rect(screen, (200, 200, 200), self.rightUIFrame)
