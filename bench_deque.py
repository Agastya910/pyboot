import timeit
from collections import deque
from tinylist.deque import CircularDeque


def builtin_deque_test(n: int = 100_000):
    d = deque()
    for i in range(n):
        d.append(i)
        d.appendleft(-i)
    for _ in range(n):
        d.pop()
        d.popleft()


def our_deque_test(n: int = 100_000):
    d = CircularDeque(2 * n + 1)
    for i in range(n):
        d.append_right(i)
        d.append_left(-i)
    for _ in range(n):
        d.pop_right()
        d.pop_left()


for name, func in (
    ("collections.deque", builtin_deque_test),
    ("CircularDeque", our_deque_test),
):
    t = min(timeit.repeat(lambda: func(), number=1, repeat=3))
    print(f"{name:18}:{t:.3f} s")
