def score(query, text):
    return len(set(query.lower().split()) & set(text.lower().split()))


def search(query, records, weights):
    ranked = []
    for record in records:
        total = weights["title"] * score(query, record["title"])
        total += weights["content"] * score(query, record["content"])
        total += weights["tags"] * score(query, " ".join(record["tags"]))
        ranked.append((total, record))
    return sorted(ranked, reverse=True, key=lambda item: item[0])


def main():
    records = [
        {"title": "Python search", "content": "retrieval systems", "tags": ["code"]},
        {"title": "Cooking", "content": "Python recipes", "tags": ["food"]},
    ]
    query = input("Query: ").strip() or "Python"
    for weights in (
        {"title": 0.5, "content": 0.3, "tags": 0.2},
        {"title": 0.2, "content": 0.6, "tags": 0.2},
    ):
        print(weights, search(query, records, weights))


if __name__ == "__main__":
    main()
