import unittest
from Level.city import City
from Level.Player.player import Player
from Level.Disease.disease import Disease

class PlayerMove(unittest.TestCase):
    """ Test cases of PlayerMove """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def movePlayer(self):
        """ Test that ... """
        disease = Disease()
        city = City("Luke's confiement center",disease)
        imporvedCity = City("Luke's habilitation center", disease)
        player = Player(city)
        player.moveTo(imporvedCity)
        assert(player.city == imporvedCity)


# Collect all test cases in this class
testcasesPlayerMove = ["movePlayer"]
suitePlayerMove = unittest.TestSuite(map(PlayerMove, testcasesPlayerMove))

##########################################################

class CureDisease(unittest.TestCase):
    """ Test cases of PlayerMove """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def cureDisease(self):
        """ Test that ... """
        disease = Disease()
        city = City("Luke's confiement center",disease)
        city.diseaseCounts[disease] = 5

        player = Player(city)

        player.cureDisease()

        assert city.diseaseCounts[disease] == 4, "Player did not cure city of a disease"

# Collect all test cases in this class
testcasesCureDisease = ["cureDisease"]
suiteCureDisease = unittest.TestSuite(map(CureDisease, testcasesCureDisease))

##########################################################



# Collect all test cases in this file
suites = [suitePlayerMove, suiteCureDisease]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()