
class City:
    """ Represents a city in the level """
    
    def __init__(self, name, disease):
        """ Initialize the city """
        self.name = name
        self.disease = disease
        self.adjacentCities = []
        self.diseaseCounts = {}
        
    def __repr__(self):
        """ Return the string representtation of the City """
        return self.name