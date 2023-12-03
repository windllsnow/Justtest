#%%
# 
#
#流暢python
#
#
#
# #
#%%
import collections
from random import random

Cards = collections.namedtuple('Cards', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    def __init__(self):
        self._cards = [Cards(rank, suit) for suit in self.suits
                                        for rank in self. ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]       

beer_card = Cards(rank = '7', suit = 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))


#%%





