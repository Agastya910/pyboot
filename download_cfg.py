import requests
from tinylist.config import DownloadCFG


def download(cfg: DownloadCFG) -> None:
    cfg.save_path.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading...", cfg.url)
    resp = requests.get(cfg.url, timeout=30)
    resp.raise_for_status()
    cfg.save_path.write_text(resp.text)
    print("Saved", cfg.save_path, f"({len(resp.text)} bytes)")


if __name__ == "__main__":
    download(DownloadCFG())
