import torch
import pathlib
from cnn_model import TinyCNN

device = "cuda" if torch.cuda.is_available() else "cpu"
model = TinyCNN().to(device)
model.load_state_dict(torch.load("best_cifar.pt", map_location=device))
model.eval()

dummy = torch.randn(1, 3, 32, 32).to(device)

pathlib.Path("artifacts").mkdir(exist_ok=True)

torch.onnx.export(
    model,
    dummy,
    "artifacts/cifar_cnn.onnx",
    input_names=["image"],
    output_names=["logits"],
    opset_version=14,
)

traced = torch.jit.trace(model, dummy)
traced.save("artifacts/cifar_cnn.pt")

for f in ("cifar_cnn.onnx", "cifar_cnn.pt"):
    kb = pathlib.Path("artifacts", f).stat().st_size / 1024
    print(f"{f}: {kb:.0f} KB")
