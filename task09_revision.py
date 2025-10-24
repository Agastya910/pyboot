from math import isqrt
from typing import Iterator


def primes() -> Iterator:
    primes_seen = [2]
    yield 2
    candidate = 3
    while True:
        flag = 0
        for p in primes_seen:
            if p > isqrt(candidate):
                break
            if candidate % p == 0:
                flag = 1
                break
        if flag == 0:
            primes_seen.append(candidate)
            yield candidate
        candidate += 2


if __name__ == "__main__":
    p = primes()
    print([next(p) for _ in range(11)])
