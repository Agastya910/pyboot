from typing import Optional, Generic, TypeVar, Iterator

T = TypeVar("T")


class CircularDeque(Generic[T]):
    """Fixed-capacity deque, O(1) both ends."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be >0 ")
        self._cap = capacity
        self._data: list[Optional[T]] = [None] * capacity
        self._front = 0
        self._size = 0

    def append_left(self, value: T) -> None:
        if self._size == self._cap:
            raise OverflowError("deque is full")
        self._front = (self._front - 1) % self._cap
        self._data[self._front] = value
        self._size += 1

    def append_right(self, value: T) -> None:
        if self._size == self._cap:
            raise OverflowError("deque is full")
        idx = (self._front + self._size) % self._cap
        self._data[idx] = value
        self._size += 1

    def pop_left(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty deque")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return value

    def pop_right(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty deque")
        value = self._data[(self._front + self._size - 1) % self._cap]
        self._data[(self._front + self._size - 1) % self._cap] = None
        self._size -= 1
        return value

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        idx = self._front
        for _ in range(self._size):
            yield self._data[idx]
            idx = (idx + 1) % self._cap
