from card import card
from Level.City.city_infection_delegate import CityInfectionDelegate.MAX_INFECTIONS_PER_DISEASE as maxDiseaseCount

"""
Draw bottom card
"""

"""
TO see 

The infection deck
"""

class EpidemicCard(Card):
    TYPE = "EPIDEMIC"

    def __init__(self):
        Card.__init__(self, infectionDeck, infectionRateManager)
        self.infectionDeck = infectionDeck
        self.infectionRateManager = infectionRateManager

    def onDraw(self):
        "Preforms the action/event when the card is drawned from the deck"
        self.increase()
        self.infect()
        self.intensify()        

    def onPlay(self):
        "Preforms the action/event when the card is played"
        "Does nothing sense the card is played when drawned"

    def increase(self):
        """ moves the infection rate marker forward 1 space """
        self.infectionRate.increaseInfectionLevel()

    def infect(self):
        """ Draws the bottom card from the infection deck
        and infects that city with the max amount of infections """
        city = self.infectionRateManager.drawBottom()
        city.infect(maxDiseaseCount)

    def intensify(self):
        self.infectionDeck.intensify()
        self.infectionRateManager.increaseInfectionRate()

