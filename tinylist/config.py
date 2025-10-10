from dataclasses import dataclass
from pathlib import Path


@dataclass
class DownloadCFG:
    url: str = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    save_path: Path = Path("data/iris.csv")
    target_col: str = "species"
    feature_cols: tuple[str, ...] = (
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    )
