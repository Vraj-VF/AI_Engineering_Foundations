def clean_words(text):
    punctuation = ".,!?;:-()[]{}\"'"
    return [
        word.strip(punctuation).lower()
        for word in text.split()
        if word.strip(punctuation)
    ]


def main():
    filename = input("Text filename: ")
    try:
        with open(filename, encoding="utf-8") as file:
            words = clean_words(file.read())
    except OSError as error:
        print("Could not read file:", error)
        return
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    average = sum(len(word) for word in words) / len(words) if words else 0
    richness = len(set(words)) / len(words) if words else 0
    print("Top words:")
    remaining = counts.copy()
    for _ in range(10):
        if not remaining:
            break
        word = max(remaining, key=remaining.get)
        count = remaining.pop(word)
        print(f"{word}: {count}")
    print(f"Average word length: {average:.2f}")
    print(f"Vocabulary richness: {richness:.2f}")


if __name__ == "__main__":
    main()
