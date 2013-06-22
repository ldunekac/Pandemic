from View.Console.controller import Controller
from View.Console.Level.cities_view import CitiesView
from View.Console.Level.city_controller import CityController

class CitiesController(Controller):
    """ Controller for cities list """

    def __init__(self, cities):
        """ Initialize the Cities Controller """
        Controller.__init__(self, CitiesView(cities))
        
        self.addCommand(ord('0'), self.viewCityZero)
        self.addCommand(ord('1'), self.viewCityOne)
        self.addCommand(ord('2'), self.viewCityTwo)
        self.addCommand(ord('3'), self.viewCityThree)
        self.addCommand(ord('4'), self.viewCityFour)
        self.addCommand(ord('5'), self.viewCityFive)
        self.addCommand(ord('6'), self.viewCitySix)
        self.addCommand(ord('7'), self.viewCitySeven)
        self.addCommand(ord('8'), self.viewCityEight)
        self.addCommand(ord('9'), self.viewCityNine)
        
        self.addCommand(ord('n'), self.screen.selectNextSection)
        self.addCommand(ord('p'), self.screen.selectPreviousSection)
        
    def viewCityZero(self):
        """ View the selected city """
        self.viewCity(0)
        
    def viewCityOne(self):
        """ View the selected city """
        self.viewCity(1)
        
    def viewCityTwo(self):
        """ View the selected city """
        self.viewCity(2)
        
    def viewCityThree(self):
        """ View the selected city """
        self.viewCity(3)
        
    def viewCityFour(self):
        """ View the selected city """
        self.viewCity(4)
        
    def viewCityFive(self):
        """ View the selected city """
        self.viewCity(5)
        
    def viewCitySix(self):
        """ View the selected city """
        self.viewCity(6)
        
    def viewCitySeven(self):
        """ View the selected city """
        self.viewCity(7)
        
    def viewCityEight(self):
        """ View the selected city """
        self.viewCity(8)
        
    def viewCityNine(self):
        """ View the selected city """
        self.viewCity(9)
        
    def viewCity(self, index):
        """ View the selected city """
        city = self.screen.getCity(index)
        if city is not None:
            controller = CityController(city)
            controller.run()