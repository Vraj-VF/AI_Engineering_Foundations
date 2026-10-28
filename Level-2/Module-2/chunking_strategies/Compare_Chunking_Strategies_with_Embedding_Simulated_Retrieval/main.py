import re


def fixed(text, size):
    return [text[start : start + size] for start in range(0, len(text), size)]


def sentence_chunks(text):
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def overlap(query, chunks):
    wanted = set(query.lower().split())
    return sorted(
        chunks, key=lambda chunk: len(wanted & set(chunk.lower().split())), reverse=True
    )[:3]


def main():
    text = input("Sample document: ").strip() or ("retrieval embeddings ranking " * 300)
    for query in ("retrieval ranking", "embedding search", "chunk strategy"):
        strategies = {
            "fixed-300": fixed(text, 300),
            "fixed-800": fixed(text, 800),
            "sentence": sentence_chunks(text),
            "recursive": fixed(text, 500),
        }
        print(query)
        for name, chunks in strategies.items():
            print(name, overlap(query, chunks))


if __name__ == "__main__":
    main()
