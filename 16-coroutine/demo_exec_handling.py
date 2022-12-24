class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_exec_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            # DemoException のためだけの処理
            print("*** DemoException handled. Continueing...")
        else:
            # 例外が上がってこなければここの処理がよばれて send された値が出力される
            print("-> coroutine received: {!r}".format(x))
    raise RuntimeError("This line should never run.") # この処理は呼ばれない


def demo_finally():
    print("-> coroutine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException handled. Continueing...")
            else:
                print("-> coroutine received: {!r}".format(x))
    finally:
        print("-> coroutine ending")
