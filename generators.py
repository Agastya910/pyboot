from typing import Iterator
from math import isqrt
from itertools import islice, count
from collections import deque


def primes() -> Iterator[int]:
    """Yeild infinite stream of primes."""
    candidate = 2
    yield candidate
    primes_seen = [candidate]
    candidate += 1
    while True:
        for p in primes_seen:
            if p > isqrt(candidate):
                primes_seen.append(candidate)
                yield candidate
                break
            if candidate % p == 0:
                break
        else:
            primes_seen.append(candidate)
            yield candidate

        candidate += 2


def primes_it() -> Iterator[int]:
    """Same logic, but uses itertools.count and islice"""
    primes_seen: list[int] = []
    for candidate in count(2):
        if all(candidate % p for p in islice(primes_seen, 0, int(candidate**0.5) + 1)):
            primes_seen.append(candidate)
            yield candidate


def rolling_prime_avg(k: int = 1000) -> Iterator[float]:
    """Yield running mean of last k primes."""
    window: deque[int] = deque(maxlen=k)
    for p in primes_it():
        window.append(p)
        if len(window) == k:
            yield sum(window) / k
