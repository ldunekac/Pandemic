import unittest

from city_test import suite as city_test_suite
from Level.Deck.Test.suite import suite as deck_suite

suites = [city_test_suite, deck_suite]
suite = unittest.TestSuite(suites)