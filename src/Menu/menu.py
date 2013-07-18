


class Menu:

    def __init__(self):
        self.menuItemList = []
        self.selectedItem = 0

    def addMenuEntry(self, menuEntry):
        self.menuItemList.append(menuEntry)

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

    def getEntryText(self):
        textList = []
        for entry in self.menuItemList:
            textList.append(entry.getLabel())
        return textList

    def executeEntry(self):
        self.menuItemList[self.selectedItem].run()