from pprint import pprint
from operator import methodcaller

class myclass:
    __slots__ = ('_name', '_args', '_kwargs')

    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._args = args
        self._kwargs = kwargs

    def get_hoge(self, num):
        print((self._name) * num)

    # def __call__(self):
    #     return self.get_hoge()

    def aaa(self):
        if not self._kwargs:
            return self.__class__, (self._name,) + self._args
        else:
            from functools import partial
            return partial(self.__class__, self._name, **self._kwargs), self._args


obj = myclass("a", "b", c="C")
print(obj.aaa())


obj2 = myclass("a", "b")
print(obj2.aaa())

# obj.get_hoge(2)

# get_hoge = methodcaller('get_hoge', 3)
get_hoge = methodcaller('get_hoge', num=3)
# print(get_hoge)

# pprint(get_hoge.__class__.__module__)
# pprint(get_hoge.__class__.__name__)

# pprint(dir(obj))
# pprint(dir(obj.__class__))
# pprint(dir(obj.__class__.__module__))



# obj.__slots__ = ('_hoge', '_fuga', 'piyo')

# setattr(obj, "piyo", "c")
# print(obj.piyo)


# obj = myclass("a", "b")
# obj()
# print(obj)