from Level.city import City
from Level.Disease.disease import Disease
from Level.Disease.Outbreak.outbreak_manager import TheOutbreakManager

from Test.test_helper import GetCityList

import unittest

class addAdjacentCity(unittest.TestCase):
    """ Test cases of addAdjacentCity """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.city = City("Blah", None)
        self.city2 = City("Blah2", None)
        
    def hasNewCity(self):
        """ Test that a new city can be added to the adjacency list """
        self.city.addAdjacentCity(self.city2)
        
        assert self.city2 in self.city.adjacentCities, "Should have the second city in its adjacency list"

# Collect all test cases in this class
testcasesAddAdjacentCity = ["hasNewCity"]
suiteAddAdjacentCity = unittest.TestSuite(map(addAdjacentCity, testcasesAddAdjacentCity))

##########################################################

class infect(unittest.TestCase):
    """ Test cases of infect """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.disease = Disease()
        self.city = City("Blah", self.disease)
        self.cities = GetCityList()
        
        TheOutbreakManager.reset()
        
    def infectCountIncreased(self):
        """ Test that a city's disease count increases by the specified amount """
        amount = 2
        self.city.diseaseCounts[self.disease] = 0
        self.city.infect(amount)
        
        assert self.city.diseaseCounts[self.disease] == amount, "City infection should increase by the amount given"
        
    def outbreak(self):
        """ Test that a city can start an outbreak """
        assert TheOutbreakManager.totalOutbreaks == 0, "Should have no outbreaks at start"
        amount = 1
        self.cities[0].diseaseCounts[self.cities[0].disease] = 3
        self.cities[0].infect(amount)
        
        assert TheOutbreakManager.totalOutbreaks == 1, "Should have had a single outbreak"
        
    def cascadingOutbreak(self):
        """ Test that a city can cascade an outbreak """
        assert TheOutbreakManager.totalOutbreaks == 0, "Should have no outbreaks at start"
        
        amount = 1
        self.cities[0].diseaseCounts[self.cities[0].disease] = 3
        for city in self.cities[0].adjacentCities:
            city.diseaseCounts[self.cities[0].disease] = 3
            break
        self.cities[0].infect(amount)
        
        assert TheOutbreakManager.totalOutbreaks == 2, "Should have had 2 outbreak"

# Collect all test cases in this class
testcasesInfect = ["infectCountIncreased", "outbreak", "cascadingOutbreak"]
suiteInfect = unittest.TestSuite(map(infect, testcasesInfect))

##########################################################

class treat(unittest.TestCase):
    """ Test cases of infect """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.disease = Disease()
        self.city = City("Blah", self.disease)
        
    def infectCountDecrease(self):
        """ Test that a city's disease count decreases by the specified amount """
        amount = 3
        self.city.diseaseCounts[self.disease] = 5
        self.city.treat(amount)

        assert self.city.diseaseCounts[self.disease] == 2, "City did not decrease disease by desired amount"

        self.city.treat(amount)

        assert self.city.diseaseCounts[self.disease] == 0, "City disease count is not zero"          

# Collect all test cases in this class
testcasesTreat = ["infectCountDecrease"]
suiteTreat = unittest.TestSuite(map(treat, testcasesTreat))

##########################################################


# Collect all test cases in this file
suites = [suiteAddAdjacentCity, suiteInfect, suiteTreat]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()