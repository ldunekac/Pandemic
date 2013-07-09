
class Outbreak:
    """ Represents a disease outbreak in a given city """
    
    def __init__(self, startingCity, disease, citiesHitByOutbreak):
        """ Initialize the Breakout """
        self.startingCity = startingCity
        self.disease = disease
        self.citiesHitByOutbreak = citiesHitByOutbreak
        self.citiesHitByOutbreak.add(startingCity)
        
    def breakout(self):
        """ Have the breakout occur in the Starting City """
        for city in self.startingCity.adjacentCities:
            if city not in self.citiesHitByOutbreak:
                city.infect(1, disease=self.disease)
                self.citiesHitByOutbreak.add(city)