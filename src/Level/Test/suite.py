import unittest

from Level.Test.infection_rate_test import suite as infection_rate_suite
from level_test import suite as level_test_suite

from Level.City.Test.suite import suite as city_suite
from Level.Deck.Test.suite import suite as deck_suite
from Level.Player.Test.suite import suite as player_suite
from Level.Disease.Test.suite import suite as diease_suite

suites = [deck_suite,
          level_test_suite,
          player_suite,
          diease_suite,
          city_suite,
          infection_rate_suite]
suite = unittest.TestSuite(suites)