


class Menu:

    def __init__(self):
        self.menuItemList = []
        self.selectedItem = None

    def addMenuEntry(self, menuEntry):
        self.menuItemList.append(menuEntry)
        if len(self.menuItemList) > 1:
            self.menuItemList[-2].addNext(self.menuItemList[-1])
            self.menuItemList[-1].addBack(self.menuItemList[-2])
        else:
            self.menuItemList[0].select()

    def moveUp(self):
        for item in self.menuItemList:
            if item.isSelected():
                item = item.getBack()
                if item != None:
                    item.select()
                break

    def moveDown(self):
        for item in self.menuItemList:
            if item.isSelected():
                item = item.getNext()
                if item != None:
                    item.select()
                break

    def getEntries(self):
        return self.menuItemList

    def executeEntry(self):
        for item in self.menuItemList:
            if item.isSelected():
                item.run()
                break