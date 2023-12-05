import pygame
from button import Buttons
from datetime import date


class ItemEntry:
    
    
    #Initializer
    def __init__(
        self, entryNum="0", name="Default", entryDate="00/00/0000", expDate="00/00/0000", cost = "0"
    ):
        self.entryNum = entryNum
        self.name = name
        self.entryDate = entryDate
        self.expDate = expDate
        self.cost = cost

        self.expired = False
        self.notificationSent = False
        
        self.textRGB = (255, 255, 255)

        self.fontSize = 15
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        
        #self.entryNumText = self.font.render("#" + str(self.entryNum), True, self.textRGB)

        self.entryButton = Buttons(0, 0, 50, 30, 220, 25, 25, "Delete", 10, 0, 0, 0)

        self.editButton = Buttons(0, 0, 50, 30, 100, 100, 100, "Edit", 10, 0, 0, 0)


    #Draws the current entry to the screen
    def showItemInList(self, anchX, anchY, screen):

        today = date.today()
        formattedDate = today.strftime("%m%d%y")

        try:
            decomposedExpirationDate = self.expDate[0] + self.expDate[1] + self.expDate[3] + self.expDate[4] + self.expDate[6] + self.expDate[7]
        except IndexError or TypeError:
            decomposedExpirationDate = 999999

        if (int(formattedDate) - int(decomposedExpirationDate)) > 0:
            self.expired = True
        else:
            self.expired = False
            self.notificationSent = False

        if not self.expired:

            entryBox = pygame.Rect(anchX, anchY, 480, 40)
            pygame.draw.rect(screen, (0, 0, 0), entryBox)

        else:

            if self.notificationSent == False:

                #
                # Notification logic
                #

                self.notificationSent = True

            entryBox = pygame.Rect(anchX, anchY, 480, 40)
            pygame.draw.rect(screen, (255,0,0), entryBox)

        #entryNumTextRect = self.entryNumText.get_rect(centery=entryBox.centery, left=anchX + 15)
        #screen.blit(self.entryNumText, entryNumTextRect)

        nameText = self.font.render(str(self.name), True, self.textRGB)
        nameTextRect = nameText.get_rect(centery=entryBox.centery, left=anchX + 20)
        screen.blit(nameText, nameTextRect)

        
        entryDateText = self.font.render(str(self.entryDate), True, self.textRGB)
        entryDateTextRect = entryDateText.get_rect(centery=entryBox.centery, left=anchX + 100)
        screen.blit(entryDateText, entryDateTextRect)

        expDateText = self.font.render(str(self.expDate), True, self.textRGB)
        expDateTextRect = expDateText.get_rect(centery=entryBox.centery, left=anchX + 200)
        screen.blit(expDateText, expDateTextRect)
        
        costText = self.font.render("$" + str(self.cost), True, self.textRGB)
        costTextRect = costText.get_rect(centery=entryBox.centery, left=anchX + 300)
        screen.blit(costText, costTextRect)

        
        self.entryButton.moveButton(anchX + 420, anchY + 5)
        self.entryButton.isHoveredOver()
        self.entryButton.drawButton(screen)

        self.editButton.moveButton(anchX + 360, anchY + 5)
        self.editButton.isHoveredOver()
        self.editButton.drawButton(screen)
