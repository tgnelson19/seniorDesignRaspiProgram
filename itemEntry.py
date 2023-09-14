import pygame

class ItemEntry():
    
    def __init__(self, itemTag = 0, name = "Default", expDate = "00/00/0000"):
        self.tag = itemTag
        self.name = name
        self.expDate = expDate
        
        self.textRGB = (255,255,255)
        
        self.fontSize = 15
        self.font = pygame.font.Font('media/coolveticarg.otf', self.fontSize)
        
        self.nameText = self.font.render(str(self.name), True, self.textRGB)
        self.expDateText = self.font.render(str(self.expDate), True, self.textRGB)
        
        
        
    def showItemInList(self, anchX, anchY, screen):
        
        entryBox = pygame.Rect(anchX, anchY, 460, 60)
        pygame.draw.rect(screen, (0,0,0), entryBox)
        
        nameTextRect = self.nameText.get_rect(centery = entryBox.centery, left = anchX + 20)
        screen.blit(self.nameText, nameTextRect)
        
        expDateTextRect = self.nameText.get_rect(centery = entryBox.centery, left = anchX + 200)
        screen.blit(self.expDateText, expDateTextRect)
        