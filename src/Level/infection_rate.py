

class InfectionRate:

    def __init__(self):
        """ Initalize the Infection Rate """
        self.infectionTable = [2,2,2,3,3,4,4]
        self.index = 0 # this is the location in the infectionTable

    def getInfectionRate(self):
        return self.infectionTable[self.index]

    def increaseInfectionRate(self):
        if not self.index >= len(self.infectionTable) - 1:
            self.index += 1