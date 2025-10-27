from typing import TypeVar, Generic, List

T = TypeVar("T")


class MinHeap(Generic[T]):
    """Binary min-heap, O(logn) push/pop."""

    def __init__(self) -> None:
        self._data: List[T] = []

    def push(self, value: T) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[parent] <= self._data[idx]:
                break
            self._data[parent], self._data[idx] = self._data[idx], self._data[parent]
            idx = parent

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty heap")
        root = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return root

    def _sift_down(self, idx: int) -> None:
        n = len(self._data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._data[idx], self._data[smallest] = (
                self._data[smallest],
                self._data[idx],
            )
            idx = smallest
