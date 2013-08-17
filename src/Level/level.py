from Level.City.city import City
from Level.Deck.infection_deck import InfectionDeck
from Level.Deck.player_deck import PlayerDeck
from Level.Deck.Card.city_card import CityCard
from Level.Disease.disease import Disease
from Level.Player.player import Player
from Level.research_station_manager import ResearchStationManager


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

        self.researchStationManager = ResearchStationManager(self.startingCity)

    def getCities(self):
        return self.cities

    def getPlayers(self):
        return self.players

    def getResearchStationManager(self):
        return self.researchStationManager
        
    def setup(self):
        """ Setup the level for the start of the game """
        self.setupCities()
        self.setupInfectionDeck()
        self.setupPlayerDeck()
        self.setupPlayers()
        self.addEpidemics()
        
    def setupCities(self):
        """ Setup the cities """
        
        # Blue Dise
        disease = Disease((0,0,225))
        self.diseases.append(disease)
        
        sanFrancisco = City("San Francisco", disease,(220,310))
        chicago = City("Chicago", disease, (350,280))
        atlanta = City("Atlanta", disease,(385,340))
        montreal = City("Montreal", disease,(440,275))
        newYork = City("New York", disease, (480,300))
        washington = City("Washington", disease, (440,340))
        london = City("London", disease,(700,230))
        madrid = City("Madrid", disease,(680,310))
        essen = City("Essen", disease, (790,220))
        paris = City("Paris", disease, (770,270))
        stPetersburg = City("St. Petersburg", disease, (890,192))
        milan = City("Milan", disease,(830,260))
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

        #Yellow Cities
        disease = Disease((255,255,0))
        self.diseases.append(disease)

        losAngeles  = City("Los Angeles", disease, (235,360))
        miami       = City("Miami", disease,(410,390))
        mexicoCity  = City("Mexico City", disease, (330,420))
        bogota      = City("Bogota", disease, (435,490))
        lima        = City("Lima", disease, (400, 570))
        santiago    = City("Santiago", disease, (410,690))
        buenosAires = City("Buenos Aires", disease, (510, 685))
        saoPaulo    = City("Sao Paulo", disease, (570,610))
        lagos       = City("Lagos", disease, (750,480))
        khartoum    = City("Khartoum", disease, (880,460))
        kinshasa    = City("Kinshasa", disease, (815, 540))
        johannesburg =City("Johannesburg", disease, (870,620))

        self.cities.append(losAngeles)
        self.cities.append(miami)
        self.cities.append(mexicoCity)
        self.cities.append(bogota)
        self.cities.append(lima)
        self.cities.append(santiago)
        self.cities.append(buenosAires)
        self.cities.append(saoPaulo)
        self.cities.append(lagos)
        self.cities.append(khartoum)
        self.cities.append(kinshasa)
        self.cities.append(johannesburg)

        # Connecting the yellow Cities witht he blue cities
        self.makeCitiesAdjacent(losAngeles, sanFrancisco)
        self.makeCitiesAdjacent(losAngeles, chicago)
        self.makeCitiesAdjacent(mexicoCity, chicago)
        self.makeCitiesAdjacent(miami, atlanta)
        self.makeCitiesAdjacent(miami, washington)
        self.makeCitiesAdjacent(saoPaulo, madrid)

        # Connect the yellow citys to yellow Cities
        self.makeCitiesAdjacent(losAngeles, mexicoCity)
        self.makeCitiesAdjacent(mexicoCity, miami)
        self.makeCitiesAdjacent(mexicoCity, lima)
        self.makeCitiesAdjacent(mexicoCity, bogota)
        self.makeCitiesAdjacent(miami, bogota)
        self.makeCitiesAdjacent(bogota, lima)
        self.makeCitiesAdjacent(bogota, buenosAires)
        self.makeCitiesAdjacent(bogota, saoPaulo)
        self.makeCitiesAdjacent(lima, santiago)
        self.makeCitiesAdjacent(buenosAires, saoPaulo)
        self.makeCitiesAdjacent(saoPaulo, lagos)
        self.makeCitiesAdjacent(lagos, kinshasa)
        self.makeCitiesAdjacent(lagos, khartoum)
        self.makeCitiesAdjacent(khartoum, kinshasa)
        self.makeCitiesAdjacent(khartoum, johannesburg)
        self.makeCitiesAdjacent(kinshasa, johannesburg)

        # Zombie Cities
        disease = Disease((0,0,0))
        self.diseases.append(disease)

        algiers     = City("Algiers",disease, (790,360))
        cairo       = City("Cairo", disease, (860, 375))
        istanbul    = City("Istanbul", disease, (880,305))
        baghdad     = City("Baghdad", disease, (940, 350))
        moscow      = City("Moscow", disease, (930, 240))
        riyrdh      = City("Riyrad", disease, (960, 430))
        tehran      = City("Tehran", disease, (1020, 295))
        karachi     = City("Karachi", disease, (1040, 380))
        mumbai      = City("Mumbai", disease, (1050, 440))
        delhi       = City("Delhi", disease, (1100, 340))
        chennai     = City("Chennai", disease, (1120, 480))
        kolkata     = City("Kolkata", disease, (1170, 360))

        self.cities.append(algiers)
        self.cities.append(cairo)
        self.cities.append(istanbul)
        self.cities.append(baghdad)
        self.cities.append(moscow)
        self.cities.append(riyrdh)
        self.cities.append(tehran)
        self.cities.append(karachi)
        self.cities.append(mumbai)
        self.cities.append(delhi)
        self.cities.append(chennai)
        self.cities.append(kolkata)        

        # connect yellow and Zombies
        self.makeCitiesAdjacent(cairo,khartoum)

        # connect zombies and blue
        self.makeCitiesAdjacent(stPetersburg, moscow)
        self.makeCitiesAdjacent(stPetersburg, istanbul)
        self.makeCitiesAdjacent(milan, istanbul)
        self.makeCitiesAdjacent(paris, algiers)
        self.makeCitiesAdjacent(madrid, algiers)

        # connect Zombie cities

        self.makeCitiesAdjacent(algiers, cairo)
        self.makeCitiesAdjacent(algiers, istanbul)
        self.makeCitiesAdjacent(cairo, istanbul)
        self.makeCitiesAdjacent(cairo, baghdad)
        self.makeCitiesAdjacent(cairo, riyrdh)
        self.makeCitiesAdjacent(istanbul, baghdad)
        self.makeCitiesAdjacent(istanbul, moscow)
        self.makeCitiesAdjacent(moscow, tehran)
        self.makeCitiesAdjacent(baghdad, tehran)
        self.makeCitiesAdjacent(baghdad, karachi)
        self.makeCitiesAdjacent(baghdad, riyrdh)
        self.makeCitiesAdjacent(riyrdh, karachi)
        self.makeCitiesAdjacent(tehran, karachi)
        self.makeCitiesAdjacent(tehran, delhi)
        self.makeCitiesAdjacent(karachi, delhi)
        self.makeCitiesAdjacent(karachi, mumbai)
        self.makeCitiesAdjacent(mumbai, delhi)
        self.makeCitiesAdjacent(mumbai, chennai)
        self.makeCitiesAdjacent(delhi, kolkata)
        self.makeCitiesAdjacent(delhi, chennai)
        self.makeCitiesAdjacent(chennai, kolkata)

        # Red Cities
        disease = Disease((255,0,0))
        self.diseases.append(disease)

        beijing     = City("Beijing", disease, (1230, 270))
        seoul       = City("Seoul", disease, (1320, 270))
        shanghai    = City("Shanghai", disease, (1230, 340))
        tokyo       = City("Tokyo", disease, (1400, 310))
        hongKong    = City("Hong Kong", disease, (1240, 400))
        taipei      = City("Taipei", disease, (1320,390))
        osaka       = City("Osaka", disease, (1390, 360))
        bangkok     = City("Bangkok", disease, (1190, 445))
        hoChiMinhCity = City("Ho Chi Minh City", disease, (1250, 510))
        manila      = City("Manila", disease, (1340, 500))
        jakarta     = City("Jakarta", disease, (1190, 555))
        sydney      = City("Sydney", disease, (1395, 680))

        self.cities.append(beijing)
        self.cities.append(seoul)
        self.cities.append(shanghai)
        self.cities.append(tokyo)
        self.cities.append(hongKong)
        self.cities.append(taipei)
        self.cities.append(osaka)
        self.cities.append(bangkok)
        self.cities.append(hoChiMinhCity)
        self.cities.append(manila)
        self.cities.append(jakarta)
        self.cities.append(sydney)

        # Connect zombie and red
        self.makeCitiesAdjacent(kolkata, bangkok)
        self.makeCitiesAdjacent(kolkata, hongKong)
        self.makeCitiesAdjacent(chennai, bangkok)
        self.makeCitiesAdjacent(chennai, jakarta) 

        # Connect red with bule
        self.makeCitiesAdjacent(tokyo, sanFrancisco)
        self.makeCitiesAdjacent(manila, sanFrancisco)
        self.makeCitiesAdjacent(sydney, losAngeles)
        
        # Connect red with red
        self.makeCitiesAdjacent(beijing, seoul)
        self.makeCitiesAdjacent(beijing, shanghai)
        self.makeCitiesAdjacent(seoul, shanghai)
        self.makeCitiesAdjacent(seoul, tokyo)
        self.makeCitiesAdjacent(shanghai, tokyo)
        self.makeCitiesAdjacent(shanghai, hongKong)
        self.makeCitiesAdjacent(shanghai, taipei)
        self.makeCitiesAdjacent(tokyo, osaka)
        self.makeCitiesAdjacent(osaka, taipei)
        self.makeCitiesAdjacent(taipei,hongKong)
        self.makeCitiesAdjacent(taipei, manila)
        self.makeCitiesAdjacent(hongKong, bangkok)
        self.makeCitiesAdjacent(hongKong, hoChiMinhCity)
        self.makeCitiesAdjacent(hongKong, manila)
        self.makeCitiesAdjacent(bangkok, hoChiMinhCity)
        self.makeCitiesAdjacent(bangkok, jakarta)
        self.makeCitiesAdjacent(hoChiMinhCity, manila)
        self.makeCitiesAdjacent(hoChiMinhCity, jakarta)
        self.makeCitiesAdjacent(manila, sydney)
        self.makeCitiesAdjacent(jakarta, sydney)      

        
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
        player1 = Player(self.startingCity)
        player2 = Player(self.startingCity)
        player3 = Player(self.startingCity)
        player4 = Player(self.startingCity)
        self.players.append(player1)
        self.players.append(player2)
        self.players.append(player3)
        self.players.append(player4)

        # Give each 4 cards in their hand
        for i in range(4):
            card = self.playerDeck.draw()
            player1.addCardToHand(card)
            card = self.playerDeck.draw()
            player2.addCardToHand(card)
            card = self.playerDeck.draw()
            player3.addCardToHand(card)
            card = self.playerDeck.draw()
            player4.addCardToHand(card)

        
    def addEpidemics(self):
        """ Setup Players """
        # Add X Epidemics to the Player Deck
        
    def makeCitiesAdjacent(self, city1, city2):
        """ Make the two cities given adjacent """
        city1.addAdjacentCity(city2)
        city2.addAdjacentCity(city1)