from outbreak import Outbreak

from contextlib import contextmanager

class OutbreakManager:
    """ Manager to control new and cascading outbreaks """
    
    def __init__(self):
        """ Initialize the Breakout Manager """
        self.outbreakCount = 0
        self.citiesInCurrentOutbreak = set()
        
    def startOutbreak(self, city, disease):
        """ Start an Outbreak """
        with self.outbreak(city, disease) as outbreak:
            outbreak.breakout()
        
        if self.outbreakCount == 0:
            self.citiesInCurrentOutbreak = set()
            
    @contextmanager
    def outbreak(self, city, disease):
        """ Perform asingle outbreak """
        self.outbreakCount += 1
        yield Outbreak(city, disease, self.citiesInCurrentOutbreak)
        self.outbreakCount -= 1