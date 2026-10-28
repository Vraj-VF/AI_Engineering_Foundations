def preprocess(text):
    stop_words = {"the", "a", "an", "is", "to", "of", "and", "in", "on", "for"}
    punctuation = ".,!?;:-()[]{}\"'"
    tokens = []
    for word in text.lower().split():
        word = word.strip(punctuation)
        if word and word not in stop_words:
            tokens.append(word)
    return tokens


def main():
    for number in range(1, 4):
        print(preprocess(input(f"Paragraph {number}: ")))


if __name__ == "__main__":
    main()
