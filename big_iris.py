import pandas as pd
from tinylist.config import DownloadCFG

cfg = DownloadCFG()
df = pd.read_csv(cfg.save_path)
big = pd.concat([df] * 6667, ignore_index=True)
big.to_csv("data/big_iris.csv", index=False)
print("Rows:", len(big))
