from Level.City.city import City
from Level.level import Level

import unittest

class makeCitiesAdjacent(unittest.TestCase):
    """ Test cases of makeCitiesAdjacent """
    
    def  setUp(self):
        """ Build the cities and level for the test """
        self.level = Level()
        self.city1 = City("Blah1", None)
        self.city2 = City("Blah2", None)
        
    def areAdjacent(self):
        """ Test that the cities are adjacent """
        self.level.makeCitiesAdjacent(self.city1, self.city2)
        
        assert self.city1 in self.city2.adjacentCities, "City 2 should know it is adjacent to City 1"
        assert self.city2 in self.city1.adjacentCities, "City 1 should know it is adjacent to City 2"

# Collect all test cases in this class
testcasesMakeCitiesAdjacent = ["areAdjacent"]
suiteMakeCitiesAdjacent = unittest.TestSuite(map(makeCitiesAdjacent, testcasesMakeCitiesAdjacent))

##########################################################

# Collect all test cases in this file
suites = [suiteMakeCitiesAdjacent]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()