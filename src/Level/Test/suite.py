import unittest

from city_test import suite as city_test_suite
from level_test import suite as level_test_suite

from Level.Deck.Test.suite import suite as deck_suite

suites = [city_test_suite, 
          deck_suite,
          level_suite]
suite = unittest.TestSuite(suites)