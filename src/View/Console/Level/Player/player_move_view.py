
class PlayerMoveView:
    """ Represents the Player's Move View """
    
    def __init__(self, player):
        """ Initialize the Player Move View """
        self.player = player
        self.cities = list(player.city.adjacentCities)
        
    def display(self):
        """ Display the Player Move Options """
        print "Player can move to:\r"
        print
        
        value = 0
        for city in self.cities:
            print "{0}: {1}\r".format(value, city)
            value += 1
            
    def getCity(self, index):
        """ Return the city at the given index """
        if index < len(self.cities):
            return self.cities[index]
        return None
        