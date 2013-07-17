

class MenuEntry:

    def __init__(self, label, callBackFuction):
        self.label = label
        self.callBackFuction = callBackFuction

    def getLabel(self):
        return self.label

    def getCallBackFunction(self):
        return self.callBackFuction

    def run(self):
        self.callBackFuction()