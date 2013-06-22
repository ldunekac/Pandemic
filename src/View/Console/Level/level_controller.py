from Level.level import Level

from View.Console.controller import Controller
from View.Console.Level.cities_controller import CitiesController
from View.Console.Level.level_view import LevelView

class LevelController(Controller):
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        Controller.__init__(self, LevelView(self.level))
        self.addCommand(ord('1'), self.viewCities)
            
    def viewCities(self):
        """ View the level's cities """
        controller = CitiesController(self.level.cities)
        controller.run()
        