import pygame
from pygame.locals import *

class PlayerView:

    def __init__(self, player):
        self.player = player
        self.image = pygame.image.load('View/GUI/Pictures/playerMarker.png')
        self.scaleImage()
        self.createSurface()

    def scaleImage(self):
        self.image = pygame.transform.scale(self.image,(10,20))

    def createSurface(self):
        surfaceSize = (self.image.get_rect().width, self.image.get_rect().height)
        self.surface = pygame.Surface(surfaceSize, flags = pygame.SRCALPHA)
        self.surface.blit(self.image,(0,0))

    def getWidth(self):
        return self.image.get_rect().width

    def getHeight(self):
        return self.image.get_rect().height

    def getCurrentCity(self):
        return self.player.getCity()

    def draw(self):
        """Draws the player"""
        return self.surface
        

