import unittest

from deck_test import suite as deck_test_suite
from infection_deck_test import suite as infection_test_suite

suites = [deck_test_suite, infection_test_suite]
suite = unittest.TestSuite(suites)