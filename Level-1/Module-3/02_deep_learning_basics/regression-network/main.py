import numpy as np

rng = np.random.default_rng(4)
x = np.linspace(-3, 3, 200).reshape(-1, 1)
y = np.sin(x) + rng.normal(0, 0.1, x.shape)
weights = np.zeros((1, 1))
bias = np.zeros((1, 1))
for _ in range(500):
    prediction = x @ weights + bias
    error = prediction - y
    weights -= 0.01 * x.T @ error / len(x)
    bias -= 0.01 * error.mean(axis=0)
print("MSE:", np.mean((x @ weights + bias - y) ** 2))
