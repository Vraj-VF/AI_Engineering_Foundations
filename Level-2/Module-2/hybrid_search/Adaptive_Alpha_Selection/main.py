import re


def choose_alpha(query):
    if re.search(r"\b[A-Z]{2,}-?\d+\b", query):
        return 0.9
    if '"' in query:
        return 0.8
    if query.lower().startswith(("what", "how", "why")):
        return 0.5
    if len(query.split()) > 6:
        return 0.6
    return 0.7


def main():
    queries = [
        "API-42 failure",
        '"exact phrase" search',
        "What is retrieval?",
        "find a short document",
        "why did the service fail",
    ] * 2
    for query in queries:
        alpha = choose_alpha(query)
        adaptive = 1 - abs(alpha - 0.7)
        fixed = 0.3
        print(
            query, "alpha=", alpha, "adaptive=", round(adaptive, 2), "fixed_0.7=", fixed
        )


if __name__ == "__main__":
    main()
