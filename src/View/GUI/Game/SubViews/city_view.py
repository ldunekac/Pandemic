import pygame
from pygame.locals import *
from View.GUI.window import window

class CityView:

    def __init__(self, cityList):
        """ Initializes the city view"""
        self.cityList = cityList
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)

        self.fontSize = 16
        self.font = pygame.font.SysFont(None,self.fontSize)
        self.radious = 10
        self.fontBuffer = 5

    def draw(self):
        surface = pygame.Surface(window.getWindowSize(),  pygame.SRCALPHA)
        for city in self.cityList:
            cityColor = city.getDisease().getColor()
            cityLocation = self.getCord(city.getMapLocation())
            pygame.draw.circle(surface,cityColor,cityLocation,self.radious)
            render = self.font.render(city.getName(),1, (255,255,255))
            renderPosition = render.get_rect(centerx = cityLocation[0], centery = cityLocation[1] + self.radious + self.fontBuffer )
            surface.blit(render,renderPosition)
        return surface

    def getCord(self, position):
        return tuple([int(a*b) for a,b in zip(self.scailingFactor,position)])