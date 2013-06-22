from View.Console.controller import Controller
from View.Console.Level.cities_view import CitiesView

class CitiesController(Controller):
    """ Controller for cities list """

    def __init__(self, cities):
        """ Initialize the Cities Controller """
        Controller.__init__(self, CitiesView(cities))