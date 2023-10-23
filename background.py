import pygame

class Background:
    """
    This class repesents the background structure of a user interface in pygame.
    It defines the main background and two frames on the left and right.
    """
    def __init__(self):
        """
        Initializes the background sturcuture with its components.
        """
        #self.bigBackBackground = pygame.Rect(0, 0, 800, 480)  # Background Color Block
        self.frontUIBackground = pygame.Rect(0, 0, 800, 480)  # Foreground Background Color Block
        self.leftUIFrame = pygame.Rect(20, 20, 520, 440)  # The left UI frame
        self.rightUIFrame = pygame.Rect(560, 20, 220, 440)  # The right UI frame
        

    def drawMainBackground(self, screen):
        """
        Draws the background components on the given screen.
        """
       # pygame.draw.rect(screen, (40, 40, 40), self.bigBackBackground)
        pygame.draw.rect(screen, (255, 0, 255), self.frontUIBackground)
        #pygame.draw.rect(screen, (200, 200, 200), self.leftUIFrame) # light Gray
        #pygame.draw.rect(screen, (200, 200, 200), self.rightUIFrame)
        #change the left and right frames color form light gray to Teal
        pygame.draw.rect(screen, (0, 128, 128), self.leftUIFrame)
        pygame.draw.rect(screen, (0, 128, 128), self.rightUIFrame)