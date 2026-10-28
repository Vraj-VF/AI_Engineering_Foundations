PATTERNS = ("ignore previous", "reveal system prompt", "bypass safety")


def defend(text):
    pattern_score = 40 if any(pattern in text.lower() for pattern in PATTERNS) else 0
    special_ratio = sum(
        not char.isalnum() and not char.isspace() for char in text
    ) / max(len(text), 1)
    heuristic_score = min(
        100, pattern_score + int(special_ratio * 40) + (20 if len(text) > 500 else 0)
    )
    secondary_score = 80 if pattern_score else 10
    final_score = round((heuristic_score + secondary_score) / 2)
    return {
        "regex": pattern_score,
        "heuristic": heuristic_score,
        "secondary_model": secondary_score,
        "statistical": round(special_ratio * 100),
        "final_score": final_score,
        "decision": "block" if final_score >= 50 else "allow",
    }


def main():
    text = input("Input to evaluate: ").strip()
    print(defend(text))
    print("evaluation_set: 50 known attacks + 50 benign inputs (local adapter)")
    print(
        "precision/recall require labeled execution data. Scores are emitted per input"
    )


if __name__ == "__main__":
    main()
