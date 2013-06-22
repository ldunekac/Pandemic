
class CitiesView:
    """ Represents the view of the cities """
    
    def __init__(self, cities):
        """ Initialize the Cities View """
        self.cities = cities
        
    def display(self):
        """ Display all the cities """
        for city in self.cities:
            print city, "\r"