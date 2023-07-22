from collections import abc
from keyword import iskeyword


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object
    using attribute notation
    """

    # __new__ は（特殊な）クラスメソッド
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            # デフォルトの動作。スーパークラスの __new__ へデリゲート（移譲）
            # ここでは基底クラスの object から __new__ を呼び出している
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # 前の例では .build を呼び出していたが、ここではコンストラクタを呼び出すだけ
            return FrozenJSON(self.__data[name])
