from fastapi import FastAPI, HTTPException
import base64
import io
import numpy as np
from PIL import Image
import onnxruntime as ort

app = FastAPI(title="cifar-onnx")

# 1. Create ORT Session
providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
sess = ort.InferenceSession("cifar_cnn.onnx", providers=providers)

input_name = sess.get_inputs()[0].name


def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


@app.post("/predict")
def predict(body: dict):
    try:
        # 2. Decode base64
        raw = base64.b64decode(body["image"])
        img = Image.open(io.BytesIO(raw)).convert("RGB")
        img = img.resize((32, 32))
        x = np.array(img).astype("float32") / 255.0  # 0-1
        x = (x - 0.5) / 0.5  # normalize
        x = np.transpose(x, (2, 0, 1))  # HWC -> CHW
        x = np.expand_dims(x, 0)  # add batch dim
        # 3. Inference
        logits = sess.run(None, {input_name: x})[0][0]
        prob = float(max(softmax(logits)))
        cls = int(np.argmax(logits))
        return {"class": cls, "prob": prob}
    except Exception as n:
        raise HTTPException(status_code=400, detail=str(n))
