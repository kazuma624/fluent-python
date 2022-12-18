import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        # findall は正規表現に一致する重複のないない文字列のリストを返す
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __len__(self) -> int:
        # シーケンスプロトコルを満たすためには __len__ が必要だが、
        # イテラブルオブジェクトを作成するための必要条件ではない
        return len(self.words)

    def __repr__(self) -> str:
        # reprlib.repr はデータ構造がとても長いとき（デフォルトで30文字）に文字列を省略して表示するユーティリティ関数
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s) # Sentence('"The time ha... Walrus said,')
    for word in s:
        print(s)

    print(list(s))

"""
シーケンスがイテラブルである理由

インタプリタはオブジェクトxに対して反復処理をするとき、自動的にiter(x)を呼び出す。
組み込み関数iterは次を実行する

1. オブジェクトが__iter__を実装しているかを確認し、実装されていればこれを呼び出してイテレータを取得する。
2. __iter__ がないが __getitem__ は実装されているときは、Pythonはインデックス0から順に要素の取得を試みるイテレータを作成する。
3. これに失敗すると、Pythonは 'hoge' object is not callable というメッセージと共にTypeErorを上げる。

要するに __getitem__ さえ実装されていればイテラブルと見なされる。
ただし標準のシーケンス型の実装に倣って __iter__ を実装した方が良い。
"""


"""
>>> class Foo:
...    def __iter__(self):
...        pass
...
>>> from collections import abc
>>> issubclass(Foo, abc.Iterable)
True

>>> f = Foo()
>>> isinstance(f, abc.Iterable)
True
"""
