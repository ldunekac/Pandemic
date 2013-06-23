
class PlayerActionView:
    """ Represents the view for a *** """
    
    def __init__(self, level, player):
        """ Initialize the view """
        self.level = level
        self.player = player
        
    def display(self):
        """ Display the Player action options """
        self.displayPlayerDetails(self.level.players)
        print "1. View Current City\r"
        print "2. View Cities\r"
        print "3. Move City\r"
        print "4. Treat Current City\r"
        
    def displayPlayerDetails(self, players):
        """ Display the current player """
        print "Current Player: {0}\r".format(self.player.city)
        print
        
        for player in players:
            if player is not self.player:
                print "Player: {0}\r".format(player.city)
        print
        