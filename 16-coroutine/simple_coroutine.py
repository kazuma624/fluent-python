def simple_coroutine():
    print("-> coroutine started")
    # コルーチンがクライアントからデータを受信するためだけに設計されているときは None を返す（yield のあとに式がないときの暗黙的な動作）。
    x = yield
    print("-> coroutine received: ", x)

"""
In [2]: my_coro = simple_coroutine()

# 通常のジェネレータと同じように、関数を呼び出してジェネレータオブジェクトを取得する
In [3]: my_coro
Out[3]: <generator object simple_coroutine at 0x10ee394d0>

# 最初に next(...) を呼び出す。
# まだジェネレータはスタートしておらず、 yield で待機もしていないので、この段階ではデータは送信できない。
In [4]: next(my_coro)
-> coroutine started

# コルーチンにある yield が 42 と評価される。
# この結果、コルーチンは再開し、次の yield まで実行を待機するか、終了する。
In [5]: my_coro.send(42)
-> coroutine received:  42
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [5], line 1
----> 1 my_coro.send(42)

StopIteration: 
# 制御フローがコルーチン本体の末尾に達するので、ジェネレーションのメカニズムが StopIteration を上げる。
"""
