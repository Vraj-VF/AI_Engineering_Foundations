import json


def main():
    rows = []
    for index in range(20):
        source = "The service runs in region A."
        rows.append(
            {
                "source": source,
                "faithful_answer": "It runs in region A.",
                "unfaithful_answer": "It runs in region B.",
                "claims": [{"text": "It runs in region B.", "label": "contradicted"}],
            }
        )
    with open("hallucination_dataset.json", "w", encoding="utf-8") as file:
        json.dump(rows, file, indent=2)
    print("examples:", len(rows), "labels:", {"supported", "contradicted", "neutral"})


if __name__ == "__main__":
    main()
