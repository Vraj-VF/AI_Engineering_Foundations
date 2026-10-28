import numpy as np


def cosine(left, right):
    return np.dot(left, right) / (np.linalg.norm(left) * np.linalg.norm(right))


def main():
    vectors = []
    for number in range(3):
        vectors.append(
            np.array(
                [float(value) for value in input(f"Vector {number + 1}: ").split()]
            )
        )
    for index, vector in enumerate(vectors):
        print(index, cosine(vectors[0], vector))


if __name__ == "__main__":
    main()
