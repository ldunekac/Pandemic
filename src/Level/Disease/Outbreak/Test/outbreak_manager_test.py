import unittest

from Level.Disease.Outbreak.outbreak_manager import OutbreakManager

class outbreak(unittest.TestCase):
    """ Test cases of outbreak """
    
    def  setUp(self):
        """ Build the Outbreak Manager for the test """
        self.outbreakManager = OutbreakManager()
        
    def outbreakCounter(self):
        """ Test that the outbreak counter is properly set """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.outbreakCount == 1, "Outbreak Counter should have increased to 1"
        assert self.outbreakManager.outbreakCount == 0, "Outbreak Counter should have decreased to 0"
        
    def multipleOutbreaks(self):
        """ Test that the outbreak counter is properly set when there are multiple outbreaks """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.outbreakCount == 1, "Outbreak Counter should have increased to 1"
            with self.outbreakManager.outbreak(None, None) as outbreak:
                assert self.outbreakManager.outbreakCount == 2, "Outbreak Counter should have increased to 2"
            assert self.outbreakManager.outbreakCount == 1, "Outbreak Counter should have decreased back to 1"
        assert self.outbreakManager.outbreakCount == 0, "Outbreak Counter should have decreased to 0"

# Collect all test cases in this class
testcasesOutbreak = ["outbreakCounter", "multipleOutbreaks"]
suiteOutbreak = unittest.TestSuite(map(outbreak, testcasesOutbreak))

##########################################################

# Collect all test cases in this file
suites = [suiteOutbreak]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()