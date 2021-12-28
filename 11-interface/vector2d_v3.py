class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))
        # こうとも書ける
        # yield self.x
        # yield self.y

"""
>>> v = Vector2d(1, 2)
>>> v.x
1.0
>>> v.x = 3
AttributeError
Traceback (most recent call last)
<ipython-input-14-be0ecbdd803a> in <module>
----> 1 v.x = 3

AttributeError: can't set attribute

読み取り専用属性に
"""
