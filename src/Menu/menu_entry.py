

class MenuEntry:

    def __init__(self, label, callBackFuction):
        self.label = label
        self.callBackFuction = callBackFuction
        self.selected = False

    def getText(self):
        return self.label

    def getCallBackFunction(self):
        return self.callBackFuction

    def run(self):
        self.callBackFuction()

    def setSelected(self, selected):
        self.selected = selected

    def isSelected(self):
        return self.selected