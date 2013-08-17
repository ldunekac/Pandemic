import pygame
from pygame.locals import *


from View.GUI.Game.SubViews.card_view   import CardView
from View.GUI.Game.SubViews.action_view import ActionView
from View.GUI.Game.SubViews.board_view  import BoardView
from View.GUI.Game.PlayerViews.player_view import PlayerView
from View.GUI.Game.ResearchStationView.research_station_view import ResearchStationView
from View.GUI.window import window

""" 
This view consists of three smaller views
Thie board view, the player hand View, and Player Action View
"""    
#1600 by 900

class GameView:

    def __init__(self, level):
        """ Initializes the game View"""
        self.level = level
        self.boardView = BoardView(level.getCities())
        self.cardView = CardView()
        self.actionView = ActionView()
        self.windowSize = window.getWindowSize()
        self.boardRatio = (1,1)
        self.scailingFactor = (window.getWindowSize()[0]/1600.0, window.getWindowSize()[1]/900.0)
        self.researchStationManager = level.getResearchStationManager()
        self.researchStationView = ResearchStationView()
        #setting up player views
        players = level.getPlayers()
        self.playerViews = []

        for player in players:
            self.playerViews.append(PlayerView(player))


    def draw(self):
        surface = pygame.Surface(self.windowSize)
        boardSurfaceSize = tuple([int(a*b) for a,b in zip(self.boardRatio, self.windowSize)])
        #Draw board Surface
        boardSurface = pygame.transform.scale(self.boardView.draw(),boardSurfaceSize)
        #Draw Reseach Stations
        for city in self.researchStationManager.getCities():
            cityLocation = self.getCoord(city.getMapLocation())
            boardSurface.blit(self.researchStationView.draw(),(cityLocation[0] - self.researchStationView.getWidth()/2, cityLocation[1] - self.researchStationView.getHeight()/2 ) )
        #Draw Diseases

        #Draw Players
        cityList = []
        for playerView in self.playerViews:
            city = playerView.getCurrentCity()
            location = cityList.count(city)
            cityList.append(city)
            cityPosition = city.getMapLocation()
            cityCoord = self.getCoord(cityPosition)
            if location == 0:
                boardSurface.blit(playerView.draw(),(cityCoord[0] - playerView.getWidth(), cityCoord[1] - playerView.getHeight()) )
            elif location == 1:
                boardSurface.blit(playerView.draw(),(cityCoord[0], cityCoord[1] - playerView.getHeight()) )
            elif location == 2:
                boardSurface.blit(playerView.draw(),(cityCoord[0] - playerView.getWidth(), cityCoord[1]) )
            else:
                boardSurface.blit(playerView.draw(),(cityCoord[0], cityCoord[1]) )
        return boardSurface
        
        
    def getCoord(self, position):
        return tuple([int(a*b) for a,b in zip(self.scailingFactor,position)])