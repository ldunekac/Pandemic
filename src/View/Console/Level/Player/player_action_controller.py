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
        self.addCommand(ord('3'), self.moveToAdjacentCity)
        self.addCommand(ord('4'), self.moveToCityOnCard)
        self.addCommand(ord('5'), self.moveFromCityCard)
        self.addCommand(ord('6'), self.treatCurrentCity)
        self.addCommand(ord('7'), self.discoverCure)
        self.addCommand(ord('8'), self.stopEarly)
        
    def viewCity(self):
        """ View the level's cities """
        controller = CityController(self.player.city)
        controller.run()
            
    def viewCities(self):
        """ View the level's cities """
        controller = CitiesController(self.level.cities)
        controller.run()
        
    def stopEarly(self):
        """ Stop performing actions early """
        self.screen.actionCount = 0
        
    # Actual actions -- If the Action succeeds this controller should stop
    def moveToAdjacentCity(self):
        """ Move the Player to a city """
        controller = PlayerMoveController(self.player)
        controller.run()
        if controller.actionCompleted:
            self.useAction()
            
    def moveToCityOnCard(self):
        """ Move to a city on a card in the player's hand """
        
    def moveFromCityCard(self):
        """ Move to any city from a card for the player's current city """
        
    def treatCurrentCity(self):
        """ Cure the current city """
        self.player.treatDisease()
        self.useAction()
        
    def discoverCure(self):
        """ Discover a cure for the disease """
        
    def quit(self):
        """ Try to quit the game """
        self.quitting = True
        
    def isRunning(self):
        """ Return if the controller is running """
        return not self.quitting and self.screen.actionCount > 0
    
    def useAction(self):
        """ Use an action point """
        self.screen.actionCount -= 1