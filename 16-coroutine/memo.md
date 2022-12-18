## コルーチンの状態

4つの状態のうちどれかを取る。
これは `inspect.getgeneratorstate` で取得できる。

- GEN_CREATED
    - 実行の開始を待機中
- GEN_RUNNING
    - インタプリタが現在実行中
- GEN_SUSPENDED
    - yield の箇所で現在休止中
- GEN_CLOSED
    - 実行完了


send メソッドの引数は休止している yield の値になるため、コルーチンが GEN_SUSPENDED の場合は `my_coro.send(42)` のような呼び出ししかできない。
しかし、コルーチンがまだ起動していない GEN_CREATED の状態にあるときは、その限りではない。
`next(my_coro)` もしくは `my_coro.send(None)` でも良い。

