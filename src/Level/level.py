from Level.City.city import City
from Level.Deck.infection_deck import InfectionDeck
from Level.Deck.player_deck import PlayerDeck
from Level.Deck.Card.city_card import CityCard
from Level.Disease.disease import Disease
from Level.Player.player import Player

class Level:
    """ Represents a single Level of the Expanded Pandemic Game """
    
    def __init__(self):
        """ Initialize the Level """
        self.diseases = []
        self.cities = []
        
        self.infectionDeck = None
        self.playerDeck = None
        
        self.players = []

        self.setup()
        
    def setup(self):
        """ Setup the level for the start of the game """
        self.setupCities()
        self.setupInfectionDeck()
        self.setupPlayerDeck()
        self.setupPlayers()
        self.addEpidemics()
        
    def setupCities(self):
        """ Setup the cities """
        disease = Disease()
        self.diseases.append(disease)
        
        sanFrancisco = City("San Francisco", disease)
        chicago = City("Chicago", disease)
        atlanta = City("Atlanta", disease)
        montreal = City("Montreal", disease)
        newYork = City("New York", disease)
        washington = City("Washington", disease)
        london = City("London", disease)
        madrid = City("Madrid", disease)
        essen = City("Essen", disease)
        paris = City("Paris", disease)
        stPetersburg = City("St. Petersburg", disease)
        milan = City("Milan", disease)
        self.startingCity = atlanta
        
        self.cities.append(chicago)
        self.cities.append(sanFrancisco)
        self.cities.append(atlanta)
        self.cities.append(montreal)
        self.cities.append(newYork)
        self.cities.append(washington)
        self.cities.append(london)
        self.cities.append(madrid)
        self.cities.append(essen)
        self.cities.append(paris)
        self.cities.append(stPetersburg)
        self.cities.append(milan)
        
        self.makeCitiesAdjacent(chicago, sanFrancisco)
        self.makeCitiesAdjacent(chicago, atlanta)
        self.makeCitiesAdjacent(chicago, montreal)
        self.makeCitiesAdjacent(atlanta, washington)
        self.makeCitiesAdjacent(montreal, newYork)
        self.makeCitiesAdjacent(montreal, washington)
        self.makeCitiesAdjacent(newYork, washington)
        self.makeCitiesAdjacent(newYork, london)
        self.makeCitiesAdjacent(newYork, madrid)
        self.makeCitiesAdjacent(london, essen)
        self.makeCitiesAdjacent(london, paris)
        self.makeCitiesAdjacent(madrid, paris)
        self.makeCitiesAdjacent(essen, paris)
        self.makeCitiesAdjacent(essen, stPetersburg)
        self.makeCitiesAdjacent(essen, milan)
        self.makeCitiesAdjacent(paris, milan)
        
    def setupInfectionDeck(self):
        """ Setup the Infection Deck """
        self.infectionDeck = InfectionDeck(self.cities)
        self.infectionDeck.shuffle()
        
        for infectionAmount in [3,2,1]:
            for i in range(3):
                city = self.infectionDeck.draw()
                city.infect(infectionAmount)
                
    def setupPlayerDeck(self):
        """ Setup the player Deck """
        cityCards = []
        for city in self.cities:
            cityCards.append(CityCard(city))
        
        self.playerDeck = PlayerDeck(cityCards)
        self.playerDeck.shuffle()
                
    def setupPlayers(self):
        """ Setup Players """
        # Choose roles
        # Add Players to list
        player = Player(self.startingCity)
        self.players.append(player)
        # Give each 4 cards in their hand
        for i in range(4):
            card = self.playerDeck.draw()
            player.addCardToHand(card)
        
    def addEpidemics(self):
        """ Setup Players """
        # Add X Epidemics to the Player Deck
        
    def makeCitiesAdjacent(self, city1, city2):
        """ Make the two cities given adjacent """
        city1.addAdjacentCity(city2)
        city2.addAdjacentCity(city1)