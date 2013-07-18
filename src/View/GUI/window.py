
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