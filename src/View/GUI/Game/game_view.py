import pygame
from pygame.locals import *


from View.GUI.Game.SubViews.card_view   import CardView
from View.GUI.Game.SubViews.action_view import ActionView
from View.GUI.Game.SubViews.board_view  import BoardView
from View.GUI.window import window

""" 
This view consists of three smaller views
Thie board view, the player hand View, and Player Action View
"""    

"""
2/3      1/3
--------|---|
        |   |
        |   |
--------|---|
        |   | 1/3
--------|---|
"""


class GameView:

    def __init__(self, level):
        """ Initializes the game View"""
        self.level = level
        self.boardView = BoardView()
        self.cardView = CardView()
        self.actionView = ActionView()
        self.windowSize = window.getWindowSize()

    def draw(self):
        surface = pygame.Surface(self.windowSize)
        boardSurfaceSize = tuple([int(a*b) for a,b in zip((2.0/3,2.0/3), self.windowSize)])
        boardSurface = pygame.transform.scale(self.boardView.draw(),boardSurfaceSize)
        return boardSurface
        
        
