import pygame
from button import Buttons


class ItemEntry:
    """
    A class to reprpresent individual item entries.
    Each entry consists of details like its name, quantity, expiration date,
    and associated action buttons like "Edit" and "Delete".
    """
    
    #Initializer
    #Initialize the item entry with the given attributes.
    def __init__(
        self, entryNum="0", name="Default", quantity="0", expDate="00/00/0000"):
        self.entryNum = entryNum   #entryNum (str): The entry's number.
        self.name = name           #name (str): The name of the item.
        self.expDate = expDate     #expDate (str): Expiration date of the item.
        self.quantity = quantity   #quantity (str): Quantity of the item.

        # Text color in RGB format. Set to white by default.
        self.textRGB = (255, 255, 255)
        # Set the font and size for displaying the item's details.
        self.fontSize = 15
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        # Initalize action buttons associated with the item entry
        #self.entryNumText = self.font.render("#" + str(self.entryNum), True, self.textRGB)
        self.entryButton = Buttons(0, 0, 50, 30, 220, 25, 25, "Delete", 10, 0, 0, 0)
        self.editButton = Buttons(0, 0, 50, 30, 100, 100, 100, "Edit", 10, 0, 0, 0)


    #Draws the current entry to the screen
    def showItemInList(self, anchX, anchY, screen):
        """
        Draw the item enty and its associated details/buttons o the screen.
        Parameters:
        - anchX (int): X-coordinate for the top-left corner of the entry's
        - anchY (int): Y-coordinate for the top-left corner of the entry's
        - screen (pygame.Surface): The screen where the enty will be drawn.
        """

        # Draw a black background box for the item entry.
        entryBox = pygame.Rect(anchX, anchY, 480, 40)
        pygame.draw.rect(screen, (0, 0, 0), entryBox)

        #entryNumTextRect = self.entryNumText.get_rect(centery=entryBox.centery, left=anchX + 15)
        #screen.blit(self.entryNumText, entryNumTextRect)

        # Render and draw the name of the item.
        nameText = self.font.render(str(self.name), True, self.textRGB)
        nameTextRect = nameText.get_rect(centery=entryBox.centery, left=anchX + 20)
        screen.blit(nameText, nameTextRect)

        # Render and draw the quantity of the item.
        quantityText = self.font.render("Count: " + str(self.quantity), True, self.textRGB)
        quantityTextRect = quantityText.get_rect(centery=entryBox.centery, left=anchX + 130)
        screen.blit(quantityText, quantityTextRect)

        # Render and draw the expiration date of the item.
        expDateText = self.font.render("Exp: " + str(self.expDate), True, self.textRGB)
        expDateTextRect = expDateText.get_rect(centery=entryBox.centery, left=anchX + 250)
        screen.blit(expDateText, expDateTextRect)

        # Position the "Delete" button and draw it.
        self.entryButton.moveButton(anchX + 420, anchY + 5)
        self.entryButton.drawButton(screen)

        # Position the "Edit" button and draw it.
        self.editButton.moveButton(anchX + 360, anchY + 5)
        self.editButton.drawButton(screen)
