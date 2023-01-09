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
    # ワーカースレッド数を設定する。余計なスレッドを生成しないために最小値を取る
    workers = min(MAX_WORKERS, len(cc_list))
    # ワーカースレッド数を指定して ThreadPoolExecutor をインスタンス化する。
    # executor.__exit__ メソッドから呼び出される executor.shutdown(wait=True) は、
    # すべてのスレッドが完了するまでブロックされる。
    with futures.ThreadPoolExecutor(workers) as executor:
        # 指定の downloas_one 関数が複数のスレッドから並行して呼び出される点で、組み込み関数 map と少し違う。
        # このメソッドで、それぞれの関数が返した値を反復処理で取得できるジェネレータを返す
        res = executor.map(download_one, sorted(cc_list))

    # 得られた結果の数を返す。
    # スレッド化された呼び出しが例外をあげると、
    # イテレータから対応する戻り値を取得しようとした暗黙的な next() 呼び出しの例外として、ここで上げられる
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
