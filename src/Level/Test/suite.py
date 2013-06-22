import unittest

from city_test import suite as city_test_suite


suites = [city_test_suite]
suite = unittest.TestSuite(suites)