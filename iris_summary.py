import pandas as pd
from iris_loader import load_tiny
from tinylist.config import DownloadCFG


def show_summary() -> None:
    cfg = DownloadCFG()
    data, cols = load_tiny(cfg.save_path)
    numeric_cols = [c for c in cfg.feature_cols]
    for col in numeric_cols:
        series = pd.Series((float(row[col]) for row in data), dtype=float)
        print(f"{col:12} mean={series.mean():.3f} std= {series.std():.3f}")


def show_summary_dict() -> dict:
    cfg = DownloadCFG()
    data, cols = load_tiny(cfg.save_path)
    numeric_cols = [c for c in cfg.feature_cols]
    out = {}
    for col in numeric_cols:
        series = pd.Series((float(row[col]) for row in data), dtype=float)
        out[col] = {"mean": round(series.mean(), 3), "std": round(series.std(), 3)}
    return out
