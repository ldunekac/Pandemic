import pygame
from pygame.locals import *


from View.GUI.Game.SubViews.card_view   import CardView
from View.GUI.Game.SubViews.action_view import ActionView
from View.GUI.Game.SubViews.board_view  import BoardView
from View.GUI.Game.PlayerViews.player_view import PlayerView
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

        #Draw Diseases

        #Draw Players
        

        return boardSurface
        
        
