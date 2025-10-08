from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    vocab_size: int
    d_model: int = 128
    n_layers: int = 4
    dropout: float = 0.1
    # default factory for mutable
    special_tokens: list[int] = field(default_factory=lambda: [0, 1])
