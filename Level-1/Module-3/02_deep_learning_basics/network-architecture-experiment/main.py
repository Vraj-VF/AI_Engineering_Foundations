import numpy as np

rng = np.random.default_rng(5)
x = rng.normal(size=(100, 2))
y = (x[:, 0] + x[:, 1] > 0).astype(int)
for hidden in [2, 4, 8]:
    weights = rng.normal(0, 0.2, (2, hidden))
    hidden_values = np.tanh(x @ weights)
    output = hidden_values.mean(axis=1) > 0
    print(f"hidden units {hidden}: accuracy {np.mean(output == y):.2f}")
