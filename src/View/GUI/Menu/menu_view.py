import pygame
from pygame.locals import *


from Menu.menu import Menu
from View.GUI.window import window
from View.GUI.Menu.menu_entry_view import MenuEntryView

class MenuView:

    def __init__(self, menu, position):
        self.menu = menu
        self.position = position
        self.windowSize = window.getWindowSize()
        selectedPicture = pygame.image.load('View/GUI/Pictures/MainMenuPictures/biohazard.png')
        self.font = pygame.font.SysFont(None, 48)
        self.menuEntryViewList = []
        for menuItem in self.menu.getEntries():
            menuEntryView = MenuEntryView(menuItem, selectedPicture)
            self.menuEntryViewList.append(menuEntryView)



    def draw(self):
        newPosition = self.position
        surface = pygame.Surface(self.windowSize, flags = pygame.SRCALPHA)
        for menuItem in self.menuEntryViewList:
            surface.blit(menuItem.draw(),newPosition)
            newPosition = (newPosition[0], newPosition[1] + menuItem.getFontSize())
        return surface



        

