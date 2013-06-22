
class City:
    """ Represents a city in the level """
    
    def __init__(self, name, disease):
        """ Initialize the city """
        self.name = name
        self.disease = disease
        self.adjacentCities = set()
        self.diseaseCounts = {}
        
    def addAdjacentCity(self, city):
        """ Add a city to this city's adjacency list """
        self.adjacentCities.add(city)
        
    def infect(self, amount, disease=None):
        """ Infect the city with given amount """
        if disease is None:
            disease = self.disease
            
        if disease in self.diseaseCounts:
            self.diseaseCounts[disease] += amount
        else:
            self.diseaseCounts[disease] = amount
        # Will need to check for outbreaks at some point
        
    def __repr__(self):
        """ Return the string representtation of the City """
        return self.name