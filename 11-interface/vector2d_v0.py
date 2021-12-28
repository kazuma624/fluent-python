class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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
>>> v.x
3
上書きできてしまう
"""
