from dataclasses import dataclass


@dataclass
class Params:
    lr: float
    batch_size: int
    training_split = 0.8
    val_split = 0.1
    test_split = 0.1


params = Params(lr=1e-3, batch_size=32)


print(params.lr, params.batch_size)
