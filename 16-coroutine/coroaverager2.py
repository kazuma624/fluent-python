from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

"""
In [1]: from averager2 import averager

In [2]: coro_avg = averager()

In [3]: from inspect import getgeneratorstate

In [4]: getgeneratorstate(coro_avg)
Out[4]: 'GEN_SUSPENDED'

# 即座に .send() が実行できる状態になっている。(next(...) の実行はデコレータ側で実装している）
In [5]: coro_avg.send(10)
Out[5]: 10.0

In [6]: coro_avg.send(30)
Out[6]: 20.0

In [7]: coro_avg.send(5)
Out[7]: 15.0
"""
