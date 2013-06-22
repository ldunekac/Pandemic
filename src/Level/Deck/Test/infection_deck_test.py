import unittest
from Level.Deck.infection_deck import InfectionDeck

class infectionClassTest(unittest.TestCase):
    """ Test cases of infectionClassTest """
    
    def  setUp(self):
        """  """
        self.testDeck = InfectionDeck([])

    def initDeck(self, cards):
        self.testDeck = InfectionDeck(cards)

    def testDraw(self):
        """ tests drawing feature of the deck """
        self.initDeck([1,2,3,4,5,6,7,8,9,10])

        card = self.testDeck.draw()
        assert len(self.testDeck.deck) == 9, "Test Deck did not reduce"
        assert len(self.testDeck.discardPile) == 1, "card was not added to the discard pile" 
        assert self.testDeck.discardPile[0] == card, "Card in the discardPile is not the same card that was drawned"
        card = self.testDeck.draw()
        assert len(self.testDeck.deck) == 8, "Test Deck did not reduce"
        assert len(self.testDeck.discardPile) == 2, "card was not added to the discard pile" 
        

    def testIntensify(self):
        self.initDeck([1,2,3,4,5,6,7,8,9,0])

        self.testDeck.draw()
        self.testDeck.draw()
        self.testDeck.draw()
        self.testDeck.draw()
        self.testDeck.draw()

        assert len(self.testDeck.discardPile) == 5, "Draw function did not put cards in discard pile"
        assert len(self.testDeck.deck) == 5, "Draw function did not remove the cards from the deck"
        self.testDeck.intensify()
        assert len(self.testDeck.discardPile) == 0, "Not all discard cards returned to the deck"
        assert len(self.testDeck.deck) == 10, "Not all cards placed in deck"
        assert self.testDeck.deck is not [1,2,3,4,5,6,7,8,9,0], "Cards were not randomized when placed on deck"
        #print self.testDeck.deck

    def testIntensifyEmpytList(self):
        self.testDeck = InfectionDeck([])
        self.testDeck.intensify()
        assert len(self.testDeck.deck) == 0, "Test deck is not empty"
        assert len(self.testDeck.discardPile) == 0, "DiscardPile not empty"

# Collect all test cases in this class
testcasesinfection = ["testDraw", "testIntensify", "testIntensifyEmpytList"]
suiteinfection = unittest.TestSuite(map(infectionClassTest, testcasesinfection))

##########################################################

# Collect all test cases in this file
suites = [suiteinfection]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()