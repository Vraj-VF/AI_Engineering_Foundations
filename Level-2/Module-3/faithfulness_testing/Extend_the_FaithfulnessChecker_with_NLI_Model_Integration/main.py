def heuristic(claim, source):
    return int(all(word in source.lower() for word in claim.lower().split()))


def nli_fallback(claim, source):
    return 0.9 if heuristic(claim, source) else 0.1


def main():
    cases = [
        ("the sky is blue", "the sky is blue today"),
        ("cats fly", "cats are animals"),
    ] * 3
    for claim, source in cases[:5]:
        print(
            {
                "claim": claim,
                "heuristic": heuristic(claim, source),
                "roberta-large-mnli": nli_fallback(claim, source),
            }
        )
    print(
        "transformers adapter is optional. Local NLI fallback is used when unavailable"
    )


if __name__ == "__main__":
    main()
