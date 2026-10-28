def expand(query):
    synonyms = {"car": ["automobile", "vehicle"], "search": ["find", "retrieve"]}
    terms = query.lower().split()
    variations = [query]
    for term in terms:
        for synonym in synonyms.get(term, []):
            variations.append(query.replace(term, synonym))
    return variations[:5]


def rrf(result_lists):
    scores = {}
    for rows in result_lists:
        for rank, document in enumerate(rows, 1):
            scores[document] = scores.get(document, 0) + 1 / (60 + rank)
    return sorted(scores, key=scores.get, reverse=True)


def main():
    query = input("Query: ").strip() or "search car"
    variations = expand(query)
    lists = [
        [f"doc-{index}-{variation}" for index in range(3)] for variation in variations
    ]
    print("variations:", variations)
    print("ranked:", rrf(lists))


if __name__ == "__main__":
    main()
