import pygame
from pygame.locals import *

from View.GUI.window import window


class LineView:

    def __init__(self, cityList):
        """ Makes all the lines that connect the cities"""
        self.cityList = cityList
        self.boardSurface = pygame.Surface(window.getWindowSize(), pygame.SRCALPHA)
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)

    def draw(self):
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
        
        return self.boardSurface

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
