from Level.city import City

class Player:

    DISEASE_CURE_AMOUNT = 1

    def __init__(self, startingCity):
        """ initializes player class"""
        self.city = startingCity

    def moveTo(self, city):
        """Move player to city"""
        self.city = city

    def treatDisease(self, disease = None):
        """Cures a disease in their current city"""
        self.city.treat(self.DISEASE_CURE_AMOUNT,disease)
