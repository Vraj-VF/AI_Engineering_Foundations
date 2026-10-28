def load_text(value):
    return value


def clean_text(value):
    return value.lower().strip()


def tokenize(value):
    return value.split()


def count_frequency(values):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def pipeline(value, functions):
    for function in functions:
        value = function(value)
    return value


def main():
    result = pipeline(
        input("Text: "), [load_text, clean_text, tokenize, count_frequency]
    )
    print(result)


if __name__ == "__main__":
    main()
