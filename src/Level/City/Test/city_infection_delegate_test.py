import unittest

from Level.City.city import City
from Level.City.city_infection_delegate import CityInfectionDelegate
from Level.Disease.disease import Disease

from Test.test_helper import BuildCityInfectionDelegate

class shouldOutbreak(unittest.TestCase):
    """ Test cases of shouldOutbreak """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.infectionDelegate = BuildCityInfectionDelegate()
        
    def noOutbreak(self):
        """ Test that no outbreak should happen """
        disease = Disease()
        assert disease not in self.infectionDelegate.city.diseaseCounts, "City should not have the given disease"
        assert not self.infectionDelegate.shouldOutbreak(CityInfectionDelegate.MAX_INFECTIONS_PER_DISEASE, disease), "Should not outbreak when infected by less than or equal to the max infections"

    def shouldOutbreak(self):
        """ Test that an outbreak can happen properly """
        disease = Disease()
        self.infectionDelegate.city.diseaseCounts[disease] = 1
        assert self.infectionDelegate.shouldOutbreak(CityInfectionDelegate.MAX_INFECTIONS_PER_DISEASE, disease), "Should outbreak when the disease count goes above the max infections"
        
# Collect all test cases in this class
testcasesShouldOutbreak = ["noOutbreak", "shouldOutbreak"]
suiteShouldOutbreak = unittest.TestSuite(map(shouldOutbreak, testcasesShouldOutbreak))

##########################################################

# Collect all test cases in this file
suites = [suiteShouldOutbreak]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()