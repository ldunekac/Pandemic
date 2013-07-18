

class MenuEntry:

    def __init__(self, label, callBackFuction):
        self.label = label
        self.callBackFuction = callBackFuction
        self.selected = False
        self.next = None
        self.back = None

    def addNext(self, next):
        self.next = next

    def addBack(self, back):
        self.back = back

    def getNext(self):
        return self.next

    def getBack(self):
        return self.back

    def getText(self):
        return self.label

    def getCallBackFunction(self):
        return self.callBackFuction

    def run(self):
        self.callBackFuction()

    def select(self):
        self.selected = True
        # move forward in list
        forward = self.getNext()
        while forward != None:
            forward.unSelect()
            forward = forward.getNext()
        # move backward in list
        back = self.getBack()
        while back != None:
            back.unSelect()
            back = back.getBack()

    def unSelect(self):
        self.selected = False

    def isSelected(self):
        return self.selected