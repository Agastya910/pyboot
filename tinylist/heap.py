from typing import TypeVar, Generic, List

T = TypeVar("T")


class MinHeap(Generic[T]):
    """Binary min-heap, O(logn) push/pop."""

    def __init__(self) -> None:
        self._data: List[T] = []
