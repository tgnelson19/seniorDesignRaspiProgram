import pygame
from background import Background
from button import Buttons
from itemEntry import ItemEntry
import json
import firebase_admin
from firebase_admin import db
import json
from datetime import date
from keyboard import Keyboard
from pinpad import Pinpad




class Variables:
    def __init__(self):
        pygame.init()  # Initializes a window

        self.sW, self.sH = (800,480)  # Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock()  # Main time keeper

        self.done = False  # Determines if the game is over or not
        self.mouseDown = False

        self.fontSize = 30
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        self.screen = pygame.display.set_mode([self.sW, self.sH])  # Makes a screen that's that wide

        self.background = Background()


        #button makers (topleft x, toplefty, width, hieght, r ,g ,b, text string, font size, Tr, Tg, TB )
        
        self.addExampleEntry = Buttons(580, 40, 180, 100, 100, 100, 100, "Add Entry", 25, 255, 255, 255)

        self.syncButton = Buttons(580, 160, 180, 50, 100, 100, 100, "Sync Data", 25, 255, 255, 255)

        self.exitButton = Buttons(580, 400, 180, 40, 100,0,0, "Exit App", 25, 255, 255, 255)
        
        self.deleteallButton = Buttons(580, 230, 180, 40, 100,0,0, "Delete All", 25, 255, 255, 255)
        
        
        
        #end of buttion maker 


        #button list
        self.buttonList = [self.addExampleEntry, self.syncButton, self.exitButton, self.deleteallButton]

        self.entryList = []

        self.highestEntryNum = 0

        self.entryJustDeleted = False

        self.currState = "Home"

        self.currItemEdited = 0

        self.pinpad = Pinpad()

        self.keyboard = Keyboard()

        self.editBackgroundBig = pygame.Rect(0, 0, 800, 480)  # Edit background

        self.keypadAcceptButton = Buttons(700, 20,80,40, 0, 255, 0, "Save", 25, 0,0,0)

        #
        #
        #Put Credentials here for firebase
        #
        #
        #

        #Loads in current saved JSON to the program

        with open("entries.json") as f:
            self.entriesJSON = json.load(f)

        for item in self.entriesJSON:
            if int(item["EntryNum"]) > self.highestEntryNum:
                self.highestEntryNum = int(item["EntryNum"])

            self.entryList.append(
                ItemEntry(
                    item["EntryNum"], item["Name"], item["Quantity"], item["Expiration"]
                )
            )


    #Handles the creation of a new default entry (More functionality to be added)
    
    def makeNewEntry(self):

        today = date.today()
        formattedDate = today.strftime("%m/%d/%y")

        self.highestEntryNum = self.highestEntryNum + 1
        newEntry = ItemEntry(str(self.highestEntryNum),"Default", "0", str(formattedDate))
        self.entryList.append(newEntry)

        self.entriesJSON.append(
            {
                "EntryNum": newEntry.entryNum,
                "Name": newEntry.name,
                "Quantity": newEntry.quantity,
                "Expiration": newEntry.expDate,
            }
        )

        with open("entries.json", "w") as f:
            json.dump(self.entriesJSON, f, indent=2)

    #
    #
    #
    #Syncs current stored data to the database
    #when uncommented
    #
    #

    #def syncToDatabase(self):
    #    ref = db.reference("/")
    #
    #   with open("entries.json", "r") as f:
    #       file_contents = json.load(f)
    #   ref.set(file_contents)

    #Updates the program (Done once per tick)




    def doAnUpdate(self):

        self.finishPaint()  # Paints whatever is desired from last frame on the screen

        self.eventHandler()  # Updates with any potential user interaction

        if self.currState == "Edit Name":

            
            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            self.keyboard.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)
            
            
            temp = self.keyboard.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.name)
            
            if temp == "To Numberpad":
                self.currState = "Edit Count"
            else:
                self.currItemEdited.name = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

        if self.currState == "Edit Count":

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            self.pinpad.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            temp = self.pinpad.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.quantity)
            
            if temp == "To NumberpadTwo":
                self.currState = "Edit Date"
            else:
                self.currItemEdited.quantity = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

        if self.currState == "Edit Date":

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            self.pinpad.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            temp = self.pinpad.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.expDate)
            
            if temp == "Exiting Editing":
                self.currState = "Home"
            else:
                self.currItemEdited.expDate = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"


        if self.currState == "Home":

            self.background.drawMainBackground(self.screen)  # Draws the background first of everything

            if len(self.buttonList) != 0:

                for button in self.buttonList:
                    button.isHoveredOver()
                    button.drawButton(self.screen)

            if self.addExampleEntry.isClicked(self.mouseDown):
                self.makeNewEntry()

            if self.exitButton.isClicked(self.mouseDown):
                self.done = True
                
            if self.deleteallButton.isClicked(self.mouseDown):
                self.entryList.clear()
                with open("entries.json", "w") as f:
                    json.dump([], f, indent=2)
                self.entriesJSON.clear()

            #if self.syncButton.isClicked(self.mouseDown):
                #self.syncToDatabase()

            if not self.mouseDown:
                self.entryJustDeleted = False

            for entry in self.entryList:
                entry.editButton.isHoveredOver()
                entry.entryButton.isHoveredOver()

                if (entry.editButton.isClicked(self.mouseDown)):

                    self.currState = "Edit Name"
                    self.currItemEdited = entry

                if (
                    entry.entryButton.isClicked(self.mouseDown)
                    and not self.entryJustDeleted
                ):
                    for jEntry in self.entriesJSON:
                        if int(jEntry["EntryNum"]) == int(entry.entryNum):
                            self.entriesJSON.remove(jEntry)

                    with open("entries.json", "w") as f:
                        json.dump(self.entriesJSON, f, indent=2)

                    self.entryList.remove(entry)
                    del entry

                    self.entryJustDeleted = True

            if len(self.entryList) != 0:
                anchX = 40
                anchY = 40

                for entry in self.entryList:
                    entry.showItemInList(anchX, anchY, self.screen)
                    anchY += 60




    #Generates handler variables for event tracking

    def eventHandler(self):
        self.clock.tick(30)  # Keeps program to only 30 frames per second

        for event in pygame.event.get():  # Main event handler
            if event.type == pygame.QUIT:
                self.done = True  # Close the entire program

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseDown = False

    #Displays current generated frame to the screen

    def finishPaint(self):
        pygame.display.flip()  # Displays currently drawn frame
        self.screen.fill(pygame.Color(0, 0, 0))  # Clears screen with a black color
