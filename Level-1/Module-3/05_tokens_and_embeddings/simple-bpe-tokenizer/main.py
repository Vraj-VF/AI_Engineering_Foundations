def pair_counts(tokens):
    counts = {}
    for left, right in zip(tokens, tokens[1:]):
        counts[(left, right)] = counts.get((left, right), 0) + 1
    return counts


def merge(tokens, pair):
    result = []
    index = 0
    while index < len(tokens):
        if index + 1 < len(tokens) and (tokens[index], tokens[index + 1]) == pair:
            result.append(tokens[index] + tokens[index + 1])
            index += 2
        else:
            result.append(tokens[index])
            index += 1
    return result


def main():
    tokens = list(input("Word: "))
    counts = pair_counts(tokens)
    pair = max(counts, key=counts.get) if counts else ()
    print(merge(tokens, pair) if pair else tokens)


if __name__ == "__main__":
    main()
