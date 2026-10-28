def detect(answer, context, threshold=0.6):
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())
    grounding = len(answer_words & context_words) / max(len(answer_words), 1)
    return {
        "grounding_score": round(grounding, 3),
        "threshold": threshold,
        "hallucination": grounding < threshold,
    }


def main():
    triples = [
        {
            "question": "Where?",
            "answer": "The service runs locally.",
            "context": "The service runs locally.",
        }
        for _ in range(10)
    ]
    report = [detect(row["answer"], row["context"]) for row in triples]
    print("triples:", len(report), "threshold:", report[0]["threshold"])
    print(
        "false_positive_tuning: adjust threshold and weights against labeled domain data"
    )
    print(report)


if __name__ == "__main__":
    main()
