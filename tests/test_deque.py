import pytest
from tinylist.deque import CircularDeque


def test_both_ends():
    d = CircularDeque(4)
    for i in [10, 20, 30]:
        d.append_right(i)
    assert d.pop_left() == 10
    assert d.pop_right() == 30
    assert len(d) == 1


def test_full_then_empty():
    d = CircularDeque(3)
    for i in range(1, 4):
        d.append_left(i)
    with pytest.raises(OverflowError):
        d.append_left(4)
    assert [d.pop_left() for _ in range(3)] == [3, 2, 1]
    with pytest.raises(IndexError):
        d.pop_left()


def test_iteration():
    d = CircularDeque(5)
    for i in [5, 6, 7]:
        d.append_right(i)
    assert list(d) == [5, 6, 7]
