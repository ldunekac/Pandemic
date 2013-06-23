from Level.level import Level

from View.Console.controller import Controller
from View.Console.input_processor import inputProcessor
from View.Console.Level.cities_controller import CitiesController
from View.Console.Level.city_controller import CityController
from View.Console.Level.level_view import LevelView
from View.Console.Level.Player.player_action_controller import PlayerActionController

class LevelController(Controller):
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        Controller.__init__(self, LevelView(self.level))
        
    def run(self):
        """  """
        self.running = True
        
        while self.running:
            player = self.level.players[0]
            
            #for i in range(4):
            controller = PlayerActionController(self.level, player)
            controller.run()
            inputProcessor.processInput(self.commands)