




class Variables:
    def __init__(self):

        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom
        self.model.eval()

        pygame.init()  # Initializes a window

        pygame.display.set_caption("Raspberry Pi Software")

        self.sW, self.sH = (800,480)  # Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock()  # Main time keeper

        self.done = False  # Determines if the game is over or not
        self.mouseDown = False
        self.justUpdated = False

        self.fontSize = 30
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        self.screen = pygame.display.set_mode([self.sW, self.sH], pygame.NOFRAME)  # Makes a screen that's that wide

        pygame.camera.init()

        cameras = pygame.camera.list_cameras()

        self.webcam = pygame.camera.Camera(cameras[0], (480, 320))

        self.webcam.start()

        self.webcam.set_controls(hflip = True, vflip = False)

        self.snapshot = pygame.surface.Surface((480,320), 0, self.screen)

        self.background = Background()


        #button makers (topleft x, toplefty, width, hieght, r ,g ,b, text string, font size, Tr, Tg, TB )
        
        self.addExampleEntry = Buttons(580, 40, 180, 100, 100, 100, 100, "Add Entry", 25, 255, 255, 255)

        self.syncButton = Buttons(580, 160, 180, 50, 100, 100, 100, "Sync Data", 25, 255, 255, 255)

        self.deleteallButton = Buttons(580, 230, 180, 50, 100,0,0, "Delete All", 25, 255, 255, 255)
        
        self.objectDetectButton = Buttons(10, 105, 180, 50, 100, 100, 100, "Object Detect", 25, 255, 255, 255)

        self.exitButton = Buttons(580, 400, 180, 40, 100,0,0, "Exit App", 25, 255, 255, 255)
        
        
        
        
        
        #end of buttion maker 


        #button list
        self.buttonList = [self.addExampleEntry, self.syncButton, self.exitButton, self.deleteallButton]

        self.entryList = []

        self.highestEntryNum = 0

        self.entryJustDeleted = False

        self.currState = "Home"
        
        self.showPic = False

        self.currItemEdited = 0

        self.pinpad = Pinpad()

        self.keyboard = Keyboard()

        self.firstMouseDown = False

        self.firstMousePos = 0

        self.distFromFirstMousePos = 0

        self.overallMouseDistance = 0

        self.editBackgroundBig = pygame.Rect(0, 0, 800, 480)  # Edit background
        
        self.blockEdits = pygame.Rect(520, 50, 110, 40)  # Edit background

        self.backgroundOfCamera = pygame.Rect(150, 50, 520, 400)  # Edit background of camera

        self.keypadAcceptButton = Buttons(700, 20,80,40, 0, 255, 0, "Save", 25, 0,0,0)

        miniXOffset = 100
        miniYOffset = -40

        self.editNameButton = Buttons(50 + miniXOffset, 50 + miniYOffset, 100, 30, 255,255,0, "Edit Name", 15, 0, 0, 0)
        self.editEntryDateButton = Buttons(170+ miniXOffset, 50 + miniYOffset, 100, 30, 255,255,0, "Edit Entry", 15, 0, 0, 0)
        self.editExpirationButton = Buttons(290+ miniXOffset, 50 + miniYOffset, 100, 30, 255,255,0, "Edit Expiration", 15, 0, 0, 0)
        self.editCostButton = Buttons(410+ miniXOffset, 50 + miniYOffset, 100, 30, 255,255,0, "Edit Cost", 15, 0, 0, 0)
        

        self.takePictureButton = Buttons(275, 400,250,30, 20,20,20, "Take Picture", 25, 255,255,255)

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
                    item["EntryNum"], item["Name"], item["EntryDate"], item["ExpirationDate"], item["Cost"]
                )
            )


    #Handles the creation of a new default entry (More functionality to be added)
    
    def makeNewEntry(self):

        today = date.today()
        formattedDate = today.strftime("%m/%d/%y")

        self.highestEntryNum = self.highestEntryNum + 1
        newEntry = ItemEntry(str(self.highestEntryNum),"Default", str(formattedDate), str(formattedDate))
        self.entryList.append(newEntry)

        self.entriesJSON.append(
            {
                "EntryNum": newEntry.entryNum,
                "Name": newEntry.name,
                "EntryDate": newEntry.entryDate,
                "ExpirationDate": newEntry.expDate,
                "Cost": newEntry.cost
            }
        )

        with open("entries.json", "w") as f:
            json.dump(self.entriesJSON, f, indent=2)


        self.currItemEdited = newEntry
        self.currState = "Edit Name"

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

            self.justUpdated = False

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)
            
            if not self.currItemEdited.expired:
                pygame.draw.rect(self.screen, (0,0,0), self.blockEdits)
            else:
                pygame.draw.rect(self.screen, (255,0,0), self.blockEdits)

            self.keyboard.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            self.objectDetectButton.isHoveredOver()
            self.objectDetectButton.drawButton(self.screen)
            
            
            temp = self.keyboard.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.name)
            
            if temp == "To Numberpad":
                self.currState = "Edit Entry"
            else:
                self.currItemEdited.name = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

            self.editEntryDateButton.isHoveredOver()
            self.editEntryDateButton.drawButton(self.screen)
            self.editExpirationButton.isHoveredOver()
            self.editExpirationButton.drawButton(self.screen)

            self.editCostButton.isHoveredOver()
            self.editCostButton.drawButton(self.screen)
            if self.editCostButton.isClicked(self.mouseDown):
                self.currState = "Edit Cost"

            if self.editEntryDateButton.isClicked(self.mouseDown):
                self.currState = "Edit Entry"
            if self.editExpirationButton.isClicked(self.mouseDown):
                self.currState = "Edit Exp"

            if self.objectDetectButton.isClicked(self.mouseDown):
                    self.showPic = True
                    
            if self.showPic == True:
                pygame.draw.rect(self.screen, (50,50,50), self.backgroundOfCamera)
                self.takePictureButton.isHoveredOver()
                self.takePictureButton.drawButton(self.screen)
                
                if self.webcam.query_image():
                    self.snapshot = self.webcam.get_image(self.snapshot)

                self.screen.blit(self.snapshot, (170, 70))

                if(self.takePictureButton.isClicked(self.mouseDown)):
                    pygame.image.save(self.snapshot, "yolov5/data/images/screenie.png")
                    tempName = self.model("yolov5/data/images/screenie.png")

                    pandaData = tempName.pandas().xyxy[0]
                    names = pandaData['name']


                    for i in range(len(names)):
                        if not(names[i] == "person" or names[i] == "persons"):
                            self.currItemEdited.name = names[i].capitalize()
                            break
                        else:
                            self.currItemEdited.name = "ERR: No Obj Fnd"

                    print(tempName)
                    
                    self.showPic = False
            

        if self.currState == "Edit Entry":

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            if not self.currItemEdited.expired:
                pygame.draw.rect(self.screen, (0,0,0), self.blockEdits)
            else:
                pygame.draw.rect(self.screen, (255,0,0), self.blockEdits)

            self.pinpad.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            temp = self.pinpad.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.entryDate, "Entry Date = ")
            
            if temp == "To NumberpadTwo":
                self.currState = "Edit Exp"
            else:
                self.currItemEdited.entryDate = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

            self.editNameButton.isHoveredOver()
            self.editNameButton.drawButton(self.screen)
            self.editExpirationButton.isHoveredOver()
            self.editExpirationButton.drawButton(self.screen)

            if self.editNameButton.isClicked(self.mouseDown):
                self.currState = "Edit Name"
            if self.editExpirationButton.isClicked(self.mouseDown):
                self.currState = "Edit Exp"

            self.editCostButton.isHoveredOver()
            self.editCostButton.drawButton(self.screen)
            if self.editCostButton.isClicked(self.mouseDown):
                self.currState = "Edit Cost"

        if self.currState == "Edit Exp":

            

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            if not self.currItemEdited.expired:
                pygame.draw.rect(self.screen, (0,0,0), self.blockEdits)
            else:
                pygame.draw.rect(self.screen, (255,0,0), self.blockEdits)

            self.pinpad.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            temp = self.pinpad.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.expDate, "Exp. Date = ")
            
            if temp == "Exiting Editing":
                self.currState = "Home"
            else:
                self.currItemEdited.expDate = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

            self.editEntryDateButton.drawButton(self.screen)
            self.editEntryDateButton.isHoveredOver()
            if self.editEntryDateButton.isClicked(self.mouseDown):
                self.currState = "Edit Entry"

            self.editNameButton.drawButton(self.screen)
            self.editNameButton.isHoveredOver()
            if self.editNameButton.isClicked(self.mouseDown):
                self.currState = "Edit Name"

            self.editCostButton.isHoveredOver()
            self.editCostButton.drawButton(self.screen)
            if self.editCostButton.isClicked(self.mouseDown):
                self.currState = "Edit Cost"

        if self.currState == "Edit Cost":

            

            pygame.draw.rect(self.screen, (50,50,50), self.editBackgroundBig)

            self.currItemEdited.showItemInList(160, 50, self.screen)

            if not self.currItemEdited.expired:
                pygame.draw.rect(self.screen, (0,0,0), self.blockEdits)
            else:
                pygame.draw.rect(self.screen, (255,0,0), self.blockEdits)

            self.pinpad.showKeys(self.screen)

            self.keypadAcceptButton.drawButton(self.screen)

            temp = self.pinpad.runKeyLogic(self.screen, self.mouseDown, self.currItemEdited.cost, "Cost = ")
            
            if temp == "Exiting Editing":
                self.currState = "Home"
            else:
                self.currItemEdited.cost = temp
            
            self.keypadAcceptButton.isHoveredOver()
            if self.keypadAcceptButton.isClicked(self.mouseDown):
                self.currState = "Home"

            self.editEntryDateButton.drawButton(self.screen)
            self.editEntryDateButton.isHoveredOver()
            if self.editEntryDateButton.isClicked(self.mouseDown):
                self.currState = "Edit Entry"

            self.editNameButton.drawButton(self.screen)
            self.editNameButton.isHoveredOver()
            if self.editNameButton.isClicked(self.mouseDown):
                self.currState = "Edit Name"


            self.editExpirationButton.isHoveredOver()
            self.editExpirationButton.drawButton(self.screen)
            if self.editExpirationButton.isClicked(self.mouseDown):
                self.currState = "Edit Exp"


        if self.currState == "Home":

            if not self.justUpdated:
                self.justUpdated = True
                self.entriesJSON.clear()
                for entry in self.entryList:
                    self.entriesJSON.append(
                    {
                        "EntryNum": entry.entryNum,
                        "Name": entry.name,
                        "EntryDate": entry.entryDate,
                        "ExpirationDate": entry.expDate,
                        "Cost": entry.cost
                    }
                )
                with open("entries.json", "w") as f:
                    json.dump(self.entriesJSON, f, indent=2)



            self.background.drawMainBackground(self.screen)  # Draws the background first of everything

            if len(self.buttonList) != 0:

                for button in self.buttonList:
                    button.isHoveredOver()
                    button.drawButton(self.screen)

            if self.exitButton.isClicked(self.mouseDown):
                self.done = True
                
            if self.addExampleEntry.isClicked(self.mouseDown):
                self.makeNewEntry()
            
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

            if self.mouseDown:
                mouseX, mouseY = pygame.mouse.get_pos()
                if not self.firstMouseDown:
                    self.firstMousePos = mouseY
                    self.firstMouseDown = True

                if (self.overallMouseDistance + mouseY - self.firstMousePos < 0 ) and (mouseX < 520):
                    self.distFromFirstMousePos = self.overallMouseDistance + mouseY - self.firstMousePos
            else:
                self.firstMouseDown = False
                self.overallMouseDistance = self.distFromFirstMousePos
                
            



            if len(self.entryList) != 0:
                anchX = 40
                anchY = 80 + self.distFromFirstMousePos

                for entry in self.entryList:
                    entry.showItemInList(anchX, anchY, self.screen)
                    anchY += 60

            self.background.drawTopLevel(self.screen)
                    

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
        pygame.display.flip()  # Displays currently drawn frame in UI
        self.screen.fill(pygame.Color(0, 0, 0))  # Clears screen with a black color