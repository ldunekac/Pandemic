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
from View.GUI.Game.game_controller import GameController

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
            mousePosition = pygame.mouse.get_pos()
            self.mainMenuView.selectEntry(mousePosition)  
            window.draw(self.mainMenuView.draw())
            if pygame.mouse.get_pressed()[0]:
                self.mainMenuView.executeIfSelected(mousePosition)

              


    def playGame(self):
        """ Executes the main Game !!!"""
        gameController = GameController()
        gameController.run()


    def exit(self):
        """ Exits the Game """
        exit(0)
