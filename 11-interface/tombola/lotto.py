import random

from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        # イニシャライザはイテラブルなら何でも受け入れる
        # iterable そのものではなくコピーを作成している
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            # 指定されたリストが空のとき、 ValueError を上げる
            position = random.randrange(len(self._balls))
        except ValueError:
            # Tombola クラスとの互換性のため LookupError として上げる
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        # 元々の実装は bool(self.inspect())
        # だけどコストが高いのでオーバーライドしている
        return bool(self._balls)

    def inspect(self):
        # この実装もオーバーライド
        return tuple(sorted(self._balls))
