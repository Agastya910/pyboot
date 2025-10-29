import timeit
from tinylist.hashmap import HashMap


def builtin_dict(n: int = 100_000):
    d = {}
    for i in range(n):
        d[i] = i
    for i in range(n):
        _ = d[i]


def our_hashmap(n: int = 100_000):
    m = HashMap[int, int]()
    for i in range(n):
        m[i] = i
    for i in range(n):
        _ = m[i]


for name, func in (("built-in dict", builtin_dict), ("our_hashmap", our_hashmap)):
    t = min(timeit.repeat(func, repeat=1, number=3))
    print(f"{name:14}: {t:.3f}s")
