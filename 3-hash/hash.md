# dict や set についてメモ

## dict でキーから値を取得する処理の流れ
`my_dict[search_key]` の値を取得するとき、Python は `hash(search_key)` を呼び出し、 search_key のハッシュ値を取得する。

そして、その値の数個の最下位ビットをオフセット位置として、ハッシュテーブル内のバケットをサーチする（使われるビットの個数は、その時点でのテーブルの大きさに依存する）。
見つけたバケットがからであれば、 KeyError が発生する。
そうでない場合、そのバケットには要素（found_key: found_value の組）が格納されている。

次に、 `search_key == found_key` であるかチェックする。
一致していればそれがサーチしていた要素であり、 found_value が返却される。

search_key と found_key が一致しないこともある。 →　ハッシュの衝突（hash collision）
衝突が発生するのは、ハッシュ関数が任意のオブジェクトをあまり多くないビット数で表現される値に対応づけるするため。
しかも、ハッシュテーブルのインデックスにはそのうちの数ビット分しか使われない。

衝突を解決するため、アルゴリズムはハッシュから異なるビットを取り込み、それをとある方法で変換した結果をオフセットに用いて、異なるバケットを検索する。
それが空であれば　KeyError が発生する。
そうでなければ、キーが一致しているとき要素の値が返却される。
一致していなければ、衝突解決の処理が繰り返される。

## dict で要素の挿入と更新の手順
見つかったの空のバケットならばそこに要素が新たに置かれ、一致したキーならばそのバケットの値は新しい値で上書きされる点だけ異なる。
要素を挿入するとき、はッシュテーブルが混んできたと判断されると、スペースに余裕のある新しい場所にはッシュテーブルを再構築することがある。
ハッシュテーブルが大きくなるにつれ、バケットのオフセットとして使用されるハッシュのビット数も多くなるので、衝突する確率を低く保てる。

dict に数百万個の要素があっても、サーチの大半では衝突は発生せず、サーチ一回あたりの平均衝突回数は1回ないし2回程度。
普通の運用条件下では、最悪の場合でも衝突解決を何回か実行すればキーは見つかる。

## オブジェクトがハッシュ可能であるための条件
- `__hash__()` メソッドを介して　`hash()` 関数を利用できる。かつ、この関数はオブジェクトの有効期間内であれば常に同じ値を返す。
- `__eq__()` メソッドを介して等値性の判定ができる。
- `a == b` が `True` ならば `hash(a) == hash(b)` も True になる。


## dict には顕著なメモリオーバーヘッドがある
ハッシュテーブルは疎でなくてはならないため、スペース効率が良くない。
大量の dict が要素になるリストを作る場合は、 dict よりもタプルの方が効率が良い。

## キーサーチは非常に高速
メモリのオーバーヘッドと引き換えにアクセス速度は dict のサイズに関係なく高速である。
