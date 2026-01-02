import torch
from cnn_model import TinyCNN

device = "cuda" if torch.cuda.is_available() else "cpu"
model = TinyCNN()

model.load_state_dict(torch.load("best_cifar.pt"))
model.eval()

dummy = torch.randn(1, 3, 32, 32).to(device)
out = model(dummy)

print("output shape:", out.shape)
