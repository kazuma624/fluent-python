from collections import namedtuple

Result = namedtuple("Result", "count average")

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield # 値を yield しない
        if term is None:
            # ループを抜けるための条件
            break
        total += term
        count += 1
        average = total/count

    return Result(count, average)

"""
In [1]: from coroaverager3 import averager

In [2]: coro_avg = averager()

In [3]: next(coro_avg)

# 値を yield しない
In [4]: coro_avg.send(10)

In [5]: coro_avg.send(30)

In [6]: coro_avg.send(6.5)

# ジェネレータオブジェクトは StopIteration を上げる
In [7]: coro_avg.send(None)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [7], line 1
----> 1 coro_avg.send(None)

StopIteration: Result(count=3, average=15.5)
"""

"""
In [8]: coro_avg = averager()

In [9]: next(coro_avg)

In [10]: coro_avg.send(10)

In [11]: coro_avg.send(30)

In [12]: coro_avg.send(6.5)

In [13]: try:
    ...:     coro_avg.send(None)
    ...: except StopIteration as exc:
    ...:     result = exc.value
    ...: 

In [14]: result
Out[14]: Result(count=3, average=15.5)
"""
