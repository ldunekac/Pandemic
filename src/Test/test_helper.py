from Level.City.city import City
from Level.Disease.disease import Disease

def GetCityList():
    """ Returns a list of cities """
    disease = Disease()
        
    city1 = City("Blah1", disease)
    city2 = City("Blah2", disease)
    city3 = City("Blah3", disease)
    city1.addAdjacentCity(city2)
    city1.addAdjacentCity(city3)
    
    return [city1, city2, city3]