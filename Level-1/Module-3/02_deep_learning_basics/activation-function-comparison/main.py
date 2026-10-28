import numpy as np

values = np.linspace(-3, 3, 7)
print("sigmoid", 1 / (1 + np.exp(-values)))
print("tanh", np.tanh(values))
print("relu", np.maximum(values, 0))
print("Compare saturation and gradient behavior for each activation.")
