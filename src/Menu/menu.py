


class Menu:

    def __init__(self):
        self.menuItemList = []
        self.selectedItem = 0

    def addMenuEntry(self, menuEntry):
        self.menuItemList.append(menuEntry)

    def moveUp(self):
        if self.selectedItem > 0:
            self.selectedItem -= 1

    def moveDown(self):
        if self.selectedItem < len(self.menuItemList) - 1:
            self.selectedItem += 1

    def executeEntry(self):
        self.menuItemList[self.selectedItem].run()