import logging


def deco(func):
    def inner(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return inner


@deco
def target():
    print('running target()')


target()
"""
running inner()
"""

print(target)
"""
<function deco.<locals>.inner at 0x108c7e4c0>
"""

