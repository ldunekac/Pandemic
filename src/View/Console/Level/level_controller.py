from Level.level import Level

from View.Console.controller import Controller
from View.Console.Level.cities_controller import CitiesController
from View.Console.Level.city_controller import CityController
from View.Console.Level.level_view import LevelView
from View.Console.Level.Player.player_move_controller import PlayerMoveController

class LevelController(Controller):
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        Controller.__init__(self, LevelView(self.level))
        self.addCommand(ord('1'), self.viewCity)
        self.addCommand(ord('2'), self.viewCities)
        self.addCommand(ord('3'), self.moveToACity)
        self.addCommand(ord('4'), self.cureCurrentCity)
        
    def viewCity(self):
        """ View the level's cities """
        controller = CityController(self.level.players[0].city)
        controller.run()
            
    def viewCities(self):
        """ View the level's cities """
        controller = CitiesController(self.level.cities)
        controller.run()
        
    def moveToACity(self):
        """ Move the Player to a city """
        controller = PlayerMoveController(self.level.players[0])
        controller.run()
        
    def cureCurrentCity(self):
        """ Cure the current city """
        self.level.players[0].cureDisease()