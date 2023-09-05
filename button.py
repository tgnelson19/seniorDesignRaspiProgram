import pygame

class Buttons():

    def __init__(self, topLeftX, topLeftY, width, height, R, G, B, text, fontSize, textR, textG, textB):
        self.posX = topLeftX
        self.posY = topLeftY

        self.width = width
        self.height = height

        self.buttonRect = pygame.Rect(topLeftX, topLeftY, width, height)
        self.buttonRGB = (R,G,B)
        self.canBeClickedAgain = True

        self.textRGB = (textR, textG, textB)
        self.text = text
        self.fontSize = fontSize
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)
        self.textRender = self.font.render(str(self.text), True, self.textRGB)
        self.textRect = self.textRender.get_rect(center=(self.buttonRect.centerx, self.buttonRect.centery))

    def drawButton(self, screen):
        pygame.draw.rect(screen,self.buttonRGB, self.buttonRect) 
        screen.blit(self.textRender, self.textRect)

    def isHoveredOver(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mouseX,mouseY):
            leftGap = (self.buttonRect.width*1.2 - self.buttonRect.width)/2
            topGap = (self.buttonRect.height*1.2 - self.buttonRect.height)/2
            self.buttonRect = pygame.Rect(self.posX - leftGap, self.posY - topGap, self.width * 1.2, self.height * 1.2)
        else:
            self.buttonRect = pygame.Rect(self.posX, self.posY, self.width, self.height)

    def isClicked(self, mouseDown):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseDown:
            if self.buttonRect.collidepoint(mouseX,mouseY) and self.canBeClickedAgain:
                self.canBeClickedAgain = False
                return True
        else:
            self.canBeClickedAgain = True
            return False