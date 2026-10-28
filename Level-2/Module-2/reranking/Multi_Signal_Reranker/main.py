def rerank(documents, weights):
    ranked = []
    for document in documents:
        score = (
            weights["cross_encoder"] * document["relevance"]
            + weights["recency"] * document["recency"]
            + weights["popularity"] * document["views"] / 1000
            + weights["authority"] * document["authority"]
        )
        ranked.append((round(score, 3), document))
    return sorted(ranked, reverse=True)


def main():
    documents = [
        {"id": "a", "relevance": 0.9, "recency": 0.6, "views": 500, "authority": 0.8},
        {"id": "b", "relevance": 0.7, "recency": 0.9, "views": 900, "authority": 0.5},
    ]
    for weights in (
        {"cross_encoder": 0.4, "recency": 0.2, "popularity": 0.2, "authority": 0.2},
        {"cross_encoder": 0.6, "recency": 0.1, "popularity": 0.1, "authority": 0.2},
    ):
        print(weights, rerank(documents, weights))


if __name__ == "__main__":
    main()
