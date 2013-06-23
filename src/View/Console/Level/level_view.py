
class LevelView:
    """ Represents the view of the Level """
    
    def __init__(self, level):
        """ Initialize the Level View with its level """
        self.level = level
        
    def display(self):
        """ Display the Level View """
        self.displayPlayerDetails(self.level.players)
        print "1. View Current City\r"
        print "2. View Cities\r"
        print "3. Move City\r"
        print "4. Cure Current City\r"
        
    def displayPlayerDetails(self, players):
        """ Display the current player """
        for player in players:
            print "Player: {0}\r".format(player.city)
        print
