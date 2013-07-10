import unittest

from Level.City.city import City
from Level.City.city_infection_delegate import CityInfectionDelegate
from Level.Disease.disease import Disease
from Level.Disease.Outbreak.outbreak_manager import TheOutbreakManager

from Test.test_helper import BuildCityInfectionDelegate, GetCityList

class infect(unittest.TestCase):
    """ Test cases of infect """
    
    def  setUp(self):
        """ Build the Infection Delegate for the test """
        self.cities = GetCityList()
        self.infectionDelegate = BuildCityInfectionDelegate(self.cities[0])
        TheOutbreakManager.reset()
        
    def outbreak(self):
        """ Test that a city can start an outbreak """
        assert TheOutbreakManager.totalOutbreaks == 0, "Should have no outbreaks at start"
        amount = 1
        self.cities[0].diseaseCounts[self.cities[0].disease] = City.MAX_INFECTIONS_PER_DISEASE
        self.cities[0].infect(amount)
        
        assert TheOutbreakManager.totalOutbreaks == 1, "Should have had a single outbreak"
        
    def cascadingOutbreak(self):
        """ Test that a city can cascade an outbreak """
        assert TheOutbreakManager.totalOutbreaks == 0, "Should have no outbreaks at start"
        
        amount = 1
        self.cities[0].diseaseCounts[self.cities[0].disease] = City.MAX_INFECTIONS_PER_DISEASE
        for city in self.cities[0].adjacentCities:
            city.diseaseCounts[self.cities[0].disease] = City.MAX_INFECTIONS_PER_DISEASE
            break
        self.cities[0].infect(amount)
        
        assert TheOutbreakManager.totalOutbreaks == 2, "Should have had 2 outbreak"

# Collect all test cases in this class
testcasesInfect = ["outbreak", "cascadingOutbreak"]
suiteInfect = unittest.TestSuite(map(infect, testcasesInfect))

##########################################################

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

class getDiseaseToInfectWith(unittest.TestCase):
    """ Test cases of getDiseaseToInfectWith """
    
    def  setUp(self):
        """ Build the Infection Delegate for the test """
        self.infectionDelegate = BuildCityInfectionDelegate()
        
    def none(self):
        """ Test that the city's disease is returned when the given disease is None """
        assert self.infectionDelegate.getDiseaseToInfectWith(None) is self.infectionDelegate.city.disease, "Should return the city's disease when no disease is passed in"
        
    def disease(self):
        """ Test that the disease passed in is returned """
        disease = Disease()
        assert self.infectionDelegate.getDiseaseToInfectWith(disease) is disease, "Should return the provided disease"

# Collect all test cases in this class
testcasesGetDiseaseToInfectWith = ["none", "disease"]
suiteGetDiseaseToInfectWith = unittest.TestSuite(map(getDiseaseToInfectWith, testcasesGetDiseaseToInfectWith))

##########################################################

# Collect all test cases in this file
suites = [suiteShouldOutbreak,
          suiteIncreaseInfections,
          suiteGetDiseaseToInfectWith,
          suiteInfect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()