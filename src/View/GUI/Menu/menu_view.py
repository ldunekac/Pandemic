import pygame
from pygame.locals import *


from Menu.menu import Menu
from View.GUI.window import window

class MenuView:

    def __init__(self, menu, position):
        self.menu = menu
        self.position = position
        self.windowSize = window.getWindowSize()
        self.font = pygame.font.SysFont(None, 48)

    def draw(self):
        newPosition = self.position
        surface = pygame.Surface(self.windowSize, flags = pygame.SRCALPHA)
        for menuItem in self.menu.getEntryText():
            text = self.font.render(menuItem,1, (10,10,10))
            surface.blit(text,newPosition)
            textRect = text.get_rect()
            textSize = (textRect.width, textRect.height)
            newPosition = (self.position[0], self.position[1] + textSize[1])
        return surface



        

