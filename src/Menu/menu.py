


class Menu:

    def __init__(self):
        self.menuItemList = []
        self.selectedItem = None

    def addMenuEntry(self, menuEntry):
        self.menuItemList.append(menuEntry)
        if self.selectedItem == None:
            self.selectedItem = 0
            self.menuItemList[0].setSelected(True)

    def moveUp(self):
        if self.selectedItem > 0:
            self.menuItemList[self.selectedItem].setSelected(False)
            self.selectedItem -= 1
            self.menuItemList[self.selectedItem].setSelected(True)

    def moveDown(self):
        if self.selectedItem < len(self.menuItemList) - 1:
            self.menuItemList[self.selectedItem].setSelected(False)
            self.selectedItem += 1
            self.menuItemList[self.selectedItem].setSelected(True)

    def getEntries(self):
        return self.menuItemList

    def executeEntry(self):
        self.menuItemList[self.selectedItem].run()