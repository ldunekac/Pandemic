from Level.Disease.disease import Disease

class Level:
    """ Represents a single Level of the Expanded Pandemic Game """
    
    def __init__(self):
        """ Initialize the Level """
        self.diseases = []
        self.cities = []
        
        self.infectionDeck = None
        self.playerDeck = None
        
        self.players = []

        self.setup()
        
    def setup(self):
        """ Setup the level for the start of the game """
        disease = Disease()
        self.diseases.append(disease)
        
        self.cities.append("San Francisco", disease)
        self.cities.append("Chicago", disease)