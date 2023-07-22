from collections import abc


"""
>>> from osconfeed import load
>>> raw_feed = load()
>>> from explore0 import FrozenJSON
>>> feed = FrozenJSON(raw_feed)
>>> len(feed.Schedule.speakers)
357
>>> sorted(feed.Schedule.keys())
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed.Schedule.items()):
...     print('{:3} {}'.format(len(value), key))
... 
  1 conferences
484 events
357 speakers
 53 venues
>>> feed.Schedule.speakers[-1]
<explore0.FrozenJSON object at 0x1092bdd50>
>>> feed.Schedule.speakers[-1].name
'Carina C. Zona'
>>> talk = feed.Schedule.events[40]
>>> type(talk)
<class 'explore0.FrozenJSON'>
>>> talk.name
'There *Will* Be Bugs'
>>> talk.speakers
[3471, 5199]
>>> talk.flavors
Traceback (most recent call last):
  ...
KeyError: 'flavors'
"""


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object
    using attribute notation
    """

    def __init__(self, mapping):
        # __data が確実に dict だと保証するため。また安全のためコピーを作る
        self.__data = dict(mapping)

    # 指定されたname属性がない場合にのみ呼び出される特殊メソッド
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            # keysなどのメソッドに対する呼び出しはこれで処理する
            return getattr(self.__data, name)
        else:
            # それ以外は self.__data からキー name を持つ要素を取得し、
            # これに対して FrozenJSON.build() を呼び出した結果を返す
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            # マッピング型ならば、FrozonJSON 型を作成する。
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            # MutableSequence ならば、リストになるはず。
            # obj にあるすべての要素を再帰的に .build() に渡してリストを作成する。
            # → obj の各要素にさらに変換すべきオブジェクトが入っている可能性があるので、再帰的に適用する
            return [cls.build(item) for item in obj]
        else:
            # どちらでもなければ、そのまま返す
            return obj
