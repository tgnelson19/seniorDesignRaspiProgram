import pygame
from background import Background
from button import Buttons
from itemEntry import ItemEntry
import json
import firebase_admin
from firebase_admin import db
import json

class Variables():

    def __init__(self):
        
        pygame.init() #Initializes a window
        
        self.sW, self.sH = 800,480 #Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock() #Main time keeper

        self.done = False #Determines if the game is over or not
        self.mouseDown = False
        
        self.fontSize = 30
        self.font = pygame.font.Font('media/coolveticarg.otf', self.fontSize)
        
        self.screen = pygame.display.set_mode([self.sW, self.sH]) #Makes a screen that's that wide
        
        self.background = Background()
        
        self.addExampleEntry = Buttons(580,60,160,100,100,100,100,"Add Entry", 20, 255,255,255)
        
        self.syncButton = Buttons(580,180,160,50,100,100,100,"Sync Data", 20, 255,255,255)

        self.buttonList = [self.addExampleEntry, self.syncButton]
        
        self.entryList = []
        
        self.highestEntryNum = 0
        
        self.entryJustDeleted = False
        
        cred_obj = firebase_admin.credentials.Certificate('seniordesign-9342c-firebase-adminsdk-649ck-c9a18f8baa.json')
        default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://seniordesign-9342c-default-rtdb.firebaseio.com/'})
        
        with open('entries.json') as f:
            self.entriesJSON = json.load(f)
            
        for item in self.entriesJSON:
            
            if int(item["EntryNum"]) > self.highestEntryNum:
                self.highestEntryNum = int(item["EntryNum"])
            
            self.entryList.append(ItemEntry(
                item["EntryNum"],
                item["Name"],
                item["Quantity"],
                item["Expiration"]
            ))
            
        
 
 
    def makeNewEntry(self):
        self.highestEntryNum = self.highestEntryNum + 1
        newEntry = ItemEntry(str(self.highestEntryNum))
        self.entryList.append(newEntry)
        
        self.entriesJSON.append(
            
            {
                "EntryNum" : newEntry.entryNum,
                "Name": newEntry.name,
                "Quantity": newEntry.quantity,
                "Expiration": newEntry.expDate
            })
        
        with open('entries.json', 'w') as f:
            json.dump(self.entriesJSON, f, indent=2)
        
        
    def syncToDatabase(self):
        
        ref = db.reference('/')

        with open("entries.json", "r") as f:
            file_contents = json.load(f)
        ref.set(file_contents)
        
        
        
    def doAnUpdate(self):
        
        self.background.drawMainBackground(self.screen) # Draws the background first of everything
        self.eventHandler() # Updates with any potential user interaction
        
        if len(self.buttonList) != 0:
            
            for button in self.buttonList:
                button.drawButton(self.screen)
        
        
        if(self.addExampleEntry.isClicked(self.mouseDown)):
            self.makeNewEntry()
            
        if(self.syncButton.isClicked(self.mouseDown)):
            self.syncToDatabase()
            
            
        if not self.mouseDown:
            self.entryJustDeleted = False    
            
        for entry in self.entryList:
            if entry.entryButton.isClicked(self.mouseDown) and not self.entryJustDeleted:
                
                for jEntry in self.entriesJSON:
                    if int(jEntry["EntryNum"]) == int(entry.entryNum):
                        self.entriesJSON.remove(jEntry)
                        
                with open('entries.json', 'w') as f:
                    json.dump(self.entriesJSON, f, indent=2)
                
                self.entryList.remove(entry)
                del entry
                
                self.entryJustDeleted = True
            
            
        if len(self.entryList) != 0:
            
            anchX = 60
            anchY = 60
            
            for entry in self.entryList:
                entry.showItemInList(anchX, anchY, self.screen)
                anchY += 60
        

        
        self.finishPaint() # Paints whatever is desired to be painted on the screen

    def eventHandler(self):

        self.clock.tick(30) #Keeps program to only 30 frames per second

        for event in pygame.event.get(): #Main event handler

            if event.type == pygame.QUIT: self.done = True #Close the entire program

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: self.done = True
                
            if event.type == pygame.MOUSEBUTTONDOWN: self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP: self.mouseDown = False

    def finishPaint(self):

        pygame.display.flip() #Displays currently drawn frame
        self.screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
        
    
        
