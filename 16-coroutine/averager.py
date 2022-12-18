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
In [18]: coro_avg = averager()

In [19]: next(coro_avg)

In [20]: coro_avg.send(10)
Out[20]: 10.0

In [21]: coro_avg.send(30)
Out[21]: 20.0

In [22]: coro_avg.send(5)
Out[22]: 15.0
"""
