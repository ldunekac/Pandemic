from Level.level import Level

from View.Console.input_processor import inputProcessor
from View.Console.Level.level_view import LevelView

from kao_console.ascii import *

class LevelController:
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        self.screen = LevelView(self.level)
        
        self.commands = {ord('1'):self.viewCities,
                         ESCAPE:self.stopRunning}
        
    def run(self):
        """ Run this controller """
        self.running = True
        
        while self.running:
            self.screen.display()
            inputProcessor.processInput(self.commands)
            
    def viewCities(self):
        """ View the level's cities """
        print "Viewing Cities\r"
        
    def stopRunning(self):
        """  """
        self.running = False
        