import pygame
from pygame.locals import *

from View.GUI.window import window

class BoardView:

    def __init__(self, cityList):
        """Initializes the Board View"""
        self.cityList = cityList
        self.boardImage = pygame.image.load('View/GUI/Pictures/world_map.png')
        self.boardSurface = pygame.Surface(window.getWindowSize())
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)
        self.fontSize = 16
        self.font = pygame.font.SysFont(None,self.fontSize)
        self.radious = 10
        self.fontBuffer = 5

    def draw(self):
        """ Draws the board"""
        self.boardSurface.blit(pygame.transform.scale(self.boardImage,window.getWindowSize()),(0,0))
        for line in self.connectCities():
            if abs(line[0][0] - line[1][0]) > 1600/2:
                leftMapPoint = line[0]
                rightMapPoint = line[1]
                if line[1][0] < line[0][0]:
                    leftMapPoint = line[1]
                    rightMapPoint = line[0]
                rightBordEdgePosition = self.calcRighEdgePoint(leftMapPoint,rightMapPoint)
                leftBoardEdgePosition = (0, rightBordEdgePosition[1])
                pygame.draw.line(self.boardSurface,(250,250,210),self.getCord(rightMapPoint),self.getCord(rightBordEdgePosition), 1)
                pygame.draw.line(self.boardSurface,(250,250,210),self.getCord(leftBoardEdgePosition),self.getCord(leftMapPoint), 1)
            else: 
                pygame.draw.line(self.boardSurface,(250,250,210),self.getCord(line[0]),self.getCord(line[1]), 1)
        for city in self.cityList:
            cityColor = city.getDisease().getColor()
            cityLocation = self.getCord(city.getMapLocation())
            pygame.draw.circle(self.boardSurface,cityColor,cityLocation,self.radious)
            render = self.font.render(city.getName(),1, (255,255,255))
            renderPosition = render.get_rect(centerx = cityLocation[0], centery = cityLocation[1] + self.radious + self.fontBuffer )
            self.boardSurface.blit(render,renderPosition)
        return self.boardSurface.convert()

    def getCord(self, position):
        return tuple([int(a*b) for a,b in zip(self.scailingFactor,position)])

    def connectCities(self):
        lines = set()

        for city in self.cityList:
            for connectedCity in city.getAdjacentCities():
                line1, line2 = self.getLines(city, connectedCity)
                if not line1 in lines and not line2 in lines:
                    lines.add(line1)

        return lines


    def getLines(self, city1, city2):
        city1Location = city1.getMapLocation()
        city2Location = city2.getMapLocation()
        return (city1Location,city2Location), (city2Location, city1Location)


    def calcRighEdgePoint(self, leftMost, rightMost):
        transpoedPoint = (rightMost[0] + 1600, rightMost[1])
        x1 = leftMost[0]
        y1 = leftMost[1]
        x2 = transpoedPoint[0]
        y2 = transpoedPoint[1]

        x3 = 1600
        y3 = 0
        x4 = 1600
        y4 = 900

        determinant = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        a = (x1 * y2) - (y1 * x2)
        b = (x3 * y4) - (y3 * x4)
        if determinant == 0:
            return (int((x1 + x3) *.5),int((y1 + y3) *.5))
        else:
            return (int(((a * (x3 - x4)) - ((x1 - x2) * b)) / determinant),int(((a * (y3 - y4)) - ((y1 - y2) * b)) / determinant))
