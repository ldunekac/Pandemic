from Level.level_settings import TheLevelSettings

class ResearchStationManager:

    def __init__(self, initialCity = None):
        """ initializes the citys with with an initial city"""
        if initialCity == None:
            self.cities = []
        else:
            self.cities = [initialCity]

    def canAddResearchStation(self):
        """ Returns true if more research stations can be added """
        return len(self.cities) < TheLevelSettings.MAX_RESEARCH_STATIONS

    def removeResearchStation(self,city):
        """ Removes a research statio from the city """
        self.cities.remove(city)

    def addResearchStation(self, city):
        """ Addes a research station to the city """
        if self.canAddResearchStation():
            self.cities.append(city)

    def hasResearchStationIn(self, city):
        """ Retruns true if the city contains a research station"""
        return (city in cities)

    def getCitiesWithResearchStations(self):
        return self.cities