import unittest

from Level.Disease.Test.disease_test import suite as diease_suite
from Level.Disease.Breakout.Test.suite import suite as breakout_suite

suites = [diease_suite,
          breakout_suite]
suite = unittest.TestSuite(suites)