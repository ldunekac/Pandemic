
class CityView:
    """ Represents the view for a city """
    
    def __init__(self, city):
        """ Initialize the view """
        self.city = city
        
    def display(self):
        """ Display the city details """
        print city, "\r"
        print
        print "Disease Count:", city.diseaseCount[city.diseaseCount.keys()[0]], "\r"
        print 
        print "Adjacent to:", "\r"
        for adjacentCity in city.adjacentCities:
            print adjacentCity, "\r"