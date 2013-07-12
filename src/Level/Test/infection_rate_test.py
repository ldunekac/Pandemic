import unittest
from Level.infection_rate import InfectionRate

class InfectionRateTest(unittest.TestCase):
    """ Test cases of InfectionRateTest """
    
    def  setUp(self):
        """ Sets up the infection Rate Class """
        self.infectionRate = InfectionRate()

    def initialize(self):
        """ Makes a new InfectionRate every time this function is called """
        self.infectionRate = InfectionRate()

    def testIncreaseInfectionRate(self):
        """ Test that the infection rate increases as defined by the infection rate table"""
        self.initialize()
        table = self.infectionRate.infectionTable

        for i in range(1,4):
            self.infectionRate.increaseInfectionRate()
            assert self.infectionRate.infectionTable[i] == self.infectionRate.getInfectionRate(), "Increasing the infection rate is not iterating thought the table"

    def testMaxInfectionRate(self):
        """ Tests that the infection rate cannot increase beyond the infe table"""
        self.initialize()
        for i in range(0, len(self.infectionRate.infectionTable)+1):
            self.infectionRate.increaseInfectionRate()

        assert self.infectionRate.getInfectionRate() == self.infectionRate.infectionTable[len(self.infectionRate.infectionTable)-1], "The infection rate index increased beyond the table size"

# Collect all test cases in this class
infectionRateTestCases = [  "testIncreaseInfectionRate",
                            "testMaxInfectionRate" ]
suiteInfectionRateTest = unittest.TestSuite(map(InfectionRateTest, infectionRateTestCases))

##########################################################

class getInfectionRate(unittest.TestCase):
    """ Test cases of getInfectionRate """
    
    def  setUp(self):
        """ Sets up the infection Rate Class """
        self.infectionRate = InfectionRate()

    def initialize(self):
        """ Makes a new InfectionRate every time this function is called """
        self.infectionRate = InfectionRate()

    def tetGetInfectionRate(self):
        """ Test that the InfectionRate will return the first element in the infectionRate Table """
        self.initialize()
        assert self.infectionRate.getInfectionRate() == self.infectionRate.infectionTable[0], "InfectonRate is not initialized or the infection table is not 2"


# Collect all test cases in this class
testcasesGetInfectionRate = ["tetGetInfectionRate"]
suiteGetInfectionRate = unittest.TestSuite(map(getInfectionRate, testcasesGetInfectionRate))

##########################################################

# Collect all test cases in this file
suites = [suiteInfectionRateTest,
          suiteGetInfectionRate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()