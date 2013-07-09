
class Breakout:
    """ Represents a disease breakout in a given city """
    
    def __init__(self, startingCity):
        """ Initialize the Breakout """
        self.startingCity = startingCity
        
    def breakout(self):
        """ Have the breakout occur in the Starting City """
        for city in self.startingCity.adjacentCities:
            # Check if city has already been hit by the breakout
            city.infect(1, disease=self.startingCity.disease)