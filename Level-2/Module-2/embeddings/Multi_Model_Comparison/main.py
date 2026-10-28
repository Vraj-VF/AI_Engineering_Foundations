import math


def embed(text, model):
    values = [0, 0, 0, 0]
    for index, word in enumerate(text.lower().split()):
        values[index % 4] += (len(word) + len(model)) / 10
    return values


def cosine(left, right):
    numerator = sum(a * b for a, b in zip(left, right))
    denominator = math.sqrt(sum(a * a for a in left) * sum(b * b for b in right))
    return numerator / denominator if denominator else 0


def main():
    documents = ["cats and care", "dogs and care", "database indexing"]
    for model in ("text-embedding-3-small", "local-huggingface"):
        vectors = [embed(document, model) for document in documents]
        matrix = [[round(cosine(a, b), 3) for b in vectors] for a in vectors]
        print(model, matrix)
    print(
        "analysis: local models can change pair ranking because vector dimensions and weighting differ"
    )


if __name__ == "__main__":
    main()
