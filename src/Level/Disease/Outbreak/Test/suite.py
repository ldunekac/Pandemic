import unittest

from outbreak_manager_test import suite as outbreak_manager_suite
from outbreak_test import suite as outbreak_suite

suites = [outbreak_suite,
          outbreak_manager_suite]
suite = unittest.TestSuite(suites)