from concurrent import futures

from flags import save_flag, get_flag, show, main

# ThreadPoolExecutor で利用できる最大スレッド数
MAX_WORKERS = 20

def download_one(cc):
    # 画像を1枚ダウンロードする関数
    # スレッドはこれを実行する
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc

def download_many(cc_list):
    # 簡易的に5カ国のみ用いる
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # 実行すべき呼び出し可能オブジェクトをスケジューリングし、保留中の処理を表現する future を返す
            future = executor.submit(download_one, cc)
            # as_completed で扱えるように、リストへ格納する
            to_do.append(future)
            msg = "Scheduled for {}: {}"
            # 国別コードと対応する future を表示する
            print(msg.format(cc, future))

        results = []
        # futures が完了すると、 as_completed はインスタンスを yield する
        for future in futures.as_completed(to_do):
            # future の結果を取得する
            res = future.result()
            msg = "{} result: {!r}"
            # future とその結果を表示する
            print(msg.format(future, res))
            results.append(res)

    return len(list(res))


if __name__ == "__main__":
    main(download_many)


"""
❯ python flags_threadpool_ac.py

スケジューリングはアルファベット順。ワーカースレッドは3なので、3つが running (実行中)の状態
Scheduled for BR: <Future at 0x102afb940 state=running>
Scheduled for CN: <Future at 0x102b40190 state=running>
Scheduled for ID: <Future at 0x102b40970 state=running>
残り二つは pending (保留中)
Scheduled for IN: <Future at 0x102b41060 state=pending>
Scheduled for US: <Future at 0x102b41120 state=pending>

行の先頭はワーカースレッドの download_one が出力したもの。残りは download_many が出力したもの。
3つのワーカースレッドが download_many よりも先に結果を表示している
BR ID CN <Future at 0x102afb940 state=finished returned str> result: 'BR'
<Future at 0x102b40970 state=finished returned str> result: 'ID'
<Future at 0x102b40190 state=finished returned str> result: 'CN'
IN <Future at 0x102b41060 state=finished returned str> result: 'IN'
US <Future at 0x102b41120 state=finished returned str> result: 'US'

2 flags downloaded in 1.68s
"""


"""
実行結果はやるたびに変わる。以下が例
❯ python flags_threadpool_ac.py
Scheduled for BR: <Future at 0x10c427940 state=running>
Scheduled for CN: <Future at 0x10c46c190 state=running>
Scheduled for ID: <Future at 0x10c46c0d0 state=running>
Scheduled for IN: <Future at 0x10c46d150 state=pending>
Scheduled for US: <Future at 0x10c46d180 state=pending>
CN BR <Future at 0x10c46c190 state=finished returned str> result: 'CN'
<Future at 0x10c427940 state=finished returned str> result: 'BR'
ID <Future at 0x10c46c0d0 state=finished returned str> result: 'ID'
IN US <Future at 0x10c46d150 state=finished returned str> result: 'IN'
<Future at 0x10c46d180 state=finished returned str> result: 'US'

2 flags downloaded in 0.82s
"""
