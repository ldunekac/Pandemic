import pygame
from pygame.locals import *

from View.GUI.window import window

class MenuEntryView:

    def __init__(self, menuEntryItem, selectedPicture):
        self.menuEntryItem = menuEntryItem
        self.selectedPicture = selectedPicture
        self.fontSize = 48
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.windowSize = window.getWindowSize()

    def draw(self):
        surface = pygame.Surface(self.windowSize, flags = pygame.SRCALPHA)
        transformedImage = pygame.transform.scale(self.selectedPicture,(self.fontSize,self.fontSize))

        if self.menuEntryItem.isSelected():
            surface.blit(transformedImage,(0,0))
        
        text = self.font.render(self.menuEntryItem.getText(),1, (10,10,10))
        textPosition = text.get_rect(left = self.fontSize,centery = transformedImage.get_rect().height/2)
        surface.blit(text, textPosition)
        return surface
    
    def getFontSize(self):
        return self.fontSize