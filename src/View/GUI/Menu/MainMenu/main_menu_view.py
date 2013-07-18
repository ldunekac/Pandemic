import pygame
from pygame.locals import *
from View.GUI.window import window
from View.GUI.Menu.menu_view import MenuView

class MainMenuView:

    def __init__(self, menu):
        imagePath = 'View/GUI/Pictures/MainMenuPictures/pandemic_logo.png'
        self.windowSize = window.getWindowSize()
        self.factor = (.1,.1)
        self.menuPicture = pygame.image.load(imagePath).convert()
        self.menuPosition = tuple([a*b for a,b in zip(self.windowSize,self.factor)])
        self.menuView = MenuView(menu, self.menuPosition)

    def draw(self):
        surface = pygame.Surface(self.windowSize)
        surface.blit(pygame.transform.scale(self.menuPicture, self.windowSize),(0,0))
        surface.blit(self.menuView.draw(),(0,0))
        return surface

    def selectEntry(self, position):
        self.menuView.selectEnty(position)

    def executeIfSelected(self,position):
        self.menuView.executeIfSelected(position)