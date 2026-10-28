import json
import time


def sentiment(text):
    positive = sum(
        word in ("good", "great", "helpful") for word in text.lower().split()
    )
    return {"label": "positive" if positive else "neutral", "confidence": 0.8}


def entities(text):
    return {"entities": [word for word in text.split() if word[:1].isupper()]}


def classify(text):
    return {"category": "support" if "help" in text.lower() else "general"}


def main():
    text = input("Text: ").strip()
    operations = [
        ("sentiment", sentiment),
        ("entities", entities),
        ("classification", classify),
    ]
    report = {
        "input": text,
        "model": "local-structured-adapter",
        "results": {},
        "token_count": len(text.split()),
        "latency_seconds": 0.0,
    }
    started = time.perf_counter()
    for name, operation in operations:
        value = operation(text)
        if not isinstance(value, dict):
            raise ValueError(name + " did not return an object")
        report["results"][name] = value
    report["latency_seconds"] = round(time.perf_counter() - started, 6)
    with open("validated_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
    with open("validated_report.txt", "w", encoding="utf-8") as file:
        file.write(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
