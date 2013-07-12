
class LevelSettings:
    """ Container for all level variable settings """
    
    def __init__(self):
        """ Initialize the standard level settings """
        self.MAX_INFECTIONS_PER_DISEASE = 24
        self.MAX_INFECTIONS_PER_DISEASE_IN_CITY = 3
        
        # This is where we would add all Level Customization
        # Such as # of diseases
        # Ability to reshuffle the player deck to continue the game
        # Extended Infection Rates and so forth
        
TheLevelSettings = LevelSettings()