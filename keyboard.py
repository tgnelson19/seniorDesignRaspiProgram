import pygame
from button import Buttons

class Keyboard:
    def __init__(self):
        
        

        self.keyboardBackground = pygame.Rect(0, 180, 800, 480)  # Edit background
        
        self.textBoxBackground = pygame.Rect(200, 100, 400, 60)  # Edit background
        
        self.textRGB = (0,0,0)
        self.fontSize = 30
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)
        

        self.topRowXShift = 20 + 60
        self.topRowYShift = 0 
        self.midRowXShift = 35 + 60
        self.midRowYShift = 60 
        self.botRowXShift = 60 + 60
        self.botRowYShift = 120 

        self.qKey = Buttons (20 + self.topRowXShift,200 + self.topRowYShift,50,50,100,100,100, "Q", 15, 0,0,0)
        self.wKey = Buttons (80+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "W", 15, 0,0,0)
        self.eKey = Buttons (140+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "E", 15, 0,0,0)
        self.rKey = Buttons (200+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "R", 15, 0,0,0)
        self.tKey = Buttons (260+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "T", 15, 0,0,0)
        self.yKey = Buttons (320+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "Y", 15, 0,0,0)
        self.uKey = Buttons (380+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "U", 15, 0,0,0)
        self.iKey = Buttons (440+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "I", 15, 0,0,0)
        self.oKey = Buttons (500+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "O", 15, 0,0,0)
        self.pKey = Buttons (560+ self.topRowXShift,200+ self.topRowYShift,50,50,100,100,100, "P", 15, 0,0,0)

        self.aKey = Buttons (20 + self.midRowXShift,200 + self.midRowYShift,50,50,100,100,100, "A", 15, 0,0,0)
        self.sKey = Buttons (80+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "S", 15, 0,0,0)
        self.dKey = Buttons (140+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "D", 15, 0,0,0)
        self.fKey = Buttons (200+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "F", 15, 0,0,0)
        self.gKey = Buttons (260+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "G", 15, 0,0,0)
        self.hKey = Buttons (320+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "H", 15, 0,0,0)
        self.jKey = Buttons (380+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "J", 15, 0,0,0)
        self.kKey = Buttons (440+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "K", 15, 0,0,0)
        self.lKey = Buttons (500+ self.midRowXShift,200+ self.midRowYShift,50,50,100,100,100, "L", 15, 0,0,0)

        self.zKey = Buttons (20 + self.botRowXShift,200 + self.botRowYShift,50,50,100,100,100, "Z", 15, 0,0,0)
        self.xKey = Buttons (80+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "X", 15, 0,0,0)
        self.cKey = Buttons (140+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "C", 15, 0,0,0)
        self.vKey = Buttons (200+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "V", 15, 0,0,0)
        self.bKey = Buttons (260+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "B", 15, 0,0,0)
        self.nKey = Buttons (320+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "N", 15, 0,0,0)
        self.mKey = Buttons (380+ self.botRowXShift,200+ self.botRowYShift,50,50,100,100,100, "M", 15, 0,0,0)
        
        self.backKey = Buttons (620 + self.topRowXShift,200+ self.topRowYShift,75,50,190,0,0, "<==", 15, 0,0,0)
        
        self.enterKey = Buttons (560 + self.midRowXShift,200+ self.midRowYShift,100,50,0,190,0, "Next", 15, 0,0,0)
        
        self.capsKey = Buttons (-65 + self.midRowXShift,200+ self.midRowYShift,75,50,0,190,0, "Caps", 15, 0,0,0)
        
        self.clearKey = Buttons (440 + self.botRowXShift,200+ self.botRowYShift,75,50,190,0,0, "Clear", 15, 0,0,0)
        
        self.spaceKey = Buttons (130+ self.botRowXShift,200+ self.botRowYShift + 60,200,50,100,100,100, "Space", 15, 0,0,0)

        self.keyArray = [self.qKey, self.wKey, self.eKey, self.rKey, self.tKey,
                         self.yKey, self.uKey, self.iKey, self.oKey, self.pKey,
                         self.aKey,self.sKey,self.dKey,self.fKey,self.gKey,
                         self.hKey, self.jKey,self.kKey,self.lKey,self.zKey,self.xKey,
                         self.cKey,self.vKey,self.bKey,self.nKey,self.mKey, self.spaceKey]
        
        self.functionKeyArray = [self.backKey, self.enterKey, self.capsKey,self.clearKey]
        
        self.lowerCaseArray = ["q", "w", "e", "r", "t", "y", "u", "i","o", "p",
                               "a", "s", "d", "f", "g", "h", "j","k", "l",
                               "z", "x", "c", "v", "b", "n", "m", " "]
        
        self.upperCaseArray = ["Q", "W", "E", "R", "T", "Y", "U", "I","O", "P",
                               "A", "S", "D", "F", "G", "H", "J","K", "L",
                               "Z", "X", "C", "V", "B", "N", "M", " "]
        
        self.isLowerCase = False

    def showKeys(self, screen):

        pygame.draw.rect(screen, (75,75,75), self.keyboardBackground)
        
        pygame.draw.rect(screen, (255,255,255), self.textBoxBackground)

        for key in self.keyArray:
            key.drawButton(screen)
            key.isHoveredOver()
            
        for key in self.functionKeyArray:
            key.drawButton(screen)
            key.isHoveredOver()
    
            
    def runKeyLogic(self, screen, mouseDown, word):
        
        if self.enterKey.isClicked(mouseDown):
            return "To Numberpad"
        
        if self.backKey.isClicked(mouseDown):
            word = word[:-1]
        
        if self.clearKey.isClicked(mouseDown):
            word = ""
            self.isLowerCase = False
            self.capsKey.changeColor(0,190,0)  
        
        if self.capsKey.isClicked(mouseDown):
            if self.isLowerCase == False:
                self.isLowerCase = True
                self.capsKey.changeColor(100,100,100)
            else:
                self.isLowerCase = False
                self.capsKey.changeColor(0,190,0)      
                
        for key in self.keyArray:
            if key.isClicked(mouseDown):
                if self.isLowerCase:
                    word = word + self.lowerCaseArray[self.keyArray.index(key)]
                else:
                    word = word + self.upperCaseArray[self.keyArray.index(key)]
                    self.isLowerCase = True
                    self.capsKey.changeColor(100,100,100)
        
        textRender = self.font.render(str(word), True, self.textRGB)
        textRect = textRender.get_rect(center=(self.textBoxBackground.center))
        screen.blit(textRender, textRect)
        
        return word
            
