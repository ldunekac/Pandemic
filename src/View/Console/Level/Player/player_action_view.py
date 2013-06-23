
class PlayerActionView:
    """ Represents the view for a *** """
    
    def __init__(self, level, player):
        """ Initialize the view """
        self.level = level
        self.player = player
        self.actionCount = 4
        
    def display(self):
        """ Display the Player action options """
        self.displayPlayerDetails(self.level.players)
        self.displayHand()
        
        print "1. View Current City\r"
        print "2. View Cities\r"
        print "3. Move to Adjacent City\r"
        print "4. Move to City on Card\r"
        print "5. Move to City from Card\r"
        print "6. Treat Current City\r"
        print "7. Discover Cure\r"
        print "8. Stop Early\r"
        
    def displayPlayerDetails(self, players):
        """ Display the current player """
        print "Current Player: {0}\r".format(self.player.city)
        print "{0} Actions Remaining\r".format(self.actionCount)
        print
        
        for player in players:
            if player is not self.player:
                print "Player: {0}\r".format(player.city)
        print
        
    def displayHand(self):
        """ Display the player's hand """
        print "Hand:\r"
        
        for card in self.player.hand:
            print card, "\r"
        print
        