from View.Console.input_processor import inputProcessor

from kao_console import cls
from kao_console.ascii import *

class Controller:
    """ Represents a controller """
    
    def __init__(self, screen):
        """ Initialize the controller """
        self.screen = screen
        self.commands = {ESCAPE:self.stopRunning}
        self.running = False
    
    def run(self):
        """  """
        self.running = True
        
        while self.isRunning():
            self.performGameCycle()
            cls()
            self.screen.display()
            inputProcessor.processInput(self.commands)
            
    def stopRunning(self):
        """ Stop running this controller """
        self.running = False
        
    def isRunning(self):
        """ Returns if the controller is still running """
        return self.running
        
    def performGameCycle(self):
        """ Performa Game Cycle Event """
        
    def addCommand(self, character, command):
        """ Add the given command to happen on the given character """
        self.commands[character] = command
        