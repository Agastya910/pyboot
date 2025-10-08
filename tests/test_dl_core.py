from tinylist.dl_core import stable_softmax, cross_entropy


def test_softmax():
    s = stable_softmax([1, 2, 3])
    assert abs(sum(s) - 1.0) < 1e-6
    assert s[-1] > s[0]


def test_cross_entropy():
    loss = cross_entropy([0.2, 0.8], target=1)
    assert abs(loss - 0.22314) < 1e-4
