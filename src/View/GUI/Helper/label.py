import pygame
from pygame.locals import *

class Label:

    def __init__(self,text = "", fontSize = 12, textPosition = (0,0)):
        """ Makes a Label for text"""
        self.text = text
        self.fontSize = fontSize
        self.textPosition = textPosition
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.renderFont()

    def renderFont(self):
        self.setRenderText()
        self.setRectangle()

    def addText(self, text):
        self.text = text
        self.renderFont()

    def setFontSize(self, fontSize):
        self.fontSize = fontSize
        self.renderFont()

    def setPosition(self, postion):
        """ Position is the top left corner of the rectangle"""
        self.textPosition = postion
        self.renderFont()

    def getFontSize(self):
        return self.fontSize

    def setRectangle(self):
        self.rectangle = self.render.get_rect()
        self.rectangle.topleft = self.textPosition

    def setTextPosition(self, myLeft = None, myCentery = None):
        self.setTextPosition = self.render.get_rect(left = myLeft, centery = myCentery)

    def setRenderText(self):
        self.render = self.font.render(self.text, 1, (10,10,10))

    def getHeight(self):
        return self.rectangle.height

    def getWidth(self):
        return self.rectangle.width

    def mouseOnText(self, mousePosition):
        return self.rectangle.collidepoint(mousePosition)

    def draw(self):
        self.setRenderText()
        surface = pygame.Surface((self.rectangle.width, self.rectangle.height),flags = pygame.SRCALPHA)
        surface.blit(self.render,(0,0))
        return surface
