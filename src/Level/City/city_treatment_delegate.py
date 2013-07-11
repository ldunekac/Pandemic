
class CityTreatmentDelegate:
    """ Delegate to handle treatment of disease infections in a city """
    MAX_INFECTIONS_PER_DISEASE = 3
    
    def __init__(self, city):
        """ Initialize the City Treatment Delegate """
        self.city = city
    
    def treat(self, amount, disease):
        """ Cures a city of a disease by a given amount"""
        disease = self.getDiseaseToTreatWith(disease)
        amount = self.normalizeTreatmentAmount(amount, disease)
        self.treatInfections(amount, disease)
                
    def getDiseaseToTreatWith(self, disease):
        """ Returns the proper disease object to treat with """
        if disease is None:
            disease = self.city.disease
        return disease
        
    def normalizeTreatmentAmount(self, amount, disease):
        """ Returns the normalized Treatment Amount """
        if disease.isCured():
            amount = self.MAX_INFECTIONS_PER_DISEASE
        elif amount > self.MAX_INFECTIONS_PER_DISEASE:
            amount = self.MAX_INFECTIONS_PER_DISEASE
            
        if amount > self.city.diseaseCounts[disease]:
            amount = self.city.diseaseCounts[disease]
            
        return amount
        
    def treatInfections(self, amount, disease):
        """ Reduce number of infections """
        if disease in self.city.diseaseCounts:
            self.city.diseaseCounts[disease] -= amount
            disease.addCubes(amount)