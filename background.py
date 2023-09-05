import pygame

class Background():
    
    def __init__(self):
        
        self.bigBackBackground = pygame.Rect(0,0,400,300)
        self.frontUIBackground = pygame.Rect(20,20,360,260)
        self.leftUIFrame = pygame.Rect(40,40,200,220)
        self.rightUIFrame = pygame.Rect(260,40,100,220)

    def drawMainBackground(self,screen):
    
        pygame.draw.rect(screen, (40,40,40), self.bigBackBackground)
        pygame.draw.rect(screen, (200,200,50), self.frontUIBackground)
        pygame.draw.rect(screen, (200,200,200), self.leftUIFrame)
        pygame.draw.rect(screen, (200,200,200), self.rightUIFrame)
        