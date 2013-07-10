import unittest

from Level.City.city import City
from Level.Disease.disease import Disease

"""
Disease tests will make sure that when cities get infected or cured
that the corret desease amount is added or subtraced from the correct
desease.

the asserts for the city is to make sure I am doing my math right
"""

class diseaseCounterDecrease(unittest.TestCase):
    """ Test cases of diseaseCounterDecrease"""
    
    def  setUp(self):
        """ Build Cities to test infection"""
        self.reset()

    def reset(self):
        self.disease1 = Disease()
        self.disease2 = Disease()

        self.chicago = City("Chicago", self.disease1)
        self.atlanta = City("Atlanta", self.disease1)

        self.city1 = City("City1", self.disease1)
        self.city2 = City("City2", self.disease1)
        self.city3 = City("City3", self.disease1)
        self.city4 = City("City4", self.disease1)
        self.city5 = City("City5", self.disease1)
        self.city6 = City("City6", self.disease1)
        self.city7 = City("City7", self.disease1)
        self.city8 = City("City8", self.disease1)
        self.city9 = City("City9", self.disease1)
        
    def decreaseDiseaseCounter(self):
        """ Test that diseases are correctly decreased when cities are infected"""
        self.reset()

        assert self.disease1.cubeCount == 24, "Initial cube count for disease is not 24"
        assert self.disease2.cubeCount == 24, "Initial cube count for disease2 is not 24"

        # infect chicago with disease 1
        self.chicago.infect(2)
        assert self.disease1.cubeCount == 22, "Wrong amount of cubes were decreased when chicago was infected by disease 1"

    def checkOverflow(self):
        self.reset()
        """Test that cites and disease decrease correctly when a city is infected with more than 3 cubes"""
        self.chicago.infect(2)
        #check cubecount and citycount
        assert self.disease1.cubeCount == 22, "Wrong amount of cubes were decreased when chicago was infected by disease 1"
        assert self.chicago.diseaseCounts[self.disease1] == 2, "Worng amount of cubes were added to chicago" 

        self.chicago.infect(3)
        #should only have decreased by one
        assert self.disease1.cubeCount == 21, "Wrong amount of cubes were decreased when chicago was infected by disease 1 a second time"
        assert self.chicago.diseaseCounts[self.disease1] == 3, "Worng amount of cubes were added to chicago a second time"         

    def checkMultipleCitiesInfection(self):
        """ Test if the disease will decrease when the disease is spread over multiable cites"""
        self.reset()

        assert self.disease1.cubeCount == 24, "Setup test for checkMultiCitieInfection faild"

        self.chicago.infect(2)
        self.atlanta.infect(2)
        assert self.disease1.cubeCount == 20, "Disease was not decreased over multiple cities"
        assert self.chicago.diseaseCounts[self.disease1] == 2, "Chicago does not have the correct amount of cubes"
        assert self.atlanta.diseaseCounts[self.disease1] == 2, "Atlanta does not have the correct amount of cubes"

        self.chicago.infect(2)
        self.atlanta.infect(2)

        assert self.disease1.cubeCount == 18, "Disease was not decreased over multiple cities when cities where infected a second time"
        assert self.chicago.diseaseCounts[self.disease1] == 3, "Chicago does not have the correct amount of cubes when infected a second time"
        assert self.atlanta.diseaseCounts[self.disease1] == 3, "Atlanta does not have the correct amount of cubes when infected a second time"

    def multipleDiseases(self):
        """Test if cities can handle multiple diseases"""
        self.reset()

        #check initial desease count
        assert self.disease1.cubeCount == 24, "disease1 cube count is incorrect"
        assert self.disease2.cubeCount == 24, "disease1 cube count is incorrect"

        self.chicago.infect(2)
        self.chicago.infect(2, self.disease2)

        #check disease count for disease 1 and 2

        assert self.disease1.cubeCount == 22, "disease1 cube count is incorrect after chicago was infected"
        assert self.disease2.cubeCount == 22, "disease1 cube count is incorrect after chicago was infected"

        # one cube should be added
        self.chicago.infect(2)
        self.chicago.infect(2, self.disease2)

        assert self.disease1.cubeCount == 21, "disease1 cube count is incorrect after chicago was infected a second time"
        assert self.disease2.cubeCount == 21, "disease1 cube count is incorrect after chicago was infected a second time"

    def CubeCountReachesZero(self):
        """Test to make sure that the disease can't become negative"""
        self.reset()

        self.city1.infect(3)
        self.city2.infect(3)
        self.city3.infect(3)
        self.city4.infect(3)
        self.city5.infect(3)
        self.city6.infect(3)
        self.city7.infect(3)
        self.city8.infect(3)
        self.city9.infect(3)

        assert self.disease1.cubeCount == 0, "Disease was not decreased correctally"

# Collect all test cases in this class
testcasesDiseaseCounterDecrease = ["decreaseDiseaseCounter", 
                                    "checkOverflow",
                                    "checkMultipleCitiesInfection",
                                    "multipleDiseases",
                                    "CubeCountReachesZero" ]
suiteDiseaseCounterDecrease = unittest.TestSuite(map(diseaseCounterDecrease, testcasesDiseaseCounterDecrease))

##########################################################

class diseaseCounterIncrease(unittest.TestCase):
    """ Test cases of diseaseCounterDecrease"""
    #stuff to test

    # basic treatment
    # overflow treatment
    # cured treatment
    # when a treatment is eradicated

    def  setUp(self):
        """ Build Cities to test infection"""
        self.reset()

    def reset(self):
        self.disease1 = Disease()
        self.disease2 = Disease()

        self.chicago = City("Chicago", self.disease1)
        self.atlanta = City("Atlanta", self.disease1)

    def basicTreatment(self):
        "Tests that a treatment can be given"        

        self.chicago.infect(3)
        self.chicago.treat(2)

        assert self.disease1.cubeCount == 23, "Cubes where not added to the disease correctally"

        self.chicago.treat(2)

        assert self.disease1.cubeCount == 24, "Cubes where not added to the disease correctally the second time"


    def fullTreatment(self):
        """Tests when a treatment is more than the infection"""
        self.reset()

        # zero case

        self.chicago.treat(1)

        assert self.disease1.cubeCount == 24, "Cubes where not added to the disease correctally on the zero case"        

        self.chicago.infect(2)
        self.chicago.treat(3)

        assert self.disease1.cubeCount == 24, "Cubes where not added to the disease correctally"
        assert self.disease1.eradicated == False, "Disease was eradicated when disease is not cured"

    def curedTreatment(self):
        "Test that a city is fully treated when the disease is cured"
        self.reset()

        
        self.chicago.infect(3)
        self.disease1.cured = True
        self.atlanta.infect(1) # to ensure that the disease is not eradicated yest
        self.chicago.treat(1)

        assert self.disease1.cubeCount == 23, "Cubes where not added to the disease correctally when disease is cured"        

    def diseaseEradicated(self):
        "Test that if a disease is cured that it is eradicated"

        self.reset()
        self.chicago.infect(3)
        self.disease1.cure()
        assert self.disease1.isEradicated() == False, "Disease 1 was eradicated before all cubes where returned to it"
        self.chicago.treat(1)

        assert self.disease1.cubeCount == 24, "Cubes where not added to the disease correctally when disease is cured"        

        # disease is cured when it no cubes are no the board
        # make sure disease 2 is full
        assert self.disease2.cubeCount == 24 , "Disease 2 cubes is not full"
        self.disease2.cure()
        assert self.disease2.eradicated == True, "Disease 2 is not eradicated when the disease is cured and it has all of its pieces"


# Collect all test cases in this class
testcasesDiseaseCounterIncrease = ["basicTreatment",
                                    "fullTreatment",
                                    "curedTreatment",
                                    "diseaseEradicated"]
suiteDiseaseCounterIncrease = unittest.TestSuite(map(diseaseCounterIncrease, testcasesDiseaseCounterIncrease))

##########################################################

class checkIfEradicated(unittest.TestCase):
    """ Test cases of checkIfEradicated """
    
    def  setUp(self):
        """ Build the disease for the test """
        self.disease = Disease()
        
    def eradicated(self):
        """ Test that the disease is eradicated """
        self.disease.cure()
        self.disease.checkIfEradicated()
        assert self.disease.eradicated, "Disease should be eradicated"
        
    def notEradicated_NotCured(self):
        """ Test that the disease is not eradicated when it is not cured """
        self.disease.checkIfEradicated()
        assert not self.disease.eradicated, "Disease should not be eradicated if it is not cured"
        
    def notEradicated_StillInfected(self):
        """ Test that the disease is not eradicated when it is not cured """
        self.disease.removeCubes(1)
        self.disease.checkIfEradicated()
        assert not self.disease.eradicated, "Disease should not be eradicated if there are still people infected with it"

# Collect all test cases in this class
testcasesCheckIfEradicated = ["eradicated", "notEradicated_NotCured"]
suiteCheckIfEradicated = unittest.TestSuite(map(checkIfEradicated, testcasesCheckIfEradicated))

##########################################################

class addCubes(unittest.TestCase):
    """ Test cases of addCubes """
    
    def  setUp(self):
        """ Build the Disease for the test """
        self.disease = Disease()
        
    def cubesAdded(self):
        """ Test that cubes are properly added """
        amount = 3
        self.disease.cubeCount = 0
        self.disease.addCubes(amount)
        assert self.disease.cubeCount == amount, "The disease should have more cubes"

# Collect all test cases in this class
testcasesAddCubes = ["cubesAdded"]
suiteAddCubes = unittest.TestSuite(map(addCubes, testcasesAddCubes))

##########################################################

class removeCubes(unittest.TestCase):
    """ Test cases of removeCubes """
    
    def  setUp(self):
        """ Build the Disease for the test """
        self.disease = Disease()
        
    def cubesRemoved(self):
        """ Test that cubes are properly removed """
        amount = 3
        self.disease.removeCubes(amount)
        assert self.disease.cubeCount == self.disease.AMOUNT_OF_DISEASE-amount, "The disease should have cubes removed"

# Collect all test cases in this class
testcasesRemoveCubes = ["cubesRemoved"]
suiteRemoveCubes = unittest.TestSuite(map(removeCubes, testcasesRemoveCubes))

##########################################################

# Collect all test cases in this file
suites = [suiteDiseaseCounterDecrease, suiteDiseaseCounterIncrease,
          suiteCheckIfEradicated,
          suiteAddCubes,
          suiteRemoveCubes]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()