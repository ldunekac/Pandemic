
class Level:
    """ Represents a single Level of the Expanded Pandemic Game """
    
    def __init__(self):
        """ Initialize the Level """
        self.diseases = []
        self.cities = []
        
        self.infectionDeck = None
        self.playerDeck = None
        
        self.players = []