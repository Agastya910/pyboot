from generators import primes
from memory_profiler import profile


@profile
def list_way():
    p = primes()
    return [next(p) for _ in range(100_000)]


@profile
def gen_way():
    p = primes()
    for _ in range(100_000):
        _ = next(p)


if __name__ == "__main__":
    list_way()
    gen_way()
