from card import card

class CityCard(Card):
    TYPE = "CITY"

    def __init__(self, city):
        Card.__init__(self)
        self.city = city

    def onDraw(self):
        """ Do nothing when drawn """

    def onPlay(self):
        """ Do nothing when played """
