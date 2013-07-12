import unittest
from Level.Deck.Card.epidemic_card import EpidemicCard
from Level.level_settings import TheLevelSettings
from Level.infection_rate import InfectionRate
from Level.Deck.infection_deck import InfectionDeck
from Test.test_helper import BuildInfectionDeck

# test will need || infectionDeck && infectionRate ||

class infectEpidemicCardTest(unittest.TestCase):
    """ Test cases of functionToTest """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.infectionDeck = BuildInfectionDeck()
        self.infectionRate = InfectionRate()
        self.epidemicCard = EpidemicCard(self.infectionDeck, self.infectionRate)

        
    def infectFlowTest(self):
        """ Test that ... """
        city = self.infectionDeck.deck[-1]
        self.epidemicCard.infect()
        assert city.getDiseaseInfections(city.disease) == TheLevelSettings.MAX_INFECTIONS_PER_DISEASE_IN_CITY, " EpidemicCard did not infect the city witht he proper disease"


# Collect all test cases in this class
infectEpidemicCardTestcases = ["infectFlowTest"]
suiteinfectEpidemicCardTest = unittest.TestSuite(map(infectEpidemicCardTest, infectEpidemicCardTestcases))

##########################################################

# Collect all test cases in this file
suites = [suiteinfectEpidemicCardTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()