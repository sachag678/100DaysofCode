"""Contains the Object Oriented implemention of a generic deck of cards.
    name: Sacha Gunaratne
    github: sachag678
"""

import random

class Card():
    """Generic card class."""

    def __init__(self, suit, rank):
        """Initialize each card with a suit and rank."""
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return str(self.rank) + ' ' + self.suit
    
    def __le__(self, other):
        return self.rank <= other.rank

    def __lt__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank
    
    def __hash__(self):
        return id(self)

class Deck():
    """Generic deck implementation."""

    def __init__(self):
        """Create a standard 52-card deck of cards."""
        self.cards = []
        suits = ['Heart', 'Diamond', 'Spade', 'Club']
        ranks = [i for i in range(2, 15)]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def __repr__(self):
        s = ''
        for card in sorted(self.cards):
            s += str(card)
            s += '\n'
        return s
    
    def draw(self, number_of_cards=1):
        """Draw a card randomly from the deck. Simulates a shuffled deck without having an ordered deck."""
        drawn_cards = []
        for _ in range(number_of_cards):
            drawn_card_index = random.choice(range(len(self.cards)))
            drawn_card = self.cards.pop(drawn_card_index)
            drawn_cards.append(drawn_card)

        return drawn_cards

class Hand():

    def __init__(self):
        self.hand = []
    
    def add(self, card):
        self.hand.append(card)
    
    def __repr__(self):
        s = '['
        for index, card in enumerate(sorted(self.hand)):
            s += str(card)
            if index < len(self.hand) - 1:
                s += ', '
        s += ']'
        return s

class GameOfPairs():

    def __init__(self):
        self.deck = Deck()
        self.hands = [Hand(), Hand()]

        for _ in range(7):
            for hand in self.hands:
                hand.add(self.deck.draw()[0])
        
        print(self.hands[0])
        print(self.hands[1])

    def play(self):

        for hand in hands:
            hand.add(self.deck.draw()[0])
            self.check_hand_for_pairs(hand)

if __name__ == '__main__':
    gop = GameOfPairs()


        