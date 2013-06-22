
class CityView:
    """ Represents the view for a city """
    
    def __init__(self, city):
        """ Initialize the view """
        self.city = city
        
    def display(self):
        """ Display the city details """
        print self.city, "\r"
        print
        self.displayDiseaseCounts()
        print "Adjacent to:", "\r"
        for adjacentCity in self.city.adjacentCities:
            print adjacentCity, "\r"
            
    def displayDiseaseCounts(self):
        """ Display the disease counts """
        if len(self.city.diseaseCounts) == 0:
            print "Not Diseased", "\r"
        else:
            for disease in self.city.diseaseCounts:
                print "Disease Count:", self.city.diseaseCounts[disease], "\r"
        print 