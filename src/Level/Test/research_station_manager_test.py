import unittest
from Level.level_settings import TheLevelSettings
from Level.research_station_manager import ResearchStationManager

class InitTest(unittest.TestCase):
    """ Test cases of InitTest """
    
    def  setUp(self):
        """ Not needed for this test """
        
    def defaultConstructor(self):
        """ Test that the research station manager get initialzed correctly with no parameters"""
        manager = ResearchStationManager()
        assert len(manager.getCitiesWithResearchStations()) == 0, "The research station manager initializes the city list with something when the list should be empty"

    def parameterConstructor(self):
        someObject = "A Meat Bicycle"
        manager = ResearchStationManager(someObject)

        assert len(manager.getCitiesWithResearchStations()) == 1, "Constructor for the research manager did not add a city when needed"

        assert someObject == (manager.getCitiesWithResearchStations())[0], "ResearchStationManager contructor initializded the list with the worong object"

       #assert someObject == shouldBeTheObject, " The item added to the list for the constructor in the research manager is not correct"

# Collect all test cases in this class
testcasesInitTest = ["defaultConstructor",
                    "parameterConstructor"]
suiteInitTest = unittest.TestSuite(map(InitTest, testcasesInitTest))

##########################################################

class canAddResearchStation(unittest.TestCase):
    """ Test cases of canAddResearchStation """
    
    def  setUp(self):
        """ Builds a research_station_manager """
        self.researchStationManager = ResearchStationManager()
        
    def addResearchStationToCity(self):
        """ Test that a city can be added to the Research station manager"""
        researchCityList = self.researchStationManager.getCitiesWithResearchStations()
        assert len(researchCityList) == 0, "Research Station was not initialized Correctly"

        assert self.researchStationManager.canAddResearchStation() == True, " canAddResearchStation was false when should be true"


    def testAddingReserchingToAFullList(self):
        """ Test that A city cannot have a research station if all the research stations are used """

        maxListLenght = TheLevelSettings.MAX_RESEARCH_STATIONS
        researchList = self.researchStationManager.getCitiesWithResearchStations()
        for i in range(0, maxListLenght):
            researchList.append(i)

        assert not self.researchStationManager.canAddResearchStation() , "Research station is not correctly returning false on a full list"

# Collect all test cases in this class
testcasesCanAddResearchStation = ["addResearchStationToCity",
                                   "testAddingReserchingToAFullList"]
suiteCanAddResearchStation = unittest.TestSuite(map(canAddResearchStation, testcasesCanAddResearchStation))

##########################################################

class AddResearchStationTest(unittest.TestCase):
    """ Test cases of AddResearchStationTest """
    
    def  setUp(self):
        """ Builds the researchStationManager for the tests """
        self.researchStationManager = ResearchStationManager()
        
    def addResearchStationToANonFullList(self):
        """ Test taht a research station is added to the list """
        # make sure list is empty
        assert len(self.researchStationManager.getCitiesWithResearchStations()) == 0, "Imporper initialization"
        someObject = "Some Stuff"
        #add city
        self.researchStationManager.addResearchStation(someObject)

        researchList = self.researchStationManager.getCitiesWithResearchStations()

        assert someObject in researchList , "City not added to the research station list"


    def addResearchStationToAFullList(self):
        """ Tests that a research station is not added if the list is already full """
        researchList = self.researchStationManager.getCitiesWithResearchStations()
        maxListLenght = TheLevelSettings.MAX_RESEARCH_STATIONS
        for i in range(0, maxListLenght):
            researchList.append(i)

        researchListLength = len(researchList)
        assert researchListLength == len(self.researchStationManager.getCitiesWithResearchStations()), "Pointers not working"

        self.researchStationManager.addResearchStation(10)

        assert researchListLength == len(self.researchStationManager.getCitiesWithResearchStations()), "Research station is adding to the list when list is full"


# Collect all test cases in this class
testcasesAddResearchStationTest = ["addResearchStationToANonFullList",
                                    "addResearchStationToAFullList"]
suiteAddResearchStationTest = unittest.TestSuite(map(AddResearchStationTest, testcasesAddResearchStationTest))

##########################################################

# Collect all test cases in this file
suites = [suiteInitTest,
          suiteCanAddResearchStation,
          suiteAddResearchStationTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()