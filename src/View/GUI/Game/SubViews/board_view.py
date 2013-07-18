import pygame
from pygame.locals import *

from View.GUI.window import window

class BoardView:

    def __init__(self):
        """Initializes the Board View"""
        self.boardImage = pygame.image.load('View/GUI/Pictures/world_map.png')
        self.boardSurface = pygame.Surface(window.getWindowSize())

    def draw(self):
        """ Draws the board"""
        self.boardSurface.blit(pygame.transform.scale(self.boardImage,window.getWindowSize()),(0,0))
        return self.boardSurface.convert()
