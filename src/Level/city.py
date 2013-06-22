
class City:
    """ Represents a city in the level """
    
    def __init__(self):
        """ Initialize the city """
        self.name = "Blah"
        self.disease = None
        self.adjacentCities = []
        self.diseaseCounts = {}