from typing import List, Iterator
from tiny_dataset import TinyDataset
import torch


class TinyDataLoader:
    def __init__(
        self,
        dataset: TinyDataset,
        batch_size: int = 64,
        shuffle: bool = True,
        drop_last: bool = False,
    ):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.drop_last = drop_last
        self.indices = list(range(len(dataset)))
        if shuffle:
            import random

            random.shuffle(self.indices)

    def __iter__(self) -> Iterator[List[torch.Tensor]]:
        for i in range(0, len(self.indices), self.batch_size):
            batch_indices = self.indices[i : i + self.batch_size]
            if len(batch_indices) < self.batch_size and self.drop_last:
                continue
            images = [self.dataset[idx][0] for idx in batch_indices]
            labels = [self.dataset[idx][1] for idx in batch_indices]
            yield torch.stack(images), torch.tensor(labels)
