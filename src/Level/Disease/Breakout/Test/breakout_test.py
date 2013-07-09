import unittest

from Level.city import City
from Level.Disease.disease import Disease
from Level.Disease.Breakout.breakout import Breakout

class breakout(unittest.TestCase):
    """ Test cases of breakout """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.disease = Disease()
        
        self.city1 = City("Blah1", self.disease)
        self.city2 = City("Blah2", self.disease)
        self.city3 = City("Blah3", self.disease)
        self.city1.addAdjacentCity(self.city2)
        self.city1.addAdjacentCity(self.city3)
        
        self.breakout = Breakout(self.city1)
        
    def infect(self):
        """ Test that the adjacent cities are infected """
        assert len(self.city2.diseaseCounts) == 0, "City 2 should not be infected at all"
        assert len(self.city3.diseaseCounts) == 0, "City 3 should not be infected at all"
        
        self.breakout.breakout()
        
        assert self.city2.diseaseCounts[self.disease] == 1, "City 2 should have been infected once"
        assert self.city3.diseaseCounts[self.disease] == 1, "City 3 should have been infected once"
        
    def multiDisease(self):
        """ Test that the adjacent cities are infected """
        disease2 = Disease()
        self.city1.disease = disease2
        self.breakout = Breakout(self.city1)
        self.breakout.breakout()
        
        assert self.city2.disease not in self.city2.diseaseCounts, "City 2 should not be infected with its own disease"
        assert self.city3.disease not in self.city3.diseaseCounts, "City 3 should not be infected with its own disease"
        assert self.city2.diseaseCounts[disease2] == 1, "City 2 should have been infected once by Disease 2"
        assert self.city3.diseaseCounts[disease2] == 1, "City 3 should have been infected once by Disease 2"

# Collect all test cases in this class
testcasesBreakout = ["infect", "multiDisease"]
suiteBreakout = unittest.TestSuite(map(breakout, testcasesBreakout))

##########################################################

# Collect all test cases in this file
suites = [suiteBreakout]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()