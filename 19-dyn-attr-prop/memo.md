# 19章 動的属性とプロパティ

- 属性(attribute)
  - データ属性、メソッド
- プロパティ
  - インタフェースを変更せずともパブリックなデータ属性を getter/setter といった accessor メソッドで置き換えることができる。



統一アクセス原理

```
モジュールが提供するサービスは、実装がストレージを介していようと演算によるものであろうと変わることなく、すべて統一された表記を介して利用できるべきである。
```

## `__new__` メソッド

- 実際にインスタンスを構築する特殊メソッドは `__init__` ではなく `__new__`
- `__new__` はクラスメソッドであり、必ずインスタンスを返す
  - 特別な扱いがなされるため @classmethod デコレータは不要
- 返却されたインスタンスは、 `__init__` の第一引数である `self` に渡される

疑似コードでPythonがオブジェクトを作成するプロセスを表現する

```python
def object_maker(the_class, some_arg):
    new_object = the_class.__new__(some_arg)
    if isinstance(new_oject, some_arg)
        the_class.__init__(new_object, some_arg)
```

上記を用いると、以下の二つはほぼ等価。

```python
x = Foo('bar')
x = object_maker(Foo, 'bar')
```
