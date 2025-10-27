import pandas as pd
from iris_loader import load_tiny
from tinylist.config import DownloadCFG
from tinylist.heap import MinHeap


def top_k_variances(k: int = 2) -> list[str]:
    cfg = DownloadCFG()
    data, _ = load_tiny(cfg.save_path)
    heap = MinHeap[tuple[float, str]]()
    for col in cfg.feature_cols:
        series = pd.Series((float(row[col]) for row in data), dtype=float)
        neg_var = -series.var()
        heap.push((neg_var, col))
    return [col for _, col in [heap.pop() for _ in range(k)]]


if __name__ == "__main__":
    print("Top-2 highest variance features:", top_k_variances(2))
