from player_move_view import PlayerMoveView

from View.Console.controller import Controller

class PlayerMoveController(Controller):
    """ Controller for Player Movement """
    
    def __init__(self, player):
        """ Initialize the Player Move Controller """
        Controller.__init__(self, PlayerMoveView(player))
        