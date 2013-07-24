import pygame
from pygame.locals import *

from View.GUI.window import window
from View.GUI.Game.SubViews.line_view import LineView
from View.GUI.Game.SubViews.city_view import CityView

class BoardView:

    def __init__(self, cityList):
        """Initializes the Board View"""
        self.cityList = cityList
        self.boardImage = pygame.image.load('View/GUI/Pictures/world_map.png')
        self.boardSurface = pygame.Surface(window.getWindowSize())
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)
        self.lineView = LineView(self.cityList)
        self.cityView = CityView(self.cityList)

        self.staticSurface = None 
        self.createStaticSurface()

    def draw(self):
        """ Draws the board"""
        self.boardSurface.blit(self.staticSurface,(0,0))
        return self.boardSurface.convert()

    def createStaticSurface(self):
        # Create Surface
        self.staticSurface = pygame.Surface(window.getWindowSize())
        # Add background
        self.staticSurface.blit(pygame.transform.scale(self.boardImage,window.getWindowSize()),(0,0))
        # add lines to cities
        self.staticSurface.blit(self.lineView.draw(), (0,0))
        # add cities
        self.staticSurface.blit(self.cityView.draw(), (0,0))

    def getCord(self, position):
        return tuple([int(a*b) for a,b in zip(self.scailingFactor,position)])

