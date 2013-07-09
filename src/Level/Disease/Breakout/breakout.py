
class Breakout:
    """ Represents a disease breakout in a given city """
    
    def __init__(self, startingCity, disease, citiesHitByBreakout):
        """ Initialize the Breakout """
        self.startingCity = startingCity
        self.disease = disease
        self.citiesHitByBreakout = citiesHitByBreakout
        self.citiesHitByBreakout.add(startingCity)
        
    def breakout(self):
        """ Have the breakout occur in the Starting City """
        for city in self.startingCity.adjacentCities:
            if city not in self.citiesHitByBreakout:
                city.infect(1, disease=self.disease)
                self.citiesHitByBreakout.add(city)