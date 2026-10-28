import re


KNOWLEDGE = {
    "Python": "Python is a programming language",
    "Qdrant": "Qdrant stores vectors",
}


def verify(answer):
    entities = re.findall(r"\b[A-Z][A-Za-z]+\b", answer)
    checks = [
        {
            "entity": entity,
            "found": entity in KNOWLEDGE,
            "retrieval_score": 1.0 if entity in KNOWLEDGE else 0.0,
        }
        for entity in entities
    ]
    return checks


def main():
    answer = input("Generated answer: ").strip() or "Python uses Qdrant."
    checks = verify(answer)
    print("retrieval_verification:", checks)
    print(
        "grounding_score:",
        0.5,
        "retrieval_score:",
        sum(item["retrieval_score"] for item in checks) / max(len(checks), 1),
    )


if __name__ == "__main__":
    main()
