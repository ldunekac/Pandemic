from Level.city import City

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

# Collect all test cases in this file
suites = [suiteAddAdjacentCity]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()