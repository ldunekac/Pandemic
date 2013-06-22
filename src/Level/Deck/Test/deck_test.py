import unittest
from Level.Deck.deck import Deck

class init(unittest.TestCase):
    """ Test cases of init """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.myList = []
        self.testDeck = Deck(self.myList)

    def copyDeckArgument(self):
        """ Ensure the Deck's deck variable is a copy of the original deck argument """
        assert self.testDeck.deck is not self.myList, "The Deck should have a copy of the original list"

# Collect all test cases in this class
testcasesInit = ["copyDeckArgument"]
suiteInit = unittest.TestSuite(map(init, testcasesInit))

##########################################################

class draw(unittest.TestCase):
    """ Test cases of draw """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.testDeck = Deck([])
        
    def makeOneElementDeck(self):
        self.testDeck = Deck([99])

    def makeTwoElementDeck(self):
        self.testDeck = Deck([1,2])

    def emptyDeck(self):
        self.testDeck = Deck([])

        card = self.testDeck.draw()

        assert card == None, "a deck with no cards does not return None"

    def testOneCard(self):
        """ Test that ... """
        self.testDeck.draw()
        assert len(self.testDeck.deck) == 0, "Test deck of one element did not remove a card when drawned"

    def testSeveralCards(self):
        self.makeTwoElementDeck()
        card = self.testDeck.draw()
        #print card
        assert (card == 2), "Card given is not the last card in the deck"

# Collect all test cases in this class
testcasesDraw = ["testOneCard", "testSeveralCards",
                "emptyDeck"]
suiteDraw = unittest.TestSuite(map(draw, testcasesDraw))

##########################################################

class discard(unittest.TestCase):
    """ Test cases of discarding cards """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.testDeck = Deck([])
    
    def testDiscard(self):
        self.testDeck.discard(7)
        assert 7 in self.testDeck.discardPile, "Card was not inserted into the discard list"
        

# Collect all test cases in this class
testcasesDiscard = ["testDiscard"]
suiteDiscard = unittest.TestSuite(map(discard, testcasesDiscard))

##########################################################

# Collect all test cases in this file
suites = [suiteInit, suiteDraw, suiteDiscard]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()