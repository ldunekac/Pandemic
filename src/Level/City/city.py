from Level.City.city_infection_delegate import CityInfectionDelegate
from Level.City.city_treatment_delegate import CityTreatmentDelegate

class City:
    """ Represents a city in the level """
    
    def __init__(self, name, disease, mapLocation = None):
        """ Initialize the city """
        self.name = name
        self.disease = disease
        self.adjacentCities = set()
        self.diseaseCounts = {}
        self.mapLocation = mapLocation

        self.infectionDelegate = CityInfectionDelegate(self)
        self.treatmentDelegate = CityTreatmentDelegate(self)

    def getName(self):
        return self.name

    def isInfected(self):
        for disease in self.diseaseCounts:
            if self.diseaseCounts[disease] > 0:
                return True
        return False
        
    def getDisease(self):
        return self.disease

    def getMapLocation(self):
        return self.mapLocation

    def getAdjacentCities(self):
        return self.adjacentCities

    def addAdjacentCity(self, city):
        """ Add a city to this city's adjacency list """
        self.adjacentCities.add(city)
        
    def infect(self, amount, disease=None):
        """ Infect the city with given amount """
        self.infectionDelegate.infect(amount, disease)

    def treat(self, amount, disease = None):
        """ Cures a city of a disease by a given amount"""
        self.treatmentDelegate.treat(amount, disease)
        
    def getDiseaseInfections(self, disease):
        """ Return the number of infections in the city of for the given disease """
        amount = 0
        if disease in self.diseaseCounts:
            amount = self.diseaseCounts[disease]
        return amount

    def getRelativeLocation(self):
        return self.mapLocation
        
    def __repr__(self):
        """ Return the string representtation of the City """
        return self.name