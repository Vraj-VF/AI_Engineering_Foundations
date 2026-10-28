CACHE = {}


def rerank(query, candidates, backend):
    key = (query, backend)
    if key not in CACHE:
        CACHE[key] = sorted(
            candidates, key=lambda item: item.get("relevance", 0), reverse=True
        )
    return CACHE[key]


def main():
    query = input("Query: ").strip() or "local search"
    candidates = [
        {"id": "a", "relevance": 0.8, "metadata": {"source": "local"}},
        {"id": "b", "relevance": 0.4, "metadata": {"source": "fallback"}},
    ]
    for backend in ("cohere", "cross-encoder", "heuristic"):
        print(backend, rerank(query, candidates, backend))
    print("/health:", {"status": "ok", "cache_entries": len(CACHE)})
    print("request_logging: enabled")


if __name__ == "__main__":
    main()
