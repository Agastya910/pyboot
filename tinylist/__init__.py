from typing import Any


class TinyList:
    def __init__(self) -> None:
        self._capacity = 2
        self._size = 0
        self._data = [None] * self._capacity

    def append(self, value: Any) -> None:
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = value
        self._size += 1

    def _resize(self) -> None:
        new_cap = self._capacity * 2
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap

    def __len__(self) -> int:
        return self._size

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0:
            idx = self._size + idx
        if idx < 0:
            idx = 0
        if idx > self._size:
            idx = self._size

        if self._size == self._capacity:
            self._resize()
        for i in range(self._size, idx, -1):
            self._data[i] = self._data[i - 1]
        self._data[idx] = value
        self._size += 1

    def pop(self, idx: int = -1) -> Any:
        if self._size == 0:
            raise IndexError("Cannot pop from an empty list")
        if idx < 0:
            idx = self._size + idx
        if idx < 0:
            idx = 0
        if idx > self._size:
            return IndexError("TinyList index out of range")
        popped = self._data[idx]
        self._data[idx] = None
        for i in range(idx, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return popped

    def remove(self, value: Any) -> None:
        """Remove first occurence of value. Raise ValueError if not found."""
        for i in range(self._size):
            if self._data[i] == value:
                self.pop(i)
                return None
        raise ValueError("Value not found in the list")

    def __getitem__(self, idx: int) -> Any:
        if 0 <= idx < self._size:
            return self._data[idx]
        raise IndexError("TinyList index out of range")


# t= TinyList()
# for ch in "Python":
#     t.append(ch)
# print("length:",t.__len__() )
# print("item 2:", t.__getitem__(2))
# t.insert(2,'!')
# print("after insert:", [t[i] for i in range(len(t))])
# print("popped:", t.pop())
# print("list after pop", [t[i] for i in range(t.__len__())])
# print("popped 2:", t.pop(1))
# print("list after pop", [t[i] for i in range(t.__len__())])
