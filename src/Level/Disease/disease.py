
class Disease:
    """ Represents a disease in a level of the game """    
    AMOUNT_OF_DISEASE = 24

    def __init__(self):
        self.cubeCount = self.AMOUNT_OF_DISEASE
        self.cured = False
        self.eradicated = False

    def removeCubes(self, amount):
        self.cubeCount -= amount
        if self.cubeCount < 0:
            self.cubeCount = 0

    def addCubes(self, amount):
        if amount > 3:
            amount = 3

        self.cubeCount += amount
        if self.cured and self.cubeCount == self.AMOUNT_OF_DISEASE:
            self.eradicated = True

    def cureDisease(self):
        self.cured = True
        if self.cubeCount == self.AMOUNT_OF_DISEASE:
            self.eradicated = True

    def isCured(self):
        return self.cured

    def isEradicated(self):
        return self.eradicated
