"""Contains the Object Oriented implemention of a generic deck of cards."""

class Card():

    def __init__(self, suit, rank):
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

    def __init__(self):
        self.cards = set()
        suits = ['Heart', 'Diamond', 'Spade', 'Club']
        ranks = [i for i in range(2, 15)]
        for suit in suits:
            for rank in ranks:
                self.cards.add(Card(suit, rank))
    
    def __repr__(self):
        s = ''
        for card in sorted(self.cards):
            s += str(card)
            s += '\n'
        return s

if __name__ == '__main__':
    deck = Deck()
    print(deck)



        