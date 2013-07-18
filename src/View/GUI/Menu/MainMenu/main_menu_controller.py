"""
This is the main Controler that initializes pygame and starts the game
"""

from sys import exit

import pygame
from pygame.locals import *
from Menu.menu import Menu
from Menu.menu_entry import MenuEntry
from View.GUI.window import window
from View.GUI.Menu.MainMenu.main_menu_view import MainMenuView


class MainMenuController:

    def __init__(self):
        self.menu = Menu()
        self.menu.addMenuEntry(MenuEntry("Play!!", self.playGame))
        self.menu.addMenuEntry(MenuEntry("Exit", self.exit))
        self.mainMenuView = MainMenuView(self.menu)
        self.clock = pygame.time.Clock()

        self.running = True

    def run(self):
        """ Starts the main menu screen """
        while self.running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        self.running = False
                    if event.key == K_UP:
                        self.menu.moveUp()
                    if event.key == K_DOWN:
                        self.menu.moveDown()
                    if event.key == K_RETURN:
                        self.menu.executeEntry()
            window.draw(self.mainMenuView.draw())


    def playGame(self):
        """ Executes the main Game """

    def exit(self):
        """ Exits the Game """
        exit(0)
