import subprocess
import pytest
import time
import requests
import io
import base64
from torchvision import datasets
import sys


@pytest.fixture(scope="module")
def server():
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "serve_onnx:app", "--port", "8081"]
    )
    url = "http://localhost:8001/docs"
    for _ in range(30):
        if requests.get(url).status_code == 200:
            break

        time.sleep(0.5)
    yield
    proc.terminate()
    proc.wait()


def test_predict(server: None):
    ds = datasets.CIFAR10(
        root="data/cifar10", train=False, download=False, transform=None
    )
    img = ds[0][0]
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    resp = requests.post("http://localhost:8001/predict", json={"image": b64})
    assert resp.status_code == 200
    data = resp.json()
    assert 0 <= data["class"] <= 9
    assert 0.0 <= data["prob"] <= 1.0
