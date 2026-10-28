import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(1)
x = np.linspace(-3, 3, 50).reshape(-1, 1)
y = np.sin(x).ravel() + rng.normal(0, 0.3, len(x))
for degree in [1, 3, 5, 10, 20]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x, y)
    print(degree, mean_squared_error(y, model.predict(x)))
