
from deck import deck

class player_deck(Deck):

    def __init__(self, deck):
        Deck.__init__(self, deck)

    def draw(self):
        if len(self.deck) == 0:
            return None
        card = self.deck.pop()
        card.onDraw()
        return card