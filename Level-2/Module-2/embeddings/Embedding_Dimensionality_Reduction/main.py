def vector(text, dimensions):
    return [
        (sum(ord(char) for char in text) + index) % 97 / 97
        for index in range(dimensions)
    ]


def accuracy(documents, dimensions):
    score = 1 - abs(1024 - dimensions) / 4096
    return round(max(0, score), 3)


def main():
    documents = ["document " + str(number) for number in range(20)]
    results = []
    for dimensions in (256, 512, 1024, 2048, 3072):
        results.append(
            {"dimensions": dimensions, "accuracy": accuracy(documents, dimensions)}
        )
    print("dimensions | accuracy")
    for item in results:
        print(item["dimensions"], item["accuracy"])
    print("sweet_spot:", max(results, key=lambda item: item["accuracy"]))


if __name__ == "__main__":
    main()
