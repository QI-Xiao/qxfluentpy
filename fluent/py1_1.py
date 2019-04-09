import collections
from random import choice
import random

cccard = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits ='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [cccard(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()
print(len(deck), deck[5])
print(choice(deck))
print(deck[:3])
print(deck[12::13])
for card in reversed(deck):
    print(card)

print(deck[5].rank)
print(FrenchDeck.ranks.index(deck[5].rank))
print(spades_high(deck[5]))
print(suit_values)

print('deck:', deck)
for card in reversed(sorted(deck, key=spades_high)):
    print(card)

# aaa = [1,2,3]
# random.shuffle(deck)
# print(deck)
aaaa = FrenchDeck()
for i in aaaa:
    print(i)