"""
This is the main Controler that initializes pygame and starts the game
"""

from sys import exit

import pygame
from pygame.locals import *
from Menu.menu import Menu
from Menu.menu_entry import MenuEntry
from View.GUI.window import Window

class MainMenuController:

    def __init__(self):
        self.window = Window()
        self.menu = Menu()
        self.menu.addMenuEntry(MenuEntry("Play!!", self.playGame))
        self.menu.addMenuEntry(MenuEntry("Exit", self.exit))

    def run(self):
        """ Starts the game!!! """

    def playGame(self):
        """ Executes the main Game """

    def exit(self):
        """ Exits the Game """
        eixt(0)
