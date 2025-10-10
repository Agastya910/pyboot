import csv
from pathlib import Path
from tinylist import TinyList
from tinylist.config import DownloadCFG
from typing import Tuple


def load_tiny(csv_path: Path) -> Tuple[TinyList, list[str]]:
    """Return TinyList of dicts and column order."""
    with csv_path.open(newline="") as f:
        reader = csv.DictReader(f)
        rows = TinyList()
        for row in reader:
            rows.append(row)
    return rows, reader.fieldnames or []


if __name__ == "__main__":
    cfg = DownloadCFG()
    data, cols = load_tiny(cfg.save_path)
    print("Rows:", len(data), "Cols:", cols)
    print("First row:", data[0])
