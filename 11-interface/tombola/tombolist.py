from random import randrange

from tombola import Tombola


@Tombola.register  # TomboListをTombolaの仮想サブクラスとして登録する
class TomboList(list):  # list を継承する

    def pick(self):
        # __bool__ は TomboList が list から継承したものであり、リストが空でなければ True を返す
        if self:
            position = randrange(len(self))
            # ランダムな要素インデックスを指定して、 list から継承した self.pop を呼び出す
            return self.pop(position)
        else:
            raise LookupError('pop from empty Tombolist')

    load = list.extend

    def loaded(self):
        # bool にデリゲートされている
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
