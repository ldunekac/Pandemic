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

class normalizeTreatmentAccount(unittest.TestCase):
    """ Test cases of normalizeTreatmentAccount """
    
    def  setUp(self):
        """ Build the Treatment Delegate for the test """
        self.disease = Disease()
        self.treatmentDelegate = BuildCityTreatmentDelegate()
        self.treatmentDelegate.city.diseaseCounts[self.disease] = self.treatmentDelegate.MAX_INFECTIONS_PER_DISEASE
        
    def basic(self):
        """ Test that the basic case works """
        treatAmount = 1
        amount = self.treatmentDelegate.normalizeTreatmentAmount(treatAmount, self.disease)
        assert amount == treatAmount, "Normalized Amount should be the original amount"
        
    def cured(self):
        """ Test that a cured disease can cure all the infections in a city """
        self.disease.cure()
        treatAmount = 1
        amount = self.treatmentDelegate.normalizeTreatmentAmount(treatAmount, self.disease)
        assert amount == self.treatmentDelegate.MAX_INFECTIONS_PER_DISEASE, "Normalized Amount should be the Max Infections a City can have"
        
    def lessInfectionsThanTreatmentAmount(self):
        """ Test that the proper amount is returned when there are less infections than can be cured """
        infections = 1
        self.treatmentDelegate.city.diseaseCounts[self.disease] = infections
        treatAmount = 2
        amount = self.treatmentDelegate.normalizeTreatmentAmount(treatAmount, self.disease)
        assert amount == infections, "Normalized Amount should be the number of infections of that disease if there are less infections than can be treated"
        
    def treatNewDisease(self):
        """ Test that the proper amount is returned when there are less infections than can be cured """
        disease = Disease()
        treatAmount = 2
        amount = self.treatmentDelegate.normalizeTreatmentAmount(treatAmount, disease)
        assert amount == 0, "If the disease is not in the city nothing should be treateds"

# Collect all test cases in this class
testcasesNormalizeTreatmentAccount = ["basic", "cured", "lessInfectionsThanTreatmentAmount", "treatNewDisease"]
suiteNormalizeTreatmentAccount = unittest.TestSuite(map(normalizeTreatmentAccount, testcasesNormalizeTreatmentAccount))

##########################################################

# Collect all test cases in this file
suites = [suiteTreatInfections,
          suiteNormalizeTreatmentAccount]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()