from typing import Generic, TypeVar, Optional, List

K = TypeVar("K")
V = TypeVar("V")


class HashMap(Generic[K, V]):
    """Open-addressing hash map, no Python dict used."""

    def __init__(self, capacity: int = 8) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be >0")
        self._keys: List[Optional[K]] = [None] * capacity
        self._values: List[Optional[V]] = [None] * capacity
        self._size = 0
        self._cap = capacity

    def _hash(self, key: K) -> int:
        return hash(key) % self._cap

    def _resize(self) -> None:
        old_keys = self._keys[:]
        old_values = self._values[:]
        self._cap *= 2
        self._keys = [None] * self._cap
        self._values = [None] * self._cap
        self._size = 0
        for key, value in zip(old_keys, old_values):
            if key is not None:
                self[key] = value

    def __setitem__(self, key: K, value: V) -> None:
        idx = self._hash(key)
        if self._size >= 0.7 * self._cap:
            self._resize()
        was_empty = self._keys[idx] is None
        while self._keys[idx] is not None and self._keys[idx] != key:
            idx = (idx + 1) % self._cap
        self._keys[idx] = key
        self._values[idx] = value
        if was_empty:
            self._size += 1

    def __getitem__(self, key: K):
        idx = self._hash(key)
        while self._keys[idx] is not None:
            if self._keys[idx] == key:
                return self._values[idx]
            idx = (idx + 1) % self._cap
        raise KeyError(key)

    def __len__(self) -> int:
        return self._size
