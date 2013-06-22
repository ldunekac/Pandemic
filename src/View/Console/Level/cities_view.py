
class CitiesView:
    """ Represents the view of the cities """
    MAX_CITIES = 10
    
    def __init__(self, cities):
        """ Initialize the Cities View """
        self.cities = cities
        
        self.section = 0
        
    def display(self):
        """ Display all the cities """
        self.displayHeader()
        
        value = 0
        for city in self.cities[self.section*CitiesView.MAX_CITIES:self.section*CitiesView.MAX_CITIES+CitiesView.MAX_CITIES]:
            print "{0}: {1}\r".format(value, city)
            value += 1
            
    def displayHeader(self):
        """ Disaply Header Information """
        print "Cities:", len(self.cities), "\r"
        
        start = self.section*CitiesView.MAX_CITIES
        end = self.section*CitiesView.MAX_CITIES+CitiesView.MAX_CITIES-1
        
        if end > len(self.cities):
            end = len(self.cities)-1
        
        print "Showing Cities: {0}-{1}\r".format(start, end)
        if end < len(self.cities)-1:
            print "n: Show Next Section\r"
        if self.section > 0:
            print "p: Show Previous Section\r"
        print
        
    def getCity(self, index):
        """ Return the city in the current section with the given index """
        actualIndex = self.section*CitiesView.MAX_CITIES + index
        if actualIndex < len(self.cities):
            return self.cities[actualIndex]
        
    def selectNextSection(self):
        """ Select the next section """ 
        if self.section < len(self.cities)%CitiesView.MAX_CITIES:
            self.section += 1
        
    def selectPreviousSection(self):
        """ Select the previous section """ 
        if self.section > 0:
            self.section -= 1