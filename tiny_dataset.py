from typing import List, Tuple
import torch
import pathlib


class TinyDataset:
    def __init__(self, images: List[torch.Tensor], labels: List[int]):
        self.images = images
        self.labels = labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, int]:
        return self.images[idx], self.labels[idx]


def load_cifar_tensors(split: str = "train") -> Tuple[List[torch.Tensor], List[int]]:
    from torchvision import datasets, transforms

    transform = transforms.Compose([transforms.ToTensor()])
    data_dir = pathlib.Path("data/cifar10")
    dataset = datasets.CIFAR10(
        root=data_dir, train=(split == "train"), download=False, transform=transform
    )
    images, labels = [], []
    for img, lbl in dataset:
        images.append(img)
        labels.append(lbl)
    return images, labels
