import unittest

from Level.Disease.Test.disease_test import suite as diease_suite
from Level.Disease.Outbreak.Test.suite import suite as outbreak_suite

suites = [diease_suite,
          outbreak_suite]
suite = unittest.TestSuite(suites)