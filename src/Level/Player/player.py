from Level.city import City

class Player:

    DISEASE_CURE_AMOUNT = 1

    def __init__(self, startingCity):
        """ initializes player class"""
        self.city = startingCity
        self.hand = []

    def moveTo(self, city):
        """Move player to city"""
        self.city = city

    def treatDisease(self, disease = None):
        """Cures a disease in their current city"""
        self.city.treatDisease(self.DISEASE_CURE_AMOUNT,disease)

    def addCardToHand(self, card):
        """ Add the given card to the player's hand """
        self.hand.append(card)
        
    def removeCardFromHand(self, card):
        """ Remove the given card from the player's hand """
        self.hand.remove(card)
        