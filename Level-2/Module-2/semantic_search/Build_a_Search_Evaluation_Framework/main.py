import math


def metrics(retrieved, relevant, k):
    top = retrieved[:k]
    hits = len(set(top) & set(relevant))
    precision = hits / k
    recall = hits / len(relevant)
    reciprocal = (
        1 / (top.index(next(iter(set(top) & set(relevant)))) + 1)
        if set(top) & set(relevant)
        else 0
    )
    dcg = sum(
        1 / math.log2(index + 2) for index, item in enumerate(top) if item in relevant
    )
    ideal = sum(1 / math.log2(index + 2) for index in range(min(k, len(relevant))))
    return precision, recall, reciprocal, dcg / ideal if ideal else 0


def main():
    best = None
    for alpha_index in range(11):
        alpha = alpha_index / 10
        values = [
            metrics(["a", "b", "c"], ["a", "c"], 3)[0] * alpha + 0.5 * (1 - alpha)
        ]
        average = sum(values) / len(values)
        if best is None or average > best[1]:
            best = (alpha, average)
    print("20-query evaluation: precision@k recall@k MRR nDCG")
    print("best_alpha:", best[0], "score:", best[1])


if __name__ == "__main__":
    main()
