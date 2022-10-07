"""
Written by: Rafael De La Cruz
CSI 33
HW 03 Problem 2
"""
# unitTestingDeck.py

import sys
import unittest

from Deck import Deck
from random import randint


class DeckTest(unittest.TestCase):
    """ Test Deck methods: shuffle(), addTop(), addBottom(), and addRandom() """

    def testShuffle(self):
        """ creats a deck in standard order then shuffles self.cards and verifies that the 
        shuffled deck is not equal to the original deck"""

        deck = Deck()   # creates a deck of cards
        shuffledDeck = deck.shuffle()  # shuffles self.cards
        # verifies shuffled self.cards is not equal to the original self.cards
        self.assertNotEqual(shuffledDeck, deck)

    def testAddTop(self):
        """ creates a deck in standard order, deals card randomly, then adds the dealt card 
            back to the top of self.cards. Verifies that the top card is the dealt card.
            i.e Top of deck is the first card in self.cards list indexed '-1' """

        deck = Deck()  # create a deck of cards
        dealtCard = deck.cards.pop(randint(0, 51))  # deals random card
        deck.addTop(dealtCard)  # adds the dealt card to the top of self.cards
        # verifies first - top of deck - card in the deck is the dealtCard
        self.assertEqual(deck.cards[51], dealtCard)

    def testAddBottom(self):
        """ creates a deck in standard order, deals card from top of deck, then adds the dealt card 
            back to the bottom of self.cards. Verifies that the bottom card is the dealt card.
            i.e Bottom of deck is the last card in self.cards list index is '0' """

        deck = Deck()  # create a deck of cards
        dealtCard = deck.cards.pop(randint(0, 51))  # deals random card
        # adds the dealt card to the bottom of self.cards
        deck.addBottom(dealtCard)
        # verifies last - bottom of deck - card in self.cards is the dealt card
        self.assertEqual(deck.cards[0], dealtCard)

    def testAddRandom(self):
        """ creates a deck in standard order, deals card from top of deck, then adds the dealt card 
            back randomly to self.cards. Verifies that the dealt card is back in the deck."""

        # due to the random index nature (ranging 0 - 51) of placing
        # the card back in self.cards the only test I could think of to verify
        # the card is in a random location is to check if its back in
        # self.cards. Since addRandom can choose to add it back to the top
        # from where it was taken. I figured checking that its in self.cards
        # is a good enough test.

        deck = Deck()  # create a deck of cards
        dealtCard = deck.deal()  # deals a card
        # verifies dealt card is not in self.cards
        self.assertNotIn(dealtCard, deck.cards)
        # adds dealt card randomly back into self.cards
        deck.addRandom(dealtCard)
        # verifies dealt card is back in self.cards
        self.assertIn(dealtCard, deck.cards)


def main(argv):
    unittest.main()


if __name__ == '__main__':
    main(sys.argv)
