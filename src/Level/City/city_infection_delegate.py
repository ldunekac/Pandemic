from Level.Disease.Outbreak.outbreak_manager import TheOutbreakManager

class CityInfectionDelegate:
    """ Delegate to handle infecting a city """
    MAX_INFECTIONS_PER_DISEASE = 3
    
    def __init__(self, city):
        """ Initialize the Infection Delegate """
        self.city = city
        
    def infect(self, amount, disease):
        """ Infect the city with the given amount of the given disease """
        amount = self.normalizeAmount(amount)
        disease = self.getDiseaseToInfectWith(disease)
            
        if disease in self.city.diseaseCounts:
            if self.shouldOutbreak(amount, disease):
                amount = self.MAX_INFECTIONS_PER_DISEASE - self.city.diseaseCounts[disease]
                TheOutbreakManager.startOutbreak(self.city, disease)
        self.increaseInfections(amount, disease)
        
    def normalizeAmount(self, amount):
        """ Normalize the amount of infection """
        if amount > self.MAX_INFECTIONS_PER_DISEASE:
            amount = self.MAX_INFECTIONS_PER_DISEASE
        return amount
        
    def getDiseaseToInfectWith(self, disease):
        """ Returns the proper disease object to infect with """
        if disease is None:
            disease = self.city.disease
        return disease
        
    def shouldOutbreak(self, amount, disease):
        """ Return if the infection should cause an outbreak """
        return self.city.getDiseaseInfections(disease) + amount > self.MAX_INFECTIONS_PER_DISEASE
        
    def increaseInfections(self, amount, disease):
        """ Increase number of infections """
        if disease in self.city.diseaseCounts:
            self.city.diseaseCounts[disease] += amount
        else:
            self.city.diseaseCounts[disease] = amount
        disease.removeCubes(amount)