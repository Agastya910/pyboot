from typing import List, Tuple


class TinyArray:
    def __init__(self, data: List[float]) -> None:
        self._data: List[float] = list(data)
        self._shape: Tuple[int, ...] = (len(self._data),)

    def __len__(self):
        return self._shape[0]

    def __getitem__(self, idx: int) -> float:
        return self._data[idx]

    def __setitem__(self, idx: int, value: float) -> None:
        self._data[idx] = value

    def mean(self) -> float:
        return sum(self._data) / len(self._data)

    def add(self, other: "TinyArray") -> "TinyArray":
        if len(self) != len(other):
            raise ValueError("shape mismatch")
        new_data = [x + y for x, y in zip(self._data, other._data)]
        return TinyArray(new_data)

    def square(self) -> "TinyArray":
        return TinyArray([x * x for x in self._data])
