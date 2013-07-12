import unittest

from city_treatment_delegate_test import suite as city_treatment_delegate_suite
from city_infection_delegate_test import suite as city_infection_delegate_suite
from city_test import suite as city_suite

suites = [city_suite,
          city_infection_delegate_suite,
          city_treatment_delegate_suite]
suite = unittest.TestSuite(suites)