
class PlayerMoveView:
    """ Represents the Player's Move View """
    
    def __init__(self, player):
        """ Initialize the Player Move View """
        self.player = player
        
    def display(self):
        """ Display the Player Move Options """
        print "Player can move to:\r"
        print
        
        value = 0
        for city in self.player.city.adjacentCities:
            print "{0}: {1}\r".format(value, city)