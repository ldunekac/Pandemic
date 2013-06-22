from View.Console.controller import Controller
from View.Console.Level.city_view import CityView

class CityController(Controller):
    """ Controller for a city """
    
    def __init__(self, city):
        """ Initialize the City Controller """
        Controller.__init__(self, CityView(city))