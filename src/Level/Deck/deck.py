import random

class Deck:

    """"Sets up a deck"""
    def __init__(self, deck):
        self.deck = deck
        self.discardPile = []

    def  shuffle(self):
        """ Shuffles the deck"""
        random.shuffle(self.deck)

    def draw(self):
        if len(self.deck) == 0:
            return None
        card = self.deck.pop()
        return card

    def discard(self, card):
        """Adds a card to the discard pile"""
        self.discardPile.append(card)
