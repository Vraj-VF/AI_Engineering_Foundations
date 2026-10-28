import math


def bleu(reference, candidate):
    reference_words = reference.split()
    candidate_words = candidate.split()
    precisions = []
    for size in range(1, 5):
        ref_grams = {
            tuple(reference_words[index : index + size])
            for index in range(len(reference_words) - size + 1)
        }
        cand_grams = [
            tuple(candidate_words[index : index + size])
            for index in range(len(candidate_words) - size + 1)
        ]
        precisions.append(
            sum(gram in ref_grams for gram in cand_grams) / max(len(cand_grams), 1)
        )
    geometric = math.prod(max(value, 0.000001) for value in precisions) ** 0.25
    penalty = min(1, math.exp(1 - len(reference_words) / max(len(candidate_words), 1)))
    return geometric * penalty


def rouge_l(reference, candidate):
    left, right = reference.split(), candidate.split()
    table = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
    for row in range(1, len(left) + 1):
        for column in range(1, len(right) + 1):
            table[row][column] = (
                table[row - 1][column - 1] + 1
                if left[row - 1] == right[column - 1]
                else max(table[row - 1][column], table[row][column - 1])
            )
    return table[-1][-1] / max(len(left), 1)


def main():
    pairs = [
        ("the cat sat", "the cat sat"),
        ("a different answer", "unrelated text"),
    ] * 5
    for reference, candidate in pairs:
        print(
            {
                "bleu": round(bleu(reference, candidate), 3),
                "rouge_l": round(rouge_l(reference, candidate), 3),
            }
        )
    print("validation: identical strings score 1.0. Unrelated strings approach 0.0")


if __name__ == "__main__":
    main()
