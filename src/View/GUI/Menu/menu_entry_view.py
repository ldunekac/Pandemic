import pygame
from pygame.locals import *
from View.GUI.Helper.label import Label
from View.GUI.window import window

class MenuEntryView:

    def __init__(self, menuEntryItem, selectedPicture, position):
        self.position = position
        self.menuEntryItem = menuEntryItem
        self.textOffset = 48
        self.label = Label(menuEntryItem.getText(), 48, (position[0] + self.textOffset, position[1]))
        self.selectedPicture = selectedPicture
        self.windowSize = window.getWindowSize()
        self.transformImage()

    def draw(self):
        surface = pygame.Surface((self.label.getFontSize() + self.label.getWidth() + 100,self.label.getHeight()), flags = pygame.SRCALPHA)
        
        if self.menuEntryItem.isSelected():
            surface.blit(self.transformImage,(0,0))
        surface.blit(self.label.draw(), (self.textOffset,0))
        return surface
        
    def transformImage(self):
        self.transformImage = pygame.transform.scale(self.selectedPicture,(self.label.getFontSize(),self.label.getHeight()))

    def getFontSize(self):
        return self.label.getFontSize()

    def selectIfMouseEntered(self, mousePosition):
        if self.label.mouseOnText(mousePosition):
            self.menuEntryItem.select()

    def executeIfSelected(self, mousePosition):
        if self.label.mouseOnText(mousePosition):
            self.menuEntryItem.run()





