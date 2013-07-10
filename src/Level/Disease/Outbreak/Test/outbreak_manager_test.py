import unittest

from Level.Disease.Outbreak.outbreak_manager import OutbreakManager

from Test.test_helper import GetCityList

class outbreak(unittest.TestCase):
    """ Test cases of outbreak """
    
    def  setUp(self):
        """ Build the Outbreak Manager for the test """
        self.outbreakManager = OutbreakManager()
        
    def concurrentOutbreakCounter(self):
        """ Test that the concurrent outbreak counter is properly set """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.concurrentOutbreakCount == 1, "Concurrent Outbreak Counter should have increased to 1"
        assert self.outbreakManager.concurrentOutbreakCount == 0, "Concurrent Outbreak Counter should have decreased to 0"
        
    def concurrentOutbreakCounter_Multiple(self):
        """ Test that the concurrent outbreak counter is properly set when there are multiple outbreaks """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.concurrentOutbreakCount == 1, "Concurrent Outbreak Counter should have increased to 1"
            with self.outbreakManager.outbreak(None, None) as outbreak:
                assert self.outbreakManager.concurrentOutbreakCount == 2, "Concurrent Outbreak Counter should have increased to 2"
            assert self.outbreakManager.concurrentOutbreakCount == 1, "Concurrent Outbreak Counter should have decreased back to 1"
        assert self.outbreakManager.concurrentOutbreakCount == 0, "Concurrent Outbreak Counter should have decreased to 0"
        
    def totalOutbreakCounter(self):
        """ Test that the total outbreak counter is properly set """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.totalOutbreaks == 1, "Total Outbreak Counter should have increased to 1"
        assert self.outbreakManager.totalOutbreaks == 1, "Toatl Outbreak Counter should stay at 1"
        
    def totalOutbreakCounter_Multiple(self):
        """ Test that the total outbreak counter is properly set when there are multiple outbreaks """
        with self.outbreakManager.outbreak(None, None) as outbreak:
            assert self.outbreakManager.totalOutbreaks == 1, "Total Outbreak Counter should have increased to 1"
            with self.outbreakManager.outbreak(None, None) as outbreak:
                assert self.outbreakManager.totalOutbreaks == 2, "Total Outbreak Counter should have increased to 2"
            assert self.outbreakManager.totalOutbreaks == 2, "Total Outbreak Counter should stay at 2"
        assert self.outbreakManager.totalOutbreaks == 2, "Total Outbreak Counter should stay at 2"

# Collect all test cases in this class
testcasesOutbreak = ["concurrentOutbreakCounter", "concurrentOutbreakCounter_Multiple", "totalOutbreakCounter", "totalOutbreakCounter_Multiple"]
suiteOutbreak = unittest.TestSuite(map(outbreak, testcasesOutbreak))

##########################################################

class startOutbreak(unittest.TestCase):
    """ Test cases of startOutbreak """
    
    def  setUp(self):
        """ Build the Outbreak Manager and Cities for the test """
        self.outbreakManager = OutbreakManager()
        self.cities = GetCityList()
        
    def singleOutbreak_ConcurrentOutbreakCount(self):
        """ Test that a single outbreak has the concurrentOutbreakCount set properly"""
        self.startOutbreak()
        assert self.outbreakManager.concurrentOutbreakCount == 0, "Outbreak Count should always be zero after a single infection"
        
    def concurrentOutbreakCount(self):
        """ Test that a single outbreak has the concurrentOutbreakCount set properly"""
        self.startOutbreak()
        assert self.outbreakManager.concurrentOutbreakCount == 0, "Outbreak Count should always be zero after a single infection"
        
    def startOutbreak(self):
        """ Start the outbreak """
        self.outbreakManager.startOutbreak(self.cities[0], self.cities[0].disease)

# Collect all test cases in this class
testcasesStartOutbreak = ["concurrentOutbreakCount"]
suiteStartOutbreak = unittest.TestSuite(map(startOutbreak, testcasesStartOutbreak))

##########################################################

# Collect all test cases in this file
suites = [suiteOutbreak,
          suiteStartOutbreak]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()