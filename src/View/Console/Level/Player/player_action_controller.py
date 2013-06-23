from View.Console.controller import Controller
from View.Console.Level.cities_controller import CitiesController
from View.Console.Level.city_controller import CityController
from View.Console.Level.level_view import LevelView
from View.Console.Level.Player.player_move_controller import PlayerMoveController
from View.Console.Level.Player.player_action_view import PlayerActionView

from kao_console.ascii import *

class PlayerActionController(Controller):
    """ Controller for a Player to choose his current Actions """
    
    def __init__(self, level, player):
        """ Initialize the *** Controller """
        Controller.__init__(self, PlayerActionView(level, player))
        self.level = level
        self.player = player
        
        self.quitting = False
        
        self.commands = {}
        self.addCommand(ESCAPE, self.quit)
        self.addCommand(ord('1'), self.viewCity)
        self.addCommand(ord('2'), self.viewCities)
        self.addCommand(ord('3'), self.moveToACity)
        self.addCommand(ord('4'), self.treatCurrentCity)
        
    def viewCity(self):
        """ View the level's cities """
        controller = CityController(self.player.city)
        controller.run()
            
    def viewCities(self):
        """ View the level's cities """
        controller = CitiesController(self.level.cities)
        controller.run()
        
    # Actual actions -- If the Action succeeds this controller should stop
    def moveToACity(self):
        """ Move the Player to a city """
        controller = PlayerMoveController(self.player)
        controller.run()
        
    def treatCurrentCity(self):
        """ Cure the current city """
        self.player.treatDisease()
        
    def quit(self):
        """ Try to quit the game """
        self.quitting = True
        
    def isRunning(self):
        """ Return if the controller is running """
        return not self.quitting