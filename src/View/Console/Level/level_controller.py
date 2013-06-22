from Level.level import Level

class LevelController:
    """ Controller for the level """
    
    def __init__(self):
        """ Initialize the Level Controller """
        self.level = Level()
        self.screen = None
        
    def run(self):
        """ Run this controller """
        self.screen.print()