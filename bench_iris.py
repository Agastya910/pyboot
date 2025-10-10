from tinylist.config import DownloadCFG
from tinylist import TinyList
from collections import defaultdict
import numpy as np
import pandas as pd
import timeit
from iris_loader import load_tiny

cfg = DownloadCFG()
data, cols = load_tiny(cfg.save_path)


def tiny_loop() -> defaultdict:
    floats = defaultdict(TinyList)
    for col in cols[:3]:
        floats[col] = [list(float(row[col]) for row in data)]
    return floats


tiny_time = min(timeit.repeat(tiny_loop, number=1000, repeat=3))
print(f"tinylist time= {tiny_time:.3f}")


def pandas_loop() -> list:
    return [
        pd.Series((float(row[col]) for row in data), dtype=float) for col in cols[:3]
    ]


pandas_time = min(timeit.repeat(pandas_loop, number=1000, repeat=3))

print(f"pandas time = {pandas_time:.3f}")


def numpy_loop() -> list:
    return [np.fromiter((row[col] for row in data), dtype=float) for col in cols[:3]]


numpy_time = min(timeit.repeat(numpy_loop, number=1000, repeat=3))

print(f"numpy_time = {numpy_time:.3f}")
