from Level.city import City
from Level.Disease.disease import Disease

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
        
    def infectCountIncreased(self):
        """ Test that a city's disease count increases by the specified amount """
        amount = 2
        self.city.diseaseCounts[self.disease] = 0
        self.city.infect(amount)
        
        assert self.city.diseaseCounts[self.disease] == amount, "City infection should increase by the amount given"

# Collect all test cases in this class
testcasesInfect = ["infectCountIncreased"]
suiteInfect = unittest.TestSuite(map(infect, testcasesInfect))

##########################################################

class Cure(unittest.TestCase):
    """ Test cases of infect """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.disease = Disease()
        self.city = City("Blah", self.disease)
        
    def infectCountDecrease(self):
        """ Test that a city's disease count decreases by the specified amount """
        amount = 3
        self.city.diseaseCounts[self.disease] = 5
        self.city.cureDisease(amount)

        assert self.city.diseaseCounts[self.disease] == 2, "City did not decrease disease by desired amount"

        self.city.cureDisease(amount)

        assert self.city.diseaseCounts[self.disease] == 0, "City disease count is not zero"          

# Collect all test cases in this class
testcasesCure = ["infectCountDecrease"]
suiteCure = unittest.TestSuite(map(Cure, testcasesCure))

##########################################################



# Collect all test cases in this file
suites = [suiteAddAdjacentCity, suiteInfect, suiteCure]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()