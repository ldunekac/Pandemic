from Level.City.city import City
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
suites = [suiteAddAdjacentCity, suiteTreat]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()