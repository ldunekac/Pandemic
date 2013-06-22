from Level.city import City
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
        
        sanFrancisco = City("San Francisco", disease)
        chicago = City("Chicago", disease)
        
        self.cities.append(chicago)
        self.cities.append(sanFrancisco)
        
        self.makeCitiesAdjacent(chicago, sanFrancisco)
        
    def makeCitiesAdjacent(self, city1, city2):
        """ Make the two cities given adjacent """
        city1.addAdjacentCity(city2)
        city2.addAdjacentCity(city1)