import pygame
from pygame.locals import *

from View.GUI.window import window

class MenuEntryView:

    def __init__(self, menuEntryItem, selectedPicture, position):
        self.position = position
        self.menuEntryItem = menuEntryItem
        self.selectedPicture = selectedPicture
        self.fontSize = 48
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.windowSize = window.getWindowSize()
        self.transformImage()
        self.set_rect()
        

    def draw(self):
        self.set_rend()
        
        surface = pygame.Surface((self.fontSize + self.rend.get_rect().width + 100,self.fontSize), flags = pygame.SRCALPHA)
        

        if self.menuEntryItem.isSelected():
            surface.blit(self.transformImage,(0,0))
        
        surface.blit(self.rend, self.textPosition)
        return surface

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.textPosition = self.rend.get_rect(left = self.fontSize,centery = self.transformImage.get_rect().height/2)
        self.rect.topleft = (self.position[0] + self.fontSize, self.position[1])
        
    def set_rend(self):
        self.rend = self.font.render(self.menuEntryItem.getText(),1, (10,10,10))
        
    def transformImage(self):
        self.transformImage = pygame.transform.scale(self.selectedPicture,(self.fontSize,self.fontSize))

    def getFontSize(self):
        return self.fontSize

    def selectIfMouseEntered(self, mousePosition):
        if self.rect.collidepoint(mousePosition):
            self.menuEntryItem.select()

    def executeIfSelected(self, mousePosition):
        if self.rect.collidepoint(mousePosition):
            self.menuEntryItem.run()





