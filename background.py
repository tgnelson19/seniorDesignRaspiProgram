import pygame

class Background():
    
    def __init__(self):
        
        self.bigBackBackground = pygame.rect(0,0,400,300)
        self.frontUIBackground = pygame.rect(20,20,360,260)
        self.leftUIFrame = pygame.rect(40,40,200,220)
        self.rightUIFrame = pygame.rect(260,40,120,220)

    def drawMainBackground(self,screen):
    
        pygame.draw.rect(screen, (10,10,10), self.bigBackBackground)
        pygame.draw.rect(screen, (100,100,0), self.frontUIBackground)
        pygame.draw.rect(screen, (200,200,0), self.bigBackBackground)
        pygame.draw.rect(screen, (200,200,0), self.frontUIBackground)
        