def gen():
    yield from 'AB'
    yield from range(1, 3)

def gen2():
    for c in 'AB':
        yield c

    for i in range(1, 3):
        yield i


def chain(*iterables):
    for i in iterables:
        yield from i


def chain2(*iterables):
    for iter in iterables:
        for i in iter:
            yield i


r = gen()
print('generatorのまま出力', r)
print('中身を全部生成', list(r))

print('-' * 32)

r = gen2()
print('generatorのまま出力', r)
print('中身を全部生成', list(r))

print('=' * 32)

s = 'ABC'
t = tuple(range(3))
r = list(chain(s, t))
print(r)
# ['A', 'B', 'C', 0, 1, 2]

print('-' * 32)

s = 'ABC'
t = tuple(range(3))
r = list(chain2(s, t))
print(r)
# ['A', 'B', 'C', 0, 1, 2]
