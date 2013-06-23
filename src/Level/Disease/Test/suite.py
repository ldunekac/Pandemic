import unittest

from Level.Disease.Test.disease_test import suite as diease_suite

suites = [diease_suite]
suite = unittest.TestSuite(suites)