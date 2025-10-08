# from dataclasses import dataclass
from math import exp, log


def stable_softmax(x: list[float]) -> list[float]:
    """Pure-Python softmax; overflow-safe."""
    max_ = max(x)
    exps = [exp(v - max_) for v in x]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]


def cross_entropy(pred: list[float], target: int) -> float:
    """Negative log-likelihood for single true class index."""
    return -log(pred[target] + 1e-12)
