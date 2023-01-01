"""
https://peps.python.org/pep-0380/ を簡略化したもの
RESULT = yield from EXPR と等価な疑似コード
以下の条件で簡略化

- .throw() や .close() はなし
- 処理できる例外も StopIteration のみ
"""

def yield_from(EXPR):
    # イテレータ _i を取得するために iter() を用いているので、 EXPR には任意のイテラブルを指定できる
    _i = iter(EXPR) # サブジェネレータ
    try:
        # サブジェネレータが予備処理される
        # その結果は格納され、最初に yield される値 _y になる
        _y = next(_i)
    except StopIteration as _e:
        # StopIteration が上げられれば、例外から属性 value を取り出し、 _r に代入する
        # これが最もシンプルな場合の RESULT になる
        _r = _e.value
    else:
        # このループが回っている間、デリゲーションジェネレータはブロックされ、
        # 呼び出し元とサブジェネレータの間のチャネルとしてのみ機能する
        while 1:
            # サブジェネレータが生成したその時点の要素を生成し、呼び出し元から値 _s が送信されるのを待機する
            _s = yield _y
            try:
                # 呼び出し元が送信してきた _s を転送することで、サブジェネレータを進める
                _y = _i.send(_s)
            except StopIteration as _e:
                # サブジェネレータが StopIteration を上げてきたら value を取り出して _r に代入し、
                # ループを抜けることでデリゲーションジェネレータを再開させる
                _r = _e.value
                break

    # _r は　RESULT で yield from 式全体の値
    RESULT = _r


# EXPR はサブジェネレータとしてジェネレータの場合にのみ対応している
EXPR = (s for s in"ABC")
result = yield_from(EXPR)
# 結果の取り出し
print(list(result))
