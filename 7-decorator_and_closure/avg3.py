def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return averager

"""
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x101c461c0: list object at 0x101cc6780>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

"""
クロージャはその関数の定義時に存在している自由変数のバインディングを保持する関数。
バインドされた自由変数は、関数が呼び出され、定義時のスコープが利用可能でなくなったあとでも使用できる。
"""


avg = make_averager()
print(avg(10))