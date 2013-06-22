
class LevelView:
    """ Represents the view of the Level """
    
    def __init__(self, level):
        """ Initialize the Level View with its level """
        self.level = level
        
    def display(self):
        """ Display the Level View """
        self.displayPlayerDetails(self.level.players)
        print "1. View cities\r"
        # User actions
        
    def displayPlayerDetails(self, players):
        """ Display the current player """
        for player in players:
            print "Player: {0}".format(player.city)