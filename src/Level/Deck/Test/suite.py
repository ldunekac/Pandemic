import unittest

from Level.Deck.Card.Test.suite import suite as card_suite
from deck_test import suite as deck_test_suite
from infection_deck_test import suite as infection_test_suite

suites = [deck_test_suite, infection_test_suite,
          card_suite]
suite = unittest.TestSuite(suites)