
class LevelView:
    """ Represents the view of the Level """
    
    def __init__(self, level):
        """ Initialize the Level View with its level """
        self.level = level
        
    def display(self):
        """ Display the Level View """
        # Print Player locations
        print "1. View cities\r"
        # User actions