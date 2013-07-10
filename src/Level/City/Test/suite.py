import unittest

from city_test import suite as city_suite

suites = [city_suite]
suite = unittest.TestSuite(suites)