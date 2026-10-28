import math


words = [
    "The",
    "programmer",
    "told",
    "the",
    "designer",
    "that",
    "she",
    "needed",
    "to",
    "fix",
    "the",
    "bug",
]

embeddings = {
    "The": [0, 0, 0, 0, 0, 1],
    "the": [0, 0, 0, 0, 0, 1],
    "programmer": [1, 0.1, 0, 1, 0, 0],
    "told": [0, 0, 0, 0, 1, 0],
    "designer": [1, 1, 0.5, 0, 0, 0],
    "that": [0, 0, 0, 0, 0, 1],
    "she": [1, 1, 0.2, 0, 0, 0],
    "needed": [0, 0, 0, 0, 1, 0],
    "to": [0, 0, 0, 0, 0, 1],
    "fix": [0, 0, 0, 1, 1, 0],
    "bug": [0, 0, 0, 1, 0, 0],
}


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def attention_matrix(values):
    scale = math.sqrt(len(values[0]))
    matrix = []
    for query in values:
        scores = [dot(query, key) / scale for key in values]
        exponentials = [math.exp(score) for score in scores]
        total = sum(exponentials)
        matrix.append([value / total for value in exponentials])
    return matrix


def print_table(matrix):
    print(" " * 12 + " ".join(f"{word:>10}" for word in words))
    for word, row in zip(words, matrix):
        values = " ".join(f"{value:10.3f}" for value in row)
        print(f"{word:>12} {values}")


def main():
    values = [[component * 2.5 for component in embeddings[word]] for word in words]
    matrix = attention_matrix(values)
    print_table(matrix)

    pronoun_index = words.index("she")
    ranked = sorted(
        zip(words, matrix[pronoun_index]),
        key=lambda item: item[1],
        reverse=True,
    )
    print("\n'she' attention ranking:")
    for word, weight in ranked[:5]:
        print(f"{word:>12} {weight:.3f}")

    print(
        "\nThe pronoun she attends most strongly to designer because both vectors "
        "share person, female, and design-role dimensions."
    )
    print("It also attends strongly to itself because a vector matches itself.")
    print("Programmer receives less attention because its female component is small.")
    print("Function words such as the, that, and to have little semantic overlap.")
    print("The verbs needed and told describe actions but do not identify the person.")
    print(
        "This example deliberately encodes gender, so it is not evidence that the "
        "real sentence has an unambiguous reference."
    )
    print(
        "A learned model would discover useful relationships through learned "
        "query and key projections."
    )


if __name__ == "__main__":
    main()
