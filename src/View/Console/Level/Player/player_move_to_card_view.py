from Level.Deck.Card.city_card import CityCard

class PlayerMoveToCardView:
    """ Represents the view for a *** """
    
    def __init__(self, player):
        """ Initialize the Player Move To Card View """
        self.player = player
        self.cityCards = []
        
        for card in self.player.hand:
            if card.TYPE is CityCard.TYPE:
                self.cityCards.append(card)
        
    def display(self):
        """ Display the Player Move Options """
        print "Player can move to:\r"
        print
        
        value = 0
        for cityCard in self.cityCards:
            print "{0}: {1}\r".format(value, cityCard)
            value += 1
            
    def getCard(self, index):
        """ Return the city at the given index """
        if index < len(self.cityCards):
            return self.cityCards[index]
        return None
        