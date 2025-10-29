import pathlib
from torchvision import datasets, transforms

DATA_DIR = pathlib.Path("data/cifar10")
transform = transforms.Compose([transforms.ToTensor()])
train_set = datasets.CIFAR10(
    root=DATA_DIR, train=True, download=True, transform=transform
)
test_set = datasets.CIFAR10(
    root=DATA_DIR, train=False, download=True, transform=transform
)

print("Train:", len(train_set), "Test:", len(test_set))
print("Shape:", train_set[0][0].shape, "Label:", train_set[0][1])
