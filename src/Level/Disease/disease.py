from Level.level_settings import TheLevelSettings

class Disease:
    """ Represents a disease in a level of the game """
    
    def __init__(self):
        self.cubeCount = TheLevelSettings.MAX_INFECTIONS_PER_DISEASE
        self.cured = False
        self.eradicated = False

    def removeCubes(self, amount):
        self.cubeCount -= amount
        if self.cubeCount < 0:
            self.cubeCount = 0

    def addCubes(self, amount):
        if amount > TheLevelSettings.MAX_INFECTIONS_PER_DISEASE_IN_CITY:
            amount = TheLevelSettings.MAX_INFECTIONS_PER_DISEASE_IN_CITY

        self.cubeCount += amount
        self.checkIfEradicated()

    def cure(self):
        self.cured = True
        self.checkIfEradicated()

    def isCured(self):
        return self.cured

    def isEradicated(self):
        return self.eradicated

    def checkIfEradicated(self):
        """ Check if the disease has been eradicated """
        if self.cured and self.cubeCount == TheLevelSettings.MAX_INFECTIONS_PER_DISEASE:
            self.eradicated = True 