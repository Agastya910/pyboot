import timeit
import heapq
from tinylist.heap import MinHeap


def builtin_heap(n: int = 100_000):
    h = []
    for x in range(n):
        heapq.heappush(h, -1 * x)
    for _ in range(n):
        heapq.heappop(h)


def our_heap(n: int = 100_000):
    h = MinHeap[int]()
    for x in range(n):
        h.push(-1 * x)
    for _ in range(n):
        h.pop()


for name, func in (("heapq", builtin_heap), ("tinylist_heap", our_heap)):
    t = min(timeit.repeat(func, number=1, repeat=3))
    print(f"{name:.8}: {t:.3f} s")
