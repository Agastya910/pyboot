import timeit
import numpy as np
from tinylist import TinyList


def for_loop():
    out = []
    for i in range(1_000_000):
        out.append(i * i)
    return out


def list_comp():
    return [i * i for i in range(1_000_000)]


def map_lambda():
    return list(map(lambda i: i * i, range(1_000_000)))


def numpy_way():
    arr = np.arange(1_000_000)
    return arr * arr


def tinylist_way():
    t = TinyList()
    for i in range(1_000_000):
        t.append(i * i)
    return t


for name, func in zip(
    ("for_loop", "list-comp", "map+lambda", "numpy-way", "tinylist-way"),
    (for_loop, list_comp, map_lambda, numpy_way, tinylist_way),
):
    t = min(timeit.repeat(func, number=1, repeat=3))
    print(f"{name}: {t:.2f} s")
