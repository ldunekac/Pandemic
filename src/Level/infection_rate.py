

class InfectionRate:

    def __init__(self):
        """ Initalize the Infection Rate """
        self.infectionTable = [2,2,2,3,3,4,4]
        self.currentInfectionRateIterator = 0 # this is the location in the infactionrate infectionTable

    def getInfectionRate(self):
        return self.infectionTable[self.currentInfectionRateIterator]

    def increaseInfectionRate(self):
        if not self.currentInfectionRateIterator >= len(self.infectionTable) - 1:
            self.currentInfectionRateIterator += 1