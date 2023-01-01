from collections import namedtuple

Result = namedtuple("Result", "count average")

# the subgenerator
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield # main が送信する値は、この term にバインドされる
        if term is None:
            # ループを抜けるための条件
            break
        total += term
        count += 1
        average = total/count

    return Result(count, average) # grouper 関数にある yield from が返す値


# the deligating generator
def grouper(results, key):
    while True:
        # ループごとに averager インスタンスを新規作成している
        # averager インスタンスはこルーチンとして動作するジェネレータオブジェクト
        results[key] = yield from averager()
        """
        grouper は値を受け取るたびに yield from を使って averager インスタンスに値を流し込む。
        averager がクライアントから送信されてくる値を取り込んでいる限り、 grouper はここで停止する。
        averager インスタンスが値をすべて受け取り終えると、帰ってきた値は results[key] にバインドされる。
        これが終わると、 while ループは次の averager インスタンスを生成し、さらに値を処理していく。
        """


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
            group.send(value)
        group.send(None) # important!(これによって averager インスタンスが停止する。)

    # print(results) # uncomment debug
    report(results)

# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print("{:2} {:5} averaging {:.2f}{}".format(
            result.count, group, result.average, unit))

data = {
    "girls;kg":
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "girls;m":
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    "boys;kg":
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    "boys;m":
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == "__main__":
    main(data)
