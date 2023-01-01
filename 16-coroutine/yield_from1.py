"""
https://peps.python.org/pep-0380/ を簡略化したもの
RESULT = yield from EXPR と等価な疑似コード
"""
import sys

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
            try:
                # サブジェネレータが生成したその時点の要素を生成し、呼び出し元から値 _s が送信されるのを待機する
                _s = yield _y
            except GeneratorExit as _e:
                # デリゲーションジェネレータとサブジェネレータを終了させるときの処理
                # サブジェネレータは任意のイテレータで良いため、 close メソッドが存在しない場合もある
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:
                # 呼び出し元が .throw(...) を使って投げてきた例外を処理する
                # サブジェネレータがイテレータであり、そこに呼び出せる throw がないときはデリゲーションジェネレータで例外を上げる
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:
                    # サブジェネレータに throw メソッドが備わっているならば、呼び出し元からの例外を使ってそれを呼び出す
                    # サブジェネレータは例外を処理（ループが続行できる）することもあれば、 StopIteration を上げる（そこから _r が取り出されてループが終了）こともある
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:
                # yield で例外が上げられなかったときの処理
                try:
                    # サブジェネレータを進める
                    if _s is None:
                        # 呼び出し元から受信した最後の値が None ならば、サブジェネレータの next を呼び出す
                        # それ以外なら send を呼び出す
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    # サブジェネレータが StopIteration を上げてきたら value を取り出して _r に代入し、
                    # ループを抜けることでデリゲーションジェネレータを再開させる
                    _r = _e.value
                    break

    # _r は　RESULT で yield from 式全体の値
    RESULT = _r


EXPR = "ABC"
result = yield_from(EXPR)
# 結果の取り出し
print(list(result))
