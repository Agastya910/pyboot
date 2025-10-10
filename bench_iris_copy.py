from tinylist.config import DownloadCFG
from tinylist import TinyList
import numpy as np
import pandas as pd
import timeit
from iris_loader import load_tiny

cfg = DownloadCFG()
data, cols = load_tiny(cfg.save_path)


def tiny_loop() -> TinyList:
    out = TinyList()
    for row in data:
        out.append(float(row["sepal_length"]))


tiny_time = min(timeit.repeat(tiny_loop, number=1000, repeat=3))
print(f"tinylist time= {tiny_time:.3f}")


def pandas_loop() -> pd.Series:
    return pd.Series((float(row["sepal_length"]) for row in data), dtype=float)


pandas_time = min(timeit.repeat(pandas_loop, number=1000, repeat=3))

print(f"pandas time = {pandas_time:.3f}")


def numpy_loop() -> np.ndarray:
    return np.fromiter(
        (float(row["sepal_length"]) for row in data), dtype=float, count=len(data)
    )


numpy_time = min(timeit.repeat(numpy_loop, number=1000, repeat=3))

print(f"numpy_time = {numpy_time:.3f}")
