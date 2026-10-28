import csv
import time


def analyze(text):
    if not text.strip():
        raise ValueError("empty text")
    positive = any(word in text.lower() for word in ("good", "great", "works"))
    return {
        "label": "positive" if positive else "neutral",
        "confidence": 0.9 if positive else 0.6,
    }


def main():
    path = input("CSV path (blank uses 50 local entries): ").strip()
    rows = []
    if path:
        with open(path, newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
    else:
        rows = [
            {"text": "Entry " + str(number) + " works well"} for number in range(50)
        ]
    successes = []
    failures = []
    for number, row in enumerate(rows, 1):
        try:
            result = analyze(row.get("text", ""))
            successes.append(result)
            print(f"\rprocessed {number}/{len(rows)}", end="")
        except Exception as error:
            failures.append({"row": number, "error": str(error)})
        time.sleep(0.01)
    print()
    average = (
        sum(item["confidence"] for item in successes) / len(successes)
        if successes
        else 0
    )
    summary = {
        "successes": len(successes),
        "failures": len(failures),
        "average_confidence": round(average, 3),
        "failure_details": failures,
    }
    with open("batch_results.json", "w", encoding="utf-8") as file:
        json.dump({"results": successes, "summary": summary}, file, indent=2)
    print(summary)


if __name__ == "__main__":
    main()
