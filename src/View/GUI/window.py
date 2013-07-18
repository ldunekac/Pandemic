
""" 
This is a single class that houses the window for the game.
there is only one Instance of this class and it initializes the gui
along with despalying anything graphical.
"""
import pygame
from pygame.locals import *

class Window:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((0,0), FULLSCREEN)
        self.windowSize = self.window.get_size()

    def draw(self, surface):
        self.window.blit(surface,(0,0))
        pygame.display.flip()

    def getWindowSize(self):
        return self.windowSize

window = Window()