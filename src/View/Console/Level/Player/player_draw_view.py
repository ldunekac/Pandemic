
class PlayerDrawView:
    """ Represents the view for the Player Drawing """
    
    def __init__(self, card):
        """ Initialize the view """
        self.card = card
        
    def display(self):
        """ Display the Card the Player Drew """
        print "Drew: {0}\r".format(self.card)