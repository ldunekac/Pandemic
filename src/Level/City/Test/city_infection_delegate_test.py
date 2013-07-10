import unittest

from Level.City.city import City
from Level.City.city_infection_delegate import CityInfectionDelegate
from Level.Disease.disease import Disease

from Test.test_helper import BuildCityInfectionDelegate

class shouldOutbreak(unittest.TestCase):
    """ Test cases of shouldOutbreak """
    
    def  setUp(self):
        """ Build the Infection Delegate for the test """
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

class increaseInfections(unittest.TestCase):
    """ Test cases of increaseInfections """
    
    def  setUp(self):
        """ Build the Infection Delegate for the test """
        self.infectionDelegate = BuildCityInfectionDelegate()
        
    def diseaseCountIncreased_NewDisease(self):
        """ Test that the disease count increases properly """
        disease = Disease()
        amount = 1
        
        assert disease not in self.infectionDelegate.city.diseaseCounts, "Should not have any infections of the given disease"
        self.infectionDelegate.increaseInfections(amount, disease)
        assert self.infectionDelegate.city.getDiseaseInfections(disease) == amount, "Should have been infected by the amount given"
        
    def diseaseCountIncreased_PreviousDisease(self):
        """ Test that the disease count increases properly """
        disease = Disease()
        startingAmount = 1
        amount = 1
        self.infectionDelegate.city.diseaseCounts[disease] = startingAmount
        
        self.infectionDelegate.increaseInfections(amount, disease)
        assert self.infectionDelegate.city.getDiseaseInfections(disease) == startingAmount+amount, "Disease Count should have increased by the amount given"
        
    def diseaseCubesRemoved(self):
        """ Test that the disease cubes are removed properly """
        disease = Disease()
        amount = 2
        startingCubeCount = disease.cubeCount
        
        self.infectionDelegate.increaseInfections(amount, disease)
        assert disease.cubeCount == startingCubeCount-amount, "The cube count should now be decreased by the infection amount"

# Collect all test cases in this class
testcasesIncreaseInfections = ["diseaseCountIncreased_NewDisease", "diseaseCountIncreased_PreviousDisease", "diseaseCubesRemoved"]
suiteIncreaseInfections = unittest.TestSuite(map(increaseInfections, testcasesIncreaseInfections))

##########################################################

# Collect all test cases in this file
suites = [suiteShouldOutbreak,
          suiteIncreaseInfections]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()