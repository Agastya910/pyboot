import pytest
from tinylist.heap import MinHeap


def test_push_pop():
    h = MinHeap()
    for x in [5, 3, 7, 1]:
        h.push(x)
    assert [h.pop() for _ in range(4)] == [1, 3, 5, 7]


def test_empty_pop():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()


def test_generic_type():
    h = MinHeap[str]()
    h.push("b")
    h.push("a")
    assert h.pop() == "a"
