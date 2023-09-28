import pygame
from button import Buttons

class ItemEntry():
    
    def __init__(self, entryNum = "0", name = "Default", quantity = "0", expDate = "00/00/0000"):
        self.entryNum = entryNum
        self.name = name
        self.expDate = expDate
        self.quantity = quantity
        
        self.textRGB = (255,255,255)
        
        self.fontSize = 15
        self.font = pygame.font.Font('media/coolveticarg.otf', self.fontSize)
        
        self.nameText = self.font.render(str(self.name), True, self.textRGB)
        self.expDateText = self.font.render(str(self.expDate), True, self.textRGB)
        self.quantityText = self.font.render(str(self.quantity), True, self.textRGB)
        self.entryNumText = self.font.render(str(self.entryNum), True, self.textRGB)
        
        self.entryButton = Buttons(0,0,50,30,200,25,25,"Delete",10,0,0,0)
        
        
        
    def showItemInList(self, anchX, anchY, screen):
        
        entryBox = pygame.Rect(anchX, anchY, 460, 40)
        pygame.draw.rect(screen, (0,0,0), entryBox)
        
        nameTextRect = self.nameText.get_rect(centery = entryBox.centery, left = anchX + 50)
        screen.blit(self.nameText, nameTextRect)
        
        expDateTextRect = self.expDateText.get_rect(centery = entryBox.centery, left = anchX + 200)
        screen.blit(self.expDateText, expDateTextRect)
        
        quantityTextRect = self.quantityText.get_rect(centery = entryBox.centery, left = anchX + 150)
        screen.blit(self.quantityText, quantityTextRect)
        
        entryNumTextRect = self.entryNumText.get_rect(centery = entryBox.centery, left = anchX + 20)
        screen.blit(self.entryNumText, entryNumTextRect)
        
        self.entryButton.moveButton(anchX + 400, anchY + 5)
        self.entryButton.drawButton(screen)
        