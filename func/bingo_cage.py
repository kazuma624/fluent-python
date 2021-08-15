import random

class BingoCage:

    def __init__(self, items):
        '''
        イテラブルであればなんでも受け付ける。
        ローカルコピーを作成することで、
        引数として渡される list に予期せぬ副作用が発生することを防止できる。
        '''
        self._items = list(items)
        # self._items は list なので必ず動作する。
        random.shuffle(self._items)

    def pick(self):
        '''
        メインメソッド
        '''
        try:
            return self._items.pop()
        except IndexError:
            # self._items に要素がなければ例外を上げる
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        '''
        任意の Python オブジェクトを関数のように動作させることができる
        全ての呼び出しを通して保持されなければならない内部状態を保持する
        '''
        # bingo() は bingo.pick() のショートカットになっている
        return self.pick()

