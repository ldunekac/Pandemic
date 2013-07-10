from Level.Disease.Outbreak.outbreak_manager import TheOutbreakManager

class City:
    """ Represents a city in the level """
    MAX_INFECTIONS_PER_DISEASE = 3
    
    def __init__(self, name, disease):
        """ Initialize the city """
        self.name = name
        self.disease = disease
        self.adjacentCities = set()
        self.diseaseCounts = {}
        
    def addAdjacentCity(self, city):
        """ Add a city to this city's adjacency list """
        self.adjacentCities.add(city)
        
    def infect(self, amount, disease=None):
        """ Infect the city with given amount """
        if amount > self.MAX_INFECTIONS_PER_DISEASE:
            amount = self.MAX_INFECTIONS_PER_DISEASE

        if disease is None:
            disease = self.disease
            
        if disease in self.diseaseCounts:
            maxAmountThatCanBeAdded = self.MAX_INFECTIONS_PER_DISEASE - self.diseaseCounts[disease]
            if amount > maxAmountThatCanBeAdded:
                amount = maxAmountThatCanBeAdded
                TheOutbreakManager.startOutbreak(self, disease)
            self.diseaseCounts[disease] += amount
        else:
            self.diseaseCounts[disease] = amount

        disease.removeCubes(amount)
        # Will need to check for outbreaks at some point

    def treat(self, amount, disease = None):
        """ Cures a city of a disease by a given amount"""
        if disease is None:
            disease = self.disease

        if disease.isCured():
            amount = self.MAX_INFECTIONS_PER_DISEASE
        elif amount > self.MAX_INFECTIONS_PER_DISEASE:
            amount = self.MAX_INFECTIONS_PER_DISEASE

        if disease in self.diseaseCounts:
            amountOfDisease = self.diseaseCounts[disease]
            if(amount >= amountOfDisease):
                disease.addCubes(self.diseaseCounts[disease])
                self.diseaseCounts[disease] = 0
            else:
                self.diseaseCounts[disease] -= amount
                disease.addCubes(amount)
        
    def getDiseaseInfections(self, disease):
        """ Return the number of infections in the city of for the given disease """
        amount = 0
        if disease in self.diseaseCounts:
            amount = self.diseaseCounts[disease]
        return amount
        
    def __repr__(self):
        """ Return the string representtation of the City """
        return self.name