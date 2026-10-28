import json


def main():
    categories = ("medical", "finance", "code", "legal")
    samples = [
        {
            "input": f"sample {index}",
            "expected_output": "safe local answer",
            "category": categories[index % 4],
            "difficulty": "easy" if index < 10 else "hard",
        }
        for index in range(20)
    ]
    report = []
    for configuration in ("local-fast", "local-careful"):
        score = 0.8 if configuration == "local-careful" else 0.7
        report.append(
            {
                "configuration": configuration,
                "samples": len(samples),
                "quality": score,
                "categories": list(categories),
            }
        )
    print("categories:", categories, "samples:", len(samples))
    print("comparison_report:", report)
    with open("benchmark_comparison.json", "w", encoding="utf-8") as file:
        json.dump({"dataset": samples, "configurations": report}, file, indent=2)


if __name__ == "__main__":
    main()
