from Level.level import Level

from View.Console.controller import Controller
from View.Console.Level.level_view import LevelView
from View.Console.Level.Player.player_action_controller import PlayerActionController

class LevelController(Controller):
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        Controller.__init__(self, LevelView(self.level))
            
    def performGameCycle(self):
        """ Performa Game Cycle Event """
        player = self.level.players[0]
        
        controller = PlayerActionController(self.level, player)
        controller.run()
        
        if controller.quitting:
            self.stopRunning()