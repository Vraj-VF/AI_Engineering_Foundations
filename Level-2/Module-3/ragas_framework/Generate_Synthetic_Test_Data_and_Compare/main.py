def score(sample):
    return len(set(sample["answer"].split()) & set(sample["context"].split())) / max(
        len(sample["answer"].split()), 1
    )


def main():
    documents = ["local retrieval improves answers", "metadata filters isolate tenants"]
    synthetic = [
        {"question": "What does this say?", "answer": document, "context": document}
        for document in (documents * 10)
    ]
    manual = [
        {
            "question": "What does this say?",
            "answer": "local answer",
            "context": document,
        }
        for document in (documents * 10)
    ]
    print("synthetic_samples:", len(synthetic), "manual_samples:", len(manual))
    print("synthetic_mean:", sum(score(row) for row in synthetic) / len(synthetic))
    print("manual_mean:", sum(score(row) for row in manual) / len(manual))


if __name__ == "__main__":
    main()
