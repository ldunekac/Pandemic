import pygame
from pygame.locals import *

from View.GUI.window import window

class MenuEntryView:

    def __init__(self, menuEntryItem):
        self.menuEntryItem = menuEntryItem
        self.fontSize = 48
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.windowSize = window.getWindowSize()

    def draw(self):
        self.font.set_bold(self.menuEntryItem.isSelected())
        return self.font.render(self.menuEntryItem.getText(),1, (10,10,10))
    
    def getFontSize(self):
        return self.fontSize