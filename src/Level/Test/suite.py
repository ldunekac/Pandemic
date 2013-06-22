import unittest

from city_test import suite as city_test_suite
from level_test import suite as level_test_suite

suites = [city_test_suite, 
          level_test_suite]
suite = unittest.TestSuite(suites)