import pytest
from tinylist.hashmap import HashMap


def test_set_get():
    m = HashMap[str, int]()
    m["a"] = 1
    assert m["a"] == 1
    assert len(m) == 1


def test_resize():
    m = HashMap[int, int](capacity=4)
    for i in range(10):
        m[i] = i
    assert len(m) == 10
    assert m[9] == 9


def test_key_error():
    m = HashMap()
    with pytest.raises(KeyError):
        m["missing"]
