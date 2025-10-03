from tinylist import TinyList
import pytest

def test_append_pop():
    t = TinyList()
    t.append(1)
    t.append(2)
    assert len(t) ==2
    assert t.pop() ==2

def test_insert_negative_index():
    t=TinyList()
    for ch in "abc":
        t.append(ch)
    t.insert(-1, 'Z')
    assert [t[i] for i in range(t.__len__())]==['a', 'b','Z','c']

def test_remove_missing():
    t= TinyList()
    t.append(10)
    with pytest.raises(ValueError):
        t.remove(99)

def test_pop_empty():
    t = TinyList()
    with pytest.raises(IndexError):
        t.pop()