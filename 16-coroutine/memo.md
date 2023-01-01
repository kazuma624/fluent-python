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

## yield from 入門

`yield from` は新しい言語構造。
他の言語での意味合いとしては `await` と同じ。

ジェネレータ `gen` が `yield from subgen()` を呼び出すと、 `subgen()` が制御を奪い、 `gen` の呼び出し元に値を返す。

実質的に呼び出し元が `subgen()` を直接駆動させることになる。

`gen` は `subgen` が終了するまで待機する。

とりあえずコルーチンに関係なく使い方の一例（14章にも出てくる）

```python
In [1]: def gen():
   ...:     for c in 'AB':
   ...:         yield c
   ...:     for i in range(1, 3):
   ...:         yield i
   ...: 

In [2]: list(gen())
Out[2]: ['A', 'B', 1, 2]
```

こう書ける。

```python
In [3]: def gen():
   ...:     yield from 'AB'
   ...:     yield from range(1, 3)
   ...: 

In [4]: list(gen())
Out[4]: ['A', 'B', 1, 2]
```

他の使い方

```python
In [5]: def chain(*iterables):
   ...:     for i in iterables:
   ...:         yield from i
   ...: 

In [6]: s = 'ABC'

In [7]: t = tuple(range(3))

In [8]: list(chain(s, t))
Out[8]: ['A', 'B', 'C', 0, 1, 2]
```

### yield from x

`yield from x` の処理

`iter(x)` を呼び出してそこからイテレータを取得する。（つまり `x` には任意のイテラブルを指定できる）。

最も外側に位置する呼び出し元から最も外側にあるサブジェネレータに対して双方向チャネルを開き、両者の間で直接的に値を送ったり戻したりできるようにできる。

用語

- デリゲーションジェネレータ（delegating generator）
    - `yield from <iterable>` を含むジェネレータ関数
- サブジェネレータ（subgenerator）
    - `yield from` の `<iterable>` 部分から取得したジェネレータ
- 呼び出し元（caller）
    - デリゲーションジェネレータを呼び出すクライアントコード

### coroaverager3.py の補足

```python
# the deligating generator
def grouper(results, key):
    while True:
        # ループごとに averager インスタンスを新規作成している
        # averager インスタンスはこルーチンとして動作するジェネレータオブジェクト
        # ここのループを抜けるために呼び出し元からの group.send(None) が必要
        results[key] = yield from averager()


# the client code, a.k.a. the caller
def main(data):
    results = {}
    for key, values in data.items():
        # group はジェネレータオブジェクト
        # コルーチンとして動作する
        group = grouper(results, key)
        # コルーチンの予備処理
        next(group)
        for value in values:
            # value を逐次的に grouper に送信する。
            # サブジェネレータ averager に直接値を送信する
            group.send(value)
        group.send(None) # important!(これによって averager インスタンスが停止する。)

    # 表示用の処理
    report(results)
```

- yield from の箇所で、デリゲーションジェネレータが休止している間、呼び出し元はサブジェネレータに直接データを送信（ `send` ）する。
- これに対し、サブジェネレータは呼び出し元にでデータを返信（ `yield` ）する。
- デリゲーションジェネレータはサブジェネレータが戻り値を返すと再開し、それに続いてインタプリタは戻り値を含んだ `StopIteration`　を上げる

`group.send(None)` をコメントアウトしたときの動きを考えてみる。

- `main` の外側の for はループのたびに `group` という名前の `grouper` インスタンス（デリゲーションジェネレータ）を新規に作成する。
- `next(group)` を呼び出すと、 `grouper` デリゲーションジェネレータが予備処理される
    - デリゲーションジェネレータは `while True` ループに入り、サブジェネレータの `averager()` を呼び出し、 `yield from` で休止する
- `main` の内側の for が呼び出した `group.send(value)` は、サブジェネレータの `averager` に直接値を送信する
    - この間、 `grouper` のその時点の `group` インスタンスは `yield from` で休止している
- 内側の for ループが完了しても、 `group` インスタンスはまだ `yield from` で休止したまま
    - `grouper` にある `results[key]` にも値は代入されていない
- 外側の for ループの末尾にある `group.send(None)` がなければ、 `averager` サブジェネレータは終了しない
    - デリゲーションジェネレータの `group` は休止したまま再開することはなく、 `results[key]` に値が代入されることもない
- 外側の for ループが次のループに戻ってくると、 `grouper` インスタンスがまた新規に作成され、 `group` にバインドされる
    - 前に用意された `grouper` インスタンスはガベージコレクトされる
    - このインスタンスの `averager` サブジェネレータも、終了しないまま一緒にコレクトされる
