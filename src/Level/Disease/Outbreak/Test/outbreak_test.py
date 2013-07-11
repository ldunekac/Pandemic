import unittest

from Level.Disease.disease import Disease
from Level.Disease.Outbreak.outbreak import Outbreak

from Test.test_helper import BuildCityList

class breakout(unittest.TestCase):
    """ Test cases of breakout """
    
    def  setUp(self):
        """ Build the Cities and Outbreak for the test """
        self.cities = BuildCityList()
        self.disease = self.cities[0].disease
        
        self.citiesHitByOutbreak = set()
        self.outbreak = Outbreak(self.cities[0], self.disease, self.citiesHitByOutbreak)
        
    def infect(self):
        """ Test that the adjacent cities are infected """
        for city in self.outbreak.startingCity.adjacentCities:
            assert len(city.diseaseCounts) == 0, "City should not be infected at all"
        
        self.outbreak.breakout()
        
        for city in self.outbreak.startingCity.adjacentCities:
            assert len(city.diseaseCounts) == 1, "City should have been infected once"
        
    def multiDisease(self):
        """ Test that the adjacent cities are infected with the outbreak disease """
        disease2 = Disease()
        self.outbreak = Outbreak(self.cities[0], disease2, self.citiesHitByOutbreak)
        self.outbreak.breakout()
        
        for city in self.outbreak.startingCity.adjacentCities:
            assert city.disease not in city.diseaseCounts, "City should not be infected with its own disease"
        
        for city in self.outbreak.startingCity.adjacentCities:
            assert city.diseaseCounts[disease2] == 1, "City should have been infected once by Disease 2"
        
    def citiesHitByOutbreak(self):
        """ Test that cities hit by the outbreak are added to the 'Hit by Outbreak' list """
        self.outbreak.breakout()
        
        for city in self.cities:
            assert city in self.citiesHitByOutbreak, "City should be in the list of cities hit by the outbreak"
        
    def ignoreCitiesAlreadyHit(self):
        """ Test that cities already hit are ignored """
        self.outbreak.citiesHitByOutbreak = set([self.cities[0], self.cities[2]])
        self.outbreak.breakout()
        
        assert self.cities[1].diseaseCounts[self.disease] == 1, "City 2 should have been infected once"
        assert self.disease not in self.cities[2].diseaseCounts, "Ignored City should have not been infected"

# Collect all test cases in this class
testcasesBreakout = ["infect", "multiDisease", "citiesHitByOutbreak", "ignoreCitiesAlreadyHit"]
suiteBreakout = unittest.TestSuite(map(breakout, testcasesBreakout))

##########################################################

# Collect all test cases in this file
suites = [suiteBreakout]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()