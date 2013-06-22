from kao_console import getch
from kao_console.ascii import *

class InputProcessor:
    """ Class to process input from pygame event queue and convert them to game commands """
    
    def __init__(self):
        """ Builds the input processor """
        
    def processInput(self, functions):
        """ Process inputs to functions """
        character = getch()
        
        if character in functions:
            functions[character]()
        
inputProcessor = InputProcessor()