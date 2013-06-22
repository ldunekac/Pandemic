from Level.level import Level

from View.Console.Level.level_view import LevelView

class LevelController:
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        self.screen = LevelView(self.level)
        
    def run(self):
        """ Run this controller """
        self.screen.display()