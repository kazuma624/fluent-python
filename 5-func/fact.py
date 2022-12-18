from functools import reduce
from operator import mul

def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


def fact_op(n):
    """fact と同じ挙動
    """
    return reduce(mul, range(1, n+1))

