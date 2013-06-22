import unittest
from Level.Deck.deck import Deck

class draw(unittest.TestCase):
    """ Test cases of draw """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.testDeck = Deck([99])
        
    def testOneCard(self):
        """ Test that ... """
        self.testDeck.draw()
        assert(len(self.testDeck.deck) == None, "Test deck of one element did not remove a card when drawned")

# Collect all test cases in this class
testcasesDraw = ["testOneCard"]
suiteDraw = unittest.TestSuite(map(draw, testcasesDraw))

##########################################################

# Collect all test cases in this file
suites = [suiteDraw]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()