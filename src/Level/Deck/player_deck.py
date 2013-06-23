from deck import Deck

class PlayerDeck(Deck):

    def __init__(self, deck):
        Deck.__init__(self, deck)

    def draw(self):
        if len(self.deck) == 0:
            return None
        card = self.deck.pop()
        card.onDraw()
        return card