import pygame

class Background:
    def __init__(self):
        self.bigBackBackground = pygame.Rect(0, 0, 800, 480)  # Background Color Block
        self.frontUIBackground = pygame.Rect(20, 20, 760, 440)  # Foreground Background Color Block
        self.leftUIFrame = pygame.Rect(40, 40, 500, 400)  # The left UI frame
        self.rightUIFrame = pygame.Rect(560, 40, 200, 400)  # The right UI frame
        
        #Alan's First Comment

    def drawMainBackground(self, screen):
        pygame.draw.rect(screen, (40, 40, 40), self.bigBackBackground)
        pygame.draw.rect(screen, (200, 200, 50), self.frontUIBackground)
        pygame.draw.rect(screen, (200, 200, 200), self.leftUIFrame)
        pygame.draw.rect(screen, (200, 200, 200), self.rightUIFrame)
