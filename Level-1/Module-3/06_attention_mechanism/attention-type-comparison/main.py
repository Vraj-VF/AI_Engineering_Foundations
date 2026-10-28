import math


def softmax(scores):
    exponentials = [math.exp(score) for score in scores]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def attention(queries, keys, causal=False):
    scale = math.sqrt(len(queries[0]))
    matrix = []
    for row_number, query in enumerate(queries):
        scores = []
        for column_number, key in enumerate(keys):
            if causal and column_number > row_number:
                scores.append(float("-inf"))
            else:
                scores.append(sum(a * b for a, b in zip(query, key)) / scale)
        finite_scores = [score for score in scores if score != float("-inf")]
        weights = softmax(finite_scores)
        result = []
        weight_index = 0
        for score in scores:
            if score == float("-inf"):
                result.append(0.0)
            else:
                result.append(weights[weight_index])
                weight_index += 1
        matrix.append(result)
    return matrix


def matrix_lines(title, rows, columns, matrix):
    lines = [
        title,
        " " * 12 + " ".join(f"{word:>10}" for word in columns),
    ]
    for word, values in zip(rows, matrix):
        lines.append(f"{word:>12} " + " ".join(f"{value:10.3f}" for value in values))
    return lines


def print_side_by_side(blocks):
    width = max(len(line) for block in blocks for line in block)
    height = max(len(block) for block in blocks)
    for row_number in range(height):
        pieces = []
        for block in blocks:
            pieces.append(block[row_number] if row_number < len(block) else "")
        print((" " * 4).join(piece.ljust(width) for piece in pieces))


def main():
    self_words = ["The", "weather", "is", "beautiful", "today"]
    english = ["The", "cat"]
    french = ["Le", "chat"]
    causal_words = ["I", "am", "learning", "about", "attention"]

    self_vectors = [[1, 0], [0, 1], [1, 1], [0, 2], [2, 0]]
    english_vectors = [[1, 0], [0, 1]]
    french_vectors = [[1, 0], [0, 1]]
    causal_vectors = [[1, 0], [1, 1], [0, 1], [0, 2], [2, 0]]

    self_matrix = attention(self_vectors, self_vectors)
    cross_matrix = attention(french_vectors, english_vectors)
    causal_matrix = attention(causal_vectors, causal_vectors, causal=True)

    print_side_by_side(
        [
            matrix_lines("SELF-attention", self_words, self_words, self_matrix),
            matrix_lines(
                "CROSS-attention (French queries, English keys)",
                french,
                english,
                cross_matrix,
            ),
            matrix_lines(
                "CAUSAL attention",
                causal_words,
                causal_words,
                causal_matrix,
            ),
        ]
    )

    print(
        "\nSelf-attention lets every token use the other tokens in its input sequence."
    )
    print("Cross-attention uses French queries to consult English keys and values.")
    print("Its matrix is rectangular when the source and query lengths differ.")
    print("Causal attention masks future tokens, so each row can only see its prefix.")
    print(
        "The formula is the same, while the source of queries, keys, and values changes."
    )
    print(
        "Self-attention is useful for encoders, cross-attention for translation, "
        "and causal attention for generation."
    )
    print(
        "These hand-built vectors illustrate the shapes; trained projections produce "
        "the useful linguistic patterns in a real model."
    )


if __name__ == "__main__":
    main()
