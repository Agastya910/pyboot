from collections import deque


def rolling_mean(values, k: int):
    window = deque(maxlen=k)
    for v in values:
        window.append(float(v))
        if len(window) == k:
            yield sum(window) / k


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    for rm in rolling_mean(data, 3):
        print(rm)
