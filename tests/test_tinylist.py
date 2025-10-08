from tinylist import TinyList
import pytest


def test_append_pop():
    t = TinyList()
    t.append(1)
    t.append(2)
    assert len(t) == 2
    assert t.pop() == 2


def test_insert_negative_index():
    t = TinyList()
    for ch in "abc":
        t.append(ch)
    t.insert(-1, "Z")
    assert [t[i] for i in range(t.__len__())] == ["a", "b", "Z", "c"]


def test_remove_missing():
    t = TinyList()
    t.append(10)
    with pytest.raises(ValueError):
        t.remove(99)


def test_pop_empty():
    t = TinyList()
    with pytest.raises(IndexError):
        t.pop()


def test_leet_style():
    t = TinyList()
    sum = 0
    for i in range(10):
        t.append(i + 1)
        sum += i + 1
    assert sum == 55
    t.insert(0, 0)
    assert t[0] == 0
    assert t.pop() == 10 and t.__len__() == 10
    t.remove(5)
    assert 5 not in t
    return [x**2 for x in t]
