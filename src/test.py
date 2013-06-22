import unittest

import Level.Test.suite as level_suite

# Collect all the test suites
suites = [level_suite.suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
