from card import card

class EpidemicCard(Card):
    TYPE = "EPIDEMIC"

    def __init__(self, city):
        Card.__init__(self)
        self.city = city

    def onDraw(self):
        "Preforms the action/event when the card is drawned from the deck"

    def onPlay(self):
        "Preforms the action/event when the card is played"
