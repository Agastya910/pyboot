# ---------- CPU ----------
FROM python:3.11-slim AS cpu
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
COPY . .
RUN pip install -e .
EXPOSE 8000
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------- GPU ----------
FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime AS gpu
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install onnxruntime-gpu fastapi uvicorn pillow numpy torchvision 

COPY serve_onnx.py /app/
COPY artifacts/cifar_cnn.onnx /app/
# RUN pip install -e .
EXPOSE 8001
CMD ["uvicorn", "serve_onnx:app", "--host", "0.0.0.0", "--port", "8000"]
