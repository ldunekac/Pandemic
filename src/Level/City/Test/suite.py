import unittest

from city_infection_delegate_test import suite as city_infection_delegate_suite
from city_test import suite as city_suite

suites = [city_suite,
          city_infection_delegate_suite]
suite = unittest.TestSuite(suites)