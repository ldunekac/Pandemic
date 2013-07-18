#from PySide.QtGui import QApplication
from Level.level import Level


import sys

def main(args):
    """ Run the main file """
    #app = QApplication(sys.argv)
    #sys.exit(app.exec_())
    try:
        import pygame
        from View.GUI.Menu.MainMenu.main_menu_controller import MainMenuController
        mainMenuController = MainMenuController()
        mainMenuController.run() 

    except ImportError as e:
        from View.Console.Level.level_controller import LevelController
        levelController = LevelController()
        levelController.run()

if __name__ == "__main__":
    main(sys.argv[1:])