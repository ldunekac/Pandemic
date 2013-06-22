import unittest
from Level.Deck.deck import Deck

class draw(unittest.TestCase):
    """ Test cases of draw """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.testDeck = Deck([])
        
    def makeOneElementDeck(self):
        self.testDeck = Deck([99])

    def makeTwoElementDeck(self):
        self.testDeck = Deck([1,2])

    def testOneCard(self):
        """ Test that ... """
        self.testDeck.draw()
        assert len(self.testDeck.deck) == 0, "Test deck of one element did not remove a card when drawned"

    def testSeveralCards(self):
        self.makeTwoElementDeck()
        card = self.testDeck.draw()
        #print card
        assert (card == 2), "Card given is not the last card in the deck"

    def testDiscard(self):
        self.testDeck.discard(7)
        assert 7 in self.testDeck.discardPile, "Card was not inserted into the discard list"

# Collect all test cases in this class
testcasesDraw = ["testOneCard", "testSeveralCards", "testDiscard"]
suiteDraw = unittest.TestSuite(map(draw, testcasesDraw))

##########################################################

# Collect all test cases in this file
suites = [suiteDraw]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()