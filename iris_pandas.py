from iris_loader import load_tiny
from pathlib import Path
from tinylist.config import DownloadCFG
import pandas as pd


def gen_pandas(csv_path: Path, feature_cols: tuple[str, ...]) -> None:
    data, cols = load_tiny(csv_path)
    floats = (float(row[feature_cols[0]]) for row in data)
    s = pd.Series(floats, dtype=float)
    print(f"{feature_cols[0]} mean = {s.mean():.3f}")


if __name__ == "__main__":
    cfg = DownloadCFG()
    gen_pandas(cfg.save_path, cfg.feature_cols)
