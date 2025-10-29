from tinylist.array import TinyArray
import math


def stable_softmax_vec(x: TinyArray) -> TinyArray:
    max_val = max(x._data)
    exps = TinyArray([math.exp(val - max_val) for val in x._data])
    # exps= TinyArray(list(map(lambda x: math.exp(x-max_val), x._data )))
    sum_exp = sum(exps._data)
    return TinyArray([v / sum_exp] for v in exps._data)


def softmax_jacobian_vec(p: TinyArray) -> TinyArray:
    n = len(p)
    jac = []
    for i in range(n):
        diag = p[i] * (1 - p[i])
        jac.append(diag)
    return TinyArray(jac)
