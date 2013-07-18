
""" 
This view consists of three smaller views
Thie board view, the player hand View, and Player Action View
"""    

from View.GUI.Game.SubViews.card_view   import CardView
from View.GUI.Game.SubViews.action_view import ActionView
from View.GUI.Game.SubViews.board_view  import BoardView

class GameView:

    def __init__(self):
        """ Initializes the game View"""
        self.boardView = BoardView()
        self.cardView = CardView()
        self.actionView = ActionView()