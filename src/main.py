#from PySide.QtGui import QApplication
from Level.level import Level

from View.Console.Level.level_controller import LevelController

import sys

def main(args):
    """ Run the main file """
    #app = QApplication(sys.argv)
    #sys.exit(app.exec_())
    levelController = LevelController()
    levelController.run()
    
    # for city in level.cities:
        # print city
        # print "Adjacent to:"
        # print city.adjacentCities

if __name__ == "__main__":
    main(sys.argv[1:])