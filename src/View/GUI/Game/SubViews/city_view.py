import pygame
from pygame.locals import *
from View.GUI.window import window
from View.GUI.Helper.label import Label

class CityView:

    def __init__(self, cityList):
        """ Initializes the city view"""
        self.cityList = cityList
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)

        self.fontSize = 16
        self.radious = 10
        self.fontBuffer = 5

    def draw(self):
        surface = pygame.Surface(window.getWindowSize(),  pygame.SRCALPHA)
        for city in self.cityList:
            cityColor = city.getDisease().getColor()
            cityLocation = self.getCord(city.getMapLocation())
            pygame.draw.circle(surface,cityColor,cityLocation,self.radious)
            label = Label(city.getName(), self.fontSize,(0,0),(255,255,255))
            renderPosition = (cityLocation[0] - label.getWidth()/2, cityLocation[1] + self.radious + self.fontBuffer)
            surface.blit(label.draw(),renderPosition)
        return surface

    def getCord(self, position):
        return tuple([int(a*b) for a,b in zip(self.scailingFactor,position)])