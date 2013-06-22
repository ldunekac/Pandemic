from View.Console.controller import Controller
from View.Console.Level.cities_view import CitiesView
from View.Console.Level.city_controller import CityController

class CitiesController(Controller):
    """ Controller for cities list """

    def __init__(self, cities):
        """ Initialize the Cities Controller """
        Controller.__init__(self, CitiesView(cities))
        
        self.addCommand(ord('1'), self.viewCity)
        
    def viewCity(self):
        """ View the selected city """
        controller = CityController(self.screen.cities[0])
        controller.run()