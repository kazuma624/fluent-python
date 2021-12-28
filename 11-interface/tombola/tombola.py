import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, interable):
        # 抽象メソッドはだいたい中身をカラにして docstrig だけ書くようにする
        # 抽象基底クラスが存在しなかった頃は NotImplementedError を上げるようにしていた
        # 抽象基底クラスを使うと NotImplementedError ではなく TypeError を上げる
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """
        # 取得する要素がないときは LookupError を上げるように docstring が実装者に指示している

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        # 抽象基底クラスの具象メソッドは抽象基底クラスによって定義されたインターフェースだけに依存しなければならない
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                # 具象サブクラスがどのように要素を収容しているかは知ることができない。
                # しかし .pick() を連続して呼び出して Tombola オブジェクトを空にすることにより
                # inspect の結果を作成できる。
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
