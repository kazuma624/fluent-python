class StrKeyDict0(dict):  # dict を継承

    def __missing__(self, key):
        if isinstance(key, str):
            # key が　str であるのに見つかってないのであれば KeyError を発生させる
            raise KeyError(key)
        # key から str を生成し、サーチする
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # __getitem__ へデリゲートする。これによって　__missing__ に動作する機会が与えられる
            return self[key]
        except KeyError:
            # KeyError が発生したということは、すでに __missing__ はすでに失敗しているので default を返す
            return default

    def __contains__(self, key):
        # 未変更のキー(インスタンスには文字列ではないキーが含まれている可能性もある)をサーチし、続いてそのキーから構築された str をサーチする
        return key in self.keys() or str(key) in self.keys()
        # str(key) in self だと再起的に __contains__ が呼び出されるため、 key in self.keys() という書き方を採用している

"""
チェックしなくても、 str(k) が既存のキーを生成できれば、 __missing__ メソッドは任意のキー k に対して問題なく動作する。
しかし、 __missing__ の最終行にある self[str(key)] は、 __getitem__ にそのキーを渡して呼び出し、これが次にまた __missing__ を呼び出すため、
str(k) が存在するキーではなければ無限に再帰を繰り返してしまう。

整合性のある動きをさせるためには __contains__ メソッドが必要。
このメソッドは k in d という操作をすると呼び出されるが、 dict から継承されたメソッドは __missing__ を呼び出さないため、無限に再帰を繰り返してしまう問題を回避できる。
"""

if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d['4'])
    # print(d['1'])

    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))

    # print(2 in d)
    # print(1 in d)
