from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = load_iris()
train_x, test_x, train_y, test_y = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target
)
for model in [
    LogisticRegression(max_iter=500),
    KNeighborsClassifier(n_neighbors=5),
    SVC(),
]:
    model.fit(train_x, train_y)
    print(type(model).__name__, accuracy_score(test_y, model.predict(test_x)))
