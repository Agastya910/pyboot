import torch
import torch.nn.functional as F
from tiny_dataset import load_cifar_tensors, TinyDataset
from tiny_loader import TinyDataLoader
from cnn_model import TinyCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device", device)

train_imgs, train_lbls = load_cifar_tensors("train")
test_imgs, test_lbls = load_cifar_tensors("test")

train_loader = TinyDataLoader(
    TinyDataset(train_imgs, train_lbls), batch_size=64, shuffle=True
)
test_loader = TinyDataLoader(
    TinyDataset(test_imgs, test_lbls), batch_size=64, shuffle=False
)

model = TinyCNN().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
best_acc = 0.0
patience = 5
no_improve = 0
for epoch in range(50):
    model.train()
    running_loss = 0.0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(x)
        loss = F.cross_entropy(logits, y)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * x.size(0)

    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            logits = model(x)
            preds = logits.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += y.size(0)
        acc = correct / total
    print(f"Epoch {epoch}: loss={running_loss/len(train_lbls):.4f}, acc={acc:.4f}")
    if acc > best_acc:
        best_acc = acc
        no_improve = 0
        torch.save(model.state_dict(), "best_cifar.pt")
        print(" -> saved best_cifar.pt")
    else:
        no_improve += 1
        if no_improve >= patience:
            print(" -> early stop")
            break
