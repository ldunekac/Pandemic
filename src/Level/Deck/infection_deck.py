from deck import Deck
import random

class InfectionDeck(Deck):

    def __init__(self, deck):
        Deck.__init__(self, deck)

    def draw(self):
        if len(self.deck) == 0:
            self.intensify()
        card = self.deck.pop()
        self.discard(card)
        return card

    def intensify(self):
        random.shuffle(self.discardPile)
        self.deck += self.discardPile
        self.discardPile = []