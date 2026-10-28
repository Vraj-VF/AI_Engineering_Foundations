import json


def main():
    samples = [
        {
            "question": f"What is policy item {index}?",
            "ground_truth": "Use the documented policy.",
            "contexts": ["The documented policy applies locally."],
        }
        for index in range(10)
    ]
    with open("evaluation_dataset.json", "w", encoding="utf-8") as file:
        json.dump(samples, file, indent=2)
    with open("evaluation_dataset.json", encoding="utf-8") as file:
        loaded = json.load(file)
    print(
        "samples:",
        len(loaded),
        "schema_verified:",
        all({"question", "ground_truth", "contexts"} <= set(row) for row in loaded),
    )


if __name__ == "__main__":
    main()
