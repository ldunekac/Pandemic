#from PySide.QtGui import QApplication
from Level.level import Level

import sys

def main(args):
    """ Run the main file """
    #app = QApplication(sys.argv)
    #sys.exit(app.exec_())
    level = Level()
    
    for city in level.cities:
        print city
        print "Adjacent to:"
        print city.adjacentCities

if __name__ == "__main__":
    main(sys.argv[1:])