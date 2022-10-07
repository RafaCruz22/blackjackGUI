# Deck.py

from random import randrange
from Card import Card


class Deck:

    # ------------------------------------------------------------

    def __init__(self):
        """post: Creates a 52 card deck in standard order"""

        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        self.cards = cards

    # ------------------------------------------------------------

    def size(self):
        """Cards left
        post: Returns the number of cards in self"""

        return len(self.cards)

    # ------------------------------------------------------------

    def deal(self):
        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""

        if self.size() > 0:
            return self.cards.pop()
        else:
            return False

    # ------------------------------------------------------------

    def shuffle(self):
        """Shuffles the deck
        post: randomizes the order of cards in self"""

        n = self.size()
        cards = self.cards
        for i, card in enumerate(cards):
            pos = randrange(i, n)
            cards[i] = cards[pos]
            cards[pos] = card
