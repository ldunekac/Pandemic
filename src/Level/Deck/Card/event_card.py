from card import card

class EventCard(Card):
    TYPE = "EVENT"

    def __init__(self):
        Card.__init__(self)

    def onDraw(self):
        "Preforms the action/event when the card is drawned from the deck"

    def onPlay(self):
        "Preforms the action/event when the card is played"
