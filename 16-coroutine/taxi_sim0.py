import collections

Event = collections.namedtuple("Event", "time proc action")

# タクシー1台につき1回呼び出される
def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change

    Args:
        ident (int): タクシー番号
        trips (int): タクシーの送迎回数
        start_time (int, optional): タクシーが出庫する時刻. Defaults to 0.

    Yields:
        Event: タクシーのイベント
    """
    time = yield Event(start_time, ident, "leave garage")
    for i in range(trips):
        time = yield Event(time, ident, "pick up passenger")
        time = yield Event(time, ident, "drop off passenger")

    yield Event(time, ident, "going home")
    # end of taxi process


"""
In [1]: from taxi_sim import taxi_process

In [2]: taxi = taxi_process(ident=13, trips=2, start_time=0)

In [3]: next(taxi)
Out[3]: Event(time=0, proc=13, action='leave garage')

In [4]: taxi.send(_.time + 7)
Out[4]: Event(time=7, proc=13, action='pick up passenger')

In [5]: taxi.send(_.time + 23)
Out[5]: Event(time=30, proc=13, action='drop off passenger')

In [6]: taxi.send(_.time + 5)
Out[6]: Event(time=35, proc=13, action='pick up passenger')

In [7]: taxi.send(_.time + 48)
Out[7]: Event(time=83, proc=13, action='drop off passenger')

In [8]: taxi.send(_.time + 1)
Out[8]: Event(time=84, proc=13, action='going home')

In [9]: taxi.send(_.time + 10)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [9], line 1
----> 1 taxi.send(_.time + 10)

StopIteration: 

"""
