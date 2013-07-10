from outbreak import Outbreak

from contextlib import contextmanager

class OutbreakManager:
    """ Manager to control new and cascading outbreaks """
    
    def __init__(self):
        """ Initialize the Breakout Manager """
        self.reset()
        
    def startOutbreak(self, city, disease):
        """ Start an Outbreak """
        with self.outbreak(city, disease) as outbreak:
            outbreak.breakout()
        
        if self.concurrentOutbreakCount == 0:
            self.citiesInCurrentOutbreak = set()
            
    @contextmanager
    def outbreak(self, city, disease):
        """ Perform a single outbreak """
        self.concurrentOutbreakCount += 1
        self.totalOutbreaks += 1
        yield Outbreak(city, disease, self.citiesInCurrentOutbreak)
        self.concurrentOutbreakCount -= 1
        
    def reset(self):
        """ Reset the Outbreak Manager """
        self.concurrentOutbreakCount = 0
        self.totalOutbreaks = 0
        self.citiesInCurrentOutbreak = set()
        
        
TheOutbreakManager = OutbreakManager()