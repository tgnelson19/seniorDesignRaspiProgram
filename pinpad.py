import pygame
from button import Buttons

class Pinpad:
    def __init__(self):
        self.keyboardBackground = pygame.Rect(0, 180, 800, 480)  # Edit background
        self.textBoxBackground = pygame.Rect(200, 100, 400, 60)  # Edit background

        self.textRGB = (0,0,0)
        self.fontSize = 30
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        self.keypadTopLeftX = 200
        self.keypadTopLeftY = 200

        self.keySize = 60
        self.keyFontSize = 15
        self.keySpacing = 10

        self.countOrMonth = "Count = "

        self.SevenKey = Buttons(self.keypadTopLeftX,self.keypadTopLeftY,50,50,100,100,100, "7", self.keyFontSize, 0,0,0)
        self.EightKey = Buttons(self.keypadTopLeftX + self.keySize + self.keySpacing,self.keypadTopLeftY,50,50,100,100,100, "8", self.keyFontSize, 0,0,0)
        self.NineKey = Buttons(self.keypadTopLeftX + self.keySize*2 + self.keySpacing*2,self.keypadTopLeftY,50,50,100,100,100, "9", self.keyFontSize, 0,0,0)
        self.FourKey = Buttons(self.keypadTopLeftX ,self.keypadTopLeftY+ self.keySize + self.keySpacing,50,50,100,100,100, "4", self.keyFontSize, 0,0,0)
        self.FiveKey = Buttons(self.keypadTopLeftX  + self.keySize + self.keySpacing,self.keypadTopLeftY + self.keySize + self.keySpacing,50,50,100,100,100, "5", self.keyFontSize, 0,0,0)
        self.SixKey = Buttons(self.keypadTopLeftX  + self.keySize*2 + self.keySpacing*2,self.keypadTopLeftY + self.keySize + self.keySpacing,50,50,100,100,100, "6", self.keyFontSize, 0,0,0)
        self.OneKey = Buttons(self.keypadTopLeftX,self.keypadTopLeftY + self.keySize*2 + self.keySpacing*2,50,50,100,100,100, "1", self.keyFontSize, 0,0,0)
        self.TwoKey = Buttons(self.keypadTopLeftX + self.keySize + self.keySpacing,self.keypadTopLeftY + self.keySize*2 + self.keySpacing*2,50,50,100,100,100, "2", self.keyFontSize, 0,0,0)
        self.ThreeKey = Buttons(self.keypadTopLeftX  + self.keySize*2 + self.keySpacing*2,self.keypadTopLeftY + self.keySize*2 + self.keySpacing*2,50,50,100,100,100, "3", self.keyFontSize, 0,0,0)
        self.DeleteKey = Buttons(self.keypadTopLeftX,self.keypadTopLeftY + self.keySize*3 + self.keySpacing*3,50,50,190,0,0, "<==", self.keyFontSize, 0,0,0)
        self.ZeroKey = Buttons(self.keypadTopLeftX + self.keySize + self.keySpacing,self.keypadTopLeftY+ self.keySize*3 + self.keySpacing*3,50,50,100,100,100, "0", self.keyFontSize, 0,0,0)
        self.EnterKey = Buttons(self.keypadTopLeftX + self.keySize*2 + self.keySpacing*2,self.keypadTopLeftY+ self.keySize*3 + self.keySpacing*3,50,50,100,100,100, "Enter", self.keyFontSize, 0,0,0)
        self.SlashKey = Buttons(self.keypadTopLeftX + self.keySize*3 + self.keySpacing*3,self.keypadTopLeftY,50,50,100,100,100, "/", self.keyFontSize, 0,0,0)
        self.ClearKey = Buttons(self.keypadTopLeftX + self.keySize*3 + self.keySpacing*3,self.keypadTopLeftY + self.keySize + self.keySpacing,50,50,190,100,100, "Clear", self.keyFontSize, 0,0,0)


        self.keyArray = [self.SevenKey, self.EightKey,self.NineKey,self.FourKey,
                         self.FiveKey,self.SixKey,self.OneKey,self.TwoKey,self.ThreeKey,
                         self.ZeroKey, self.SlashKey]
        
        self.keyNumbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "/"]


    def showKeys(self, screen):

        pygame.draw.rect(screen, (75,75,75), self.keyboardBackground)
        pygame.draw.rect(screen, (255,255,255), self.textBoxBackground)

        for key in self.keyArray:
            key.drawButton(screen)
            key.isHoveredOver()

        self.EnterKey.isHoveredOver()
        self.EnterKey.drawButton(screen)
        self.DeleteKey.isHoveredOver()
        self.DeleteKey.drawButton(screen)
        self.ClearKey.isHoveredOver()
        self.ClearKey.drawButton(screen)


    def runKeyLogic(self, screen, mouseDown, word):

        if self.EnterKey.isClicked(mouseDown):

            if self.countOrMonth == "Count = ":
                self.countOrMonth = "Exp. Date = "
                return "To NumberpadTwo"
            
            else:
                self.countOrMonth = "Count = "
                return "Exiting Editing"
            
        if self.ClearKey.isClicked(mouseDown):
            word = ""
            
        
        if self.DeleteKey.isClicked(mouseDown):
            word = word[:-1]


        for key in self.keyArray:
            if key.isClicked(mouseDown):
                word = word + self.keyNumbers[self.keyArray.index(key)]


        textRender = self.font.render(self.countOrMonth + str(word), True, self.textRGB)
        textRect = textRender.get_rect(center=(self.textBoxBackground.center))
        screen.blit(textRender, textRect)
        
        return word
