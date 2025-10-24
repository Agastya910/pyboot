import numpy as np


def softmax_grad(x: np.ndarray) -> np.ndarray:
    """
    Vectorized Jacobian of softmax.
    Input: logits shape (N,)
    Returns: Jacobian shape (N,N) where J[i,j] = ∂softmax_i/ ∂x_j
    """
    s = np.exp(x - x.mean())
    p = s / s.sum()
    return np.diag(p) - np.outer(p, p)


if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])
    J = softmax_grad(x)
    print("Jacobian shape:", J.shape)
    print("Rows sums (should be 0):", J.sum(axis=1))
