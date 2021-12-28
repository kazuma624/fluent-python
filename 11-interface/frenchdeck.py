import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # シーケンスプロトコルのメソッドの一つ
    def __len__(self):
        return len(self._cards)

    # シーケンスプロトコルのメソッドの一つ
    def __getitem__(self, position):
        return self._cards[position]


"""
In [5]: from random import shuffle
In [7]: from frenchdeck import FrenchDeck
In [8]: deck = FrenchDeck()
In [9]: shuffle(deck)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-f43911d87fe3> in <module>
----> 1 shuffle(deck)

~/.anyenv/envs/pyenv/versions/3.9.5/lib/python3.9/random.py in shuffle(self, x, random)
    361                 # pick an element in x[:i+1] with which to exchange x[i]
    362                 j = randbelow(i + 1)
--> 363                 x[i], x[j] = x[j], x[i]
    364         else:
    365             _warn('The *random* parameter to shuffle() has been deprecated\n'

TypeError: 'FrenchDeck' object does not support item assignment

不変なシーケンスプロトコルだけを実装しているのにインプレイスで要素を並び替えようとしている
"""



"""
In [10]: def set_card(deck, position, card):
    ...:     deck._cards[position] = card
    ...: 
In [11]: FrenchDeck.__setitem__ = set_card
In [12]: shuffle(deck)
In [13]: deck[:5]
Out[13]: 
[Card(rank='3', suit='hearts'),
 Card(rank='Q', suit='clubs'),
 Card(rank='7', suit='spades'),
 Card(rank='7', suit='hearts'),
 Card(rank='9', suit='hearts')]

__setitem__ メソッドを実装することでシーケンスを可変にできる
言語リファレンスでは引数が (self, key, value) だが、
第一引数を self にするのはあくまで慣習なのでここでは deck としている

このようにランタイムでプロトコルを実装するやり方をモンキーパッチという
"""
