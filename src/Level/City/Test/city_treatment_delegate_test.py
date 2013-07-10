import unittest

from Level.Disease.disease import Disease

from Test.test_helper import BuildCityTreatmentDelegate

class treatInfections(unittest.TestCase):
    """ Test cases of treatInfections """
    
    def  setUp(self):
        """ Build the Treatment Delegate for the test """
        self.treatmentDelegate = BuildCityTreatmentDelegate()
        
    def treatInfections(self):
        """ Test that infections are treated properly """
        disease = Disease()
        amount = 2
        self.treatmentDelegate.city.diseaseCounts[disease] = amount
        
        self.treatmentDelegate.treatInfections(amount, disease)
        assert self.treatmentDelegate.city.diseaseCounts[disease] == 0, "Should have completely treated the disease"
        
    def returnCubes(self):
        """ Test that the disease infections are returned properly """
        disease = Disease()
        amount = 2
        self.treatmentDelegate.city.diseaseCounts[disease] = amount
        disease.removeCubes(2)
        
        self.treatmentDelegate.treatInfections(amount, disease)
        assert disease.cubeCount == disease.AMOUNT_OF_DISEASE, "Should have completely returned all disease cubes"
        
    def treatDiseaseWithNoInfections(self):
        """ Test that treating a diseas not in the city works properly """
        disease = Disease()
        amount = 2
        
        self.treatmentDelegate.treatInfections(amount, disease)
        assert disease not in self.treatmentDelegate.city.diseaseCounts, "Disease should not be in the city's disease Counts"

# Collect all test cases in this class
testcasesTreatInfections = ["treatInfections", "returnCubes", "treatDiseaseWithNoInfections"]
suiteTreatInfections = unittest.TestSuite(map(treatInfections, testcasesTreatInfections))

##########################################################

# Collect all test cases in this file
suites = [suiteTreatInfections]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()