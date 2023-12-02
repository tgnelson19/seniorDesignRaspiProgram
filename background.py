import pygame

class Background:
    def __init__(self):
        self.frontUIBackground = pygame.Rect(0, 0, 800, 480)  #Backgroung rectangle 
        self.leftUIFrame = pygame.Rect(20, 60, 520, 400)  #The left UI frame placement
        self.rightUIFrame = pygame.Rect(560, 20, 220, 440)  #The right UI frame

        self.topFrame = pygame.Rect(0, 0, 520, 60)  
        self.botFrame = pygame.Rect(0,460,520,20)

        self.fontSize = 20
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        self.textRGB = (0,0,0)

        self.nameText =  self.font.render("Name", True, self.textRGB)
        self.entryDateText = self.font.render("Entry Date", True, self.textRGB)
        self.expirationDateText = self.font.render("Expiration Date", True, self.textRGB)
        self.costText = self.font.render("Cost", True, self.textRGB)

        self.nameRect = self.nameText.get_rect(topleft = (40,20))
        self.entryDateRect = self.entryDateText.get_rect(topleft = (120,20))
        self.expirationDateRect = self.expirationDateText.get_rect(topleft = (240,20))
        self.costRect = self.costText.get_rect(topleft = (400,20))

    def drawMainBackground(self, screen):




        pygame.draw.rect(screen, (200, 200, 50), self.frontUIBackground) #Paints background with given RGB
        pygame.draw.rect(screen, (200, 200, 200), self.leftUIFrame) #Paints left UI frame with given RGB
        pygame.draw.rect(screen, (200, 200, 200), self.rightUIFrame) #Paints right UI frame with given RGB




        


    def drawTopLevel(self,screen):

        pygame.draw.rect(screen, (200, 200, 50), self.topFrame) #Paints background with given RGB
        pygame.draw.rect(screen, (200, 200, 50), self.botFrame) #Paints background with given RGB

        screen.blit(self.nameText, self.nameRect)
        screen.blit(self.entryDateText, self.entryDateRect)
        screen.blit(self.expirationDateText, self.expirationDateRect)
        screen.blit(self.costText,self.costRect)