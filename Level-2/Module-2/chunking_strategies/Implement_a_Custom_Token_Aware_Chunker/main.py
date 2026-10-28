def chunk_text(text, max_tokens):
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")

    chunks = []
    current = ""
    for word in text.split():
        candidate = word if not current else current + " " + word
        if len(candidate) > max_tokens * 4 and current:
            chunks.append(current)
            current = word
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def main():
    text = (
        input("Document text: ").strip()
        or "This local document demonstrates token-aware chunking. " * 30
    )
    for budget in (100, 256):
        chunks = chunk_text(text, budget)
        assert all((len(chunk) + 3) // 4 <= budget for chunk in chunks)
        print(
            "max_tokens:",
            budget,
            "chunks:",
            len(chunks),
            "estimated_tokens:",
            [(len(chunk) + 3) // 4 for chunk in chunks],
        )


if __name__ == "__main__":
    main()
