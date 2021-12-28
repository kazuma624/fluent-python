import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
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

    # シャフルするために必要なメソッド
    def __setitem__(self, position, value):
        self._cards[position] = value

    # 実装しないといけない
    def __delitem__(self, position):
        del self._cards[position]

    # 実装しないといけない
    def insert(self, position, value):
        self._cards.insert(position, value)


"""
FrenchDeck2はすぐに使える具象メソッドの
__contains__, __iter__, __reversed__, index, count
を Sequence から継承する。

MutableSequence からは append, reverse, extend, pop, remove, __iadd__
を取得する。
"""
