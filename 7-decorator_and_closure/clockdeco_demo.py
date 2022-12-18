import time
from clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))


"""
❯ python clockdeco_demo.py
**************************************** Calling snooze(.123)
[0.12592979s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00000135s] factorial(1) -> 1
[0.00002843s] factorial(2) -> 2
[0.00004450s] factorial(3) -> 6
[0.00005887s] factorial(4) -> 24
[0.00007332s] factorial(5) -> 120
[0.00009372s] factorial(6) -> 720
6! = 720
"""