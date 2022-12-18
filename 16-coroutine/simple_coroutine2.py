def simple_coro2(a):
    print("-> Started: a =", a)
    b = yield a
    print("-> Received: b =", b)
    c = yield a + b
    print("-> Received: c =", c)


"""
In [8]: from simple_coroutine2 import simple_coro2

In [9]: my_coro2 = simple_coro2(14)

In [10]: from inspect import getgeneratorstate

# コルーチンはまだ開始されていない
In [11]: getgeneratorstate(my_coro2)
Out[11]: 'GEN_CREATED'

# コルーチンを最初の yield まで進める。
# メッセージ「-> Started: a = 14」を出力する。
# a の値を yield し、値が b へ代入されるのを待機するために休止する。
In [12]: next(my_coro2)
-> Started: a = 14
Out[12]: 14

# コルーチンは yield 式で一時停止している。
In [13]: getgeneratorstate(my_coro2)
Out[13]: 'GEN_SUSPENDED'

# 休止中のコルーチンへ 28 を送信する。
# yield 式が 28 を評価すると、その値が b にバインドされる。
# メッセージ「-> Received: b = 28」が表示され、a + b の値(42)が生成される。
# コルーチンは休止し、値が c へ代入されるまで待機する。
In [14]: my_coro2.send(28)
-> Received: b = 28
Out[14]: 42

# 休止中のコルーチンへ 99 を送信する。
# yield 式が 99 を評価すると、その値が c にバインドされる。
# メッセージ「-> Received: c = 99」が表示されてコルーチンが終了しジェネレータオブジェクトが StopIteration を上げる。
In [15]: my_coro2.send(99)
-> Received: c = 99
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [15], line 1
----> 1 my_coro2.send(99)

StopIteration: 

# コルーチンの実行が完了している。
In [16]: getgeneratorstate(my_coro2)
Out[16]: 'GEN_CLOSED'
"""
