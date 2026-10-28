def quality(category, question, round_number):
    category_bonus = {"factual": 0.06, "creative": 0.03, "analytical": 0.05, "mathematical": 0.04}
    return min(
        1.0,
        0.45
        + category_bonus[category]
        + round_number * 0.08
        - max(0, round_number - 3) * 0.02
        + len(question) * 0.0001,
    )


def main():
    categories = {
        "factual": ["Who wrote Hamlet? " + str(i) for i in range(5)],
        "creative": ["Write a slogan. " + str(i) for i in range(5)],
        "analytical": ["Compare designs. " + str(i) for i in range(5)],
        "mathematical": ["Solve 2 + 2. " + str(i) for i in range(5)],
    }
    all_results = {}
    for category, questions in categories.items():
        results = []
        for question in questions:
            scores = [quality(category, question, round_number) for round_number in range(1, 6)]
            results.append(scores)
        average_by_round = [
            round(sum(scores[round_number] for scores in results) / len(results), 3)
            for round_number in range(5)
        ]
        improvement = [round(average_by_round[i] - average_by_round[0], 3) for i in range(5)]
        optimal = average_by_round.index(max(average_by_round)) + 1
        all_results[category] = {
            "per_round_improvement": improvement,
            "average_by_round": average_by_round,
            "optimal_round": optimal,
            "extra_api_calls": optimal * len(questions),
        }
    print("category | average scores by round | optimal round | cost calls")
    for category, result in all_results.items():
        print(category, result)
    print("cost-benefit: compare each extra round's quality improvement with five API calls.")


if __name__ == "__main__":
    main()
