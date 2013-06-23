
class InfectionView:
    """ Represents the view for an Infection """
    
    def __init__(self, city):
        """ Initialize the view """
        self.city = city
        
    def display(self):
        """ Display the Infection """
        print "{0} was infected!\r".format(self.city)
        for disease in self.city.diseaseCounts:
            print "Disease Count: {0}\r".format(self.city.diseaseCounts[disease])