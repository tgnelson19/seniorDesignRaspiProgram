import pygame


class Buttons:
    
    """
    This class represents a button in pygame.
    It provides methods to display, move and detect interactions with the button.
    """
        
    #Initializer
    def __init__(self, topLeftX, topLeftY, width, height, R, G, B, text, fontSize, textR, textG, textB):
        """
        Intializes the buton with specified properties.
        """
        # Position of the button
        self.posX = topLeftX
        self.posY = topLeftY

        # Dimentsions of the button
        self.width = width
        self.height = height

        # Rectangle object representing the button's positon and size
        self.buttonRect = pygame.Rect(topLeftX, topLeftY, width, height)
        # Color of the button
        self.buttonRGB = (R, G, B)
        # To prvent multiple click detections for a single click
        self.canBeClickedAgain = True
        # Text attributes for display on the button
        self.textRGB = (textR, textG, textB)
        self.text = text
        self.fontSize = fontSize
        # Font for the text and its rendering
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)
        self.textRender = self.font.render(str(self.text), True, self.textRGB)
        # Positioning the text at the center of the button
        self.textRect = self.textRender.get_rect(
            center=(self.buttonRect.centerx, self.buttonRect.centery)
        )


    #Draws the button to the screen
    def drawButton(self, screen):
        pygame.draw.rect(screen, self.buttonRGB, self.buttonRect)
        screen.blit(self.textRender, self.textRect)

    #Moves the button to a designated x adn y coordinate
    def moveButton(self, x, y):
        self.posX = x
        self.posY = y

        self.buttonRect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.textRect = self.textRender.get_rect(
            center=(self.buttonRect.centerx, self.buttonRect.centery)
        )
        
    def changeColor(self,R,G,B):
        self.buttonRGB = (R,G,B)
        


    #Does an action if the button is hovered over (Mouse only)
    def isHoveredOver(self):
        scaler = 1.05
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mouseX, mouseY):
            leftGap = (self.buttonRect.width * scaler - self.buttonRect.width) / 2
            topGap = (self.buttonRect.height * scaler - self.buttonRect.height) / 2
            self.buttonRect = pygame.Rect(
                self.posX - leftGap,
                self.posY - topGap,
                self.width * scaler,
                self.height * scaler,
            )
        else:
            self.buttonRect = pygame.Rect(self.posX, self.posY, self.width, self.height)


    #Determines if the button has been clicked
    def isClicked(self, mouseDown):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseDown:
            if self.buttonRect.collidepoint(mouseX, mouseY) and self.canBeClickedAgain:
                self.canBeClickedAgain = False
                return True
        else:
            self.canBeClickedAgain = True
            return False
