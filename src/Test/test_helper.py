from Level.City.city import City
from Level.City.city_infection_delegate import CityInfectionDelegate
from Level.Disease.disease import Disease

def BuildCity(name="Blah", disease=Disease()):
    """ Build a city """
    return City(name, disease)
    
def BuildCityInfectionDelegate(city=BuildCity()):
    """ Build a city infection delegate """
    return CityInfectionDelegate(city)

def GetCityList():
    """ Returns a list of cities """
    disease = Disease()
        
    city1 = BuildCity("Blah1", disease)
    city2 = BuildCity("Blah2", disease)
    city3 = BuildCity("Blah3", disease)
    city1.addAdjacentCity(city2)
    city1.addAdjacentCity(city3)
    
    return [city1, city2, city3]