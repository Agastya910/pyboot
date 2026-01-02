import numpy as np


class MultiHeadAttention:
    def __init__(self, d_model: int, n_heads: int):
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.w_q = np.random.randn(d_model, d_model).astype(np.float32) * 0.02
        self.w_k = np.random.randn(d_model, d_model).astype(np.float32) * 0.02
        self.w_v = np.random.randn(d_model, d_model).astype(np.float32) * 0.02
        self.w_o = np.random.randn(d_model, d_model).astype(np.float32) * 0.02

    def forward(self, x: np.ndarray) -> np.ndarray:
        """x shape (batch, seq, d_model) -> same shape"""
        q = x @ self.w_q
        k = x @ self.w_k
        v = x @ self.w_v
        q = split_heads(q, self.n_heads)
        k = split_heads(k, self.n_heads)
        v = split_heads(v, self.n_heads)
        head_outs = []
        for h in range(self.n_heads):
            head_outs.append(batched_attention(q[:, h], k[:, h], v[:, h]))
        concat = np.concatenate(head_outs, axis=-1)
        return concat @ self.w_o


def split_heads(x: np.ndarray, n_heads: int) -> np.ndarray:
    b, seq, d_model = x.shape
    assert d_model % n_heads == 0
    d_head = d_model // n_heads
    x = x.reshape(b, seq, n_heads, d_head).transpose(0, 2, 1, 3)  # (B, H, T, Dh)
    return x


def softmax(x: np.ndarray, axis=-1) -> np.ndarray:
    """stable softmax"""
    exps = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return exps / np.sum(exps, axis=axis, keepdims=True)


def attention(q: np.ndarray, k: np.ndarray, v: np.ndarray) -> np.ndarray:
    """scaled dot product attention"""
    return np.dot(softmax(np.dot(q, k.T) / np.sqrt(k.shape[-1])), v)


def batched_attention(q, k, v):
    out = []
    for b in range(q.shape[0]):
        out.append(attention(q[b], k[b], v[b]))
    return np.stack(out)


def cross_entropy(logits: np.ndarray, targets: np.ndarray) -> float:
    B, S, V = logits.shape
    logits = logits.reshape(-1, V)
    targets = targets.ravel()
    probs = softmax(logits, axis=-1)
    correct = probs[np.arange(len(targets)), targets]
    return -np.log(correct + 1e-9).mean()


class TransformerBlock:
    def __init__(self, d_model: int, n_heads: int, d_ff: int):
        self.mha = MultiHeadAttention(d_model, n_heads)
        # two learned matrices for FFN
        self.w1 = np.random.randn(d_model, d_ff).astype(np.float32) * 0.02
        self.w2 = np.random.randn(d_ff, d_model).astype(np.float32) * 0.02
        # Learned LayerNorm params (gamma, beta)
        self.gamma = np.ones(d_model, dtype=np.float32)
        self.beta = np.zeros(d_model, dtype=np.float32)

    def ln(self, x: np.ndarray) -> np.ndarray:
        """Layer Norm (x shape any, last axis = features)"""
        mean = x.mean(axis=-1, keepdims=True)
        var = x.var(axis=-1, keepdims=True)
        return self.gamma * (x - mean) / np.sqrt(var + 1e-5) + self.beta

    def ff(self, x: np.ndarray) -> np.ndarray:
        """FFN: linear-> relu -> linear"""
        return np.maximum(0, x @ self.w1) @ self.w2

    def forward(self, x: np.ndarray) -> np.ndarray:
        """pre-norm: ln -> mha -> residual -> ln -> ff -> residual"""
        x = x + self.mha.forward(self.ln(x))
        x = x + self.ff(self.ln(x))
        return x


def positional_encoding(seq_len: int, d_model: int) -> np.ndarray:
    """sin/cos positional matrix (seq_len, d_model)"""
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            angle = pos / (10000 ** (i / d_model))
            pe[pos, i] = np.sin(angle)
            if i + 1 < d_model:
                pe[pos, i + 1] = np.cos(angle)
    return pe.astype(np.float32)


class TinyTransformer:
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        n_heads: int,
        n_layers: int,
        d_ff: int,
        seq_len: int,
    ):
        self.embed = np.random.randn(vocab_size, d_model).astype(np.float32) * 0.02
        self.pe = positional_encoding(seq_len, d_model)
        self.blocks = [
            TransformerBlock(d_model, n_heads, d_ff) for _ in range(n_layers)
        ]
        self.ln_final = lambda x: (x - x.mean(axis=-1, keepdims=True)) / np.sqrt(
            x.var(axis=-1, keepdims=True) + 1e-5
        )
        self.w_vocab = np.random.randn(d_model, vocab_size).astype(np.float32) * 0.02

    def forward(self, x: np.ndarray):
        """x: (batch, seq) ints -> (batch, seq, d_model)"""
        x = self.embed[x] + self.pe
        for block in self.blocks:
            x = block.forward(x)
        x = self.ln_final(x)
        return x @ self.w_vocab  # (B, T, vocab_size)


def causal_mask(seq_len: int) -> np.ndarray:
    """lower-triangular 0/-inf mask (seq_len, seq_len)"""
    mask = np.triu(np.ones((seq_len, seq_len)), k=1) * -1e9
    return mask.astype(np.float32)


def load_text(
    path: str, seq_len: int
) -> tuple[dict[str, int], dict[int, str], np.ndarray]:
    text = open(path, encoding="utf=8").read()
    chars = sorted(list(set(text)))
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for i, ch in enumerate(chars)}
    data = np.array([stoi[c] for c in text], dtype=np.int32)
    return stoi, itos, data


def data_loader(data: np.ndarray, seq_len: int, batch_size: int):
    """infinite character batches"""
    n = len(data) - seq_len
    while True:
        ix = np.random.randint(0, n, batch_size)
        x = np.stack([data[i : i + seq_len] for i in ix])
        y = np.stack([data[i + 1 : i + seq_len + 1] for i in ix])
        yield x, y


def generate(
    model: TinyTransformer,
    prompt: str,
    stoi: dict,
    itos: dict,
    max_new: int = 200,
    beam: int = 3,
):
    """char-level beam search"""
    tokens = [stoi[c] for c in prompt[-64:]]
    if len(tokens) < 64:
        tokens = [0] * (64 - len(tokens)) + tokens
    tokens = np.array(tokens, dtype=np.int32)
    beams = [(0.0, tokens)]
    for _ in range(max_new):
        new_beams = []
        for logp, seq in beams:
            logits = model.forward(seq[None, :])[0, -1, :]
            log_probs = np.log(softmax(logits))
            top_k = np.argpartition(log_probs, -beam)[-beam:]
            for idx in top_k:
                new_seq = np.concatenate([seq[1:], [idx]])
                new_beams.append((logp + log_probs[idx], new_seq))
        beams = sorted(new_beams, key=lambda x: x[0], reverse=True)[:beam]
    best = beams[0][1]
    return "".join(itos[i] for i in best)


if __name__ == "__main__":
    stoi, itos, data = load_text("shakespeare.txt", seq_len=64)
    vocab_size = len(stoi)
    model = TinyTransformer(
        vocab_size, d_model=256, n_heads=8, n_layers=4, d_ff=512, seq_len=64
    )
    loader = data_loader(data, 64, 4)
    for step in range(int(10)):
        x, y = next(loader)
        logits = model.forward(x)
        loss = cross_entropy(logits, y)
        print(f"step: {step} : loss = {loss:.3f}")
    print(
        "sample:", generate(model, "First citizen:\n", stoi, itos, max_new=200, beam=2)
    )


# mask = causal_mask(10)
# print("mask shape:", mask.shape)
# print("upper-right corner:\n", mask[:3, :3])

# model = TinyTransformer(vocab_size=1000, d_model=512, n_heads=8, n_layers=4, d_ff=2048, seq_len=64)
# dummy_tokens = np.random.randint(0, 1000, size=(2, 64)).astype(np.int32)
# out = model.forward(dummy_tokens)
# print("transformer out shape:", out.shape)   # (2, 64, 512)

# block = TransformerBlock(512, 8, 2048)
# dummy = np.random.randn(2, 16, 512).astype(np.float32)
# out = block.forward(dummy)
# print("block out shape:", out.shape)   # (2, 16, 512)
# q=k=v=np.random.randn(2,4,64).astype(np.float32)
# out= batched_attention(q,k,v)
# print("Batched output shape:", out.shape )


# x = np.random.randn(2, 4, 512).astype(np.float32)
# out = split_heads(x, 8)
# print("split shape:", out.shape)   # must be (2, 8, 4, 64)


# mha = MultiHeadAttention(512, 8)
# dummy = np.random.randn(2, 16, 512).astype(np.float32)
# out = mha.forward(dummy)
# print("multi-head out shape:", out.shape)   # (2, 16, 512)
# x = np.array([[1., 2., 3.]])
# assert softmax(x).round(2).tolist() == [[0.09, 0.24, 0.67]]

# print("warm-up ok")
