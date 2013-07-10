
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
        self.checkIfEradicated()

    def cureDisease(self):
        self.cured = True
        self.checkIfEradicated()

    def isCured(self):
        return self.cured

    def isEradicated(self):
        return self.eradicated

    def checkIfEradicated(self):
        """ Check if the disease has been eradicated """
        if self.cubeCount == self.AMOUNT_OF_DISEASE:
            self.eradicated = True 