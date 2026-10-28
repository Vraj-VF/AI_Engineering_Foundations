import re


def sections(markdown):
    found = re.split(r"(?m)^(?=#+ )", markdown)
    result = []
    for part in found:
        lines = part.strip().splitlines()
        if not lines:
            continue
        header = lines[0].lstrip("# ").strip()
        text = " ".join(lines[1:]).strip()
        sentence = re.split(r"(?<=[.!?])\s+", text)[0] if text else ""
        result.append(
            {"header": header, "word_count": len(text.split()), "summary": sentence}
        )
    return result


def main():
    path = input("Markdown path (blank uses sample): ").strip()
    text = (
        open(path, encoding="utf-8").read()
        if path
        else "# One\nFirst section.\n## Two\nSecond section.\n## Three\nThird section.\n## Four\nFourth section."
    )
    for section in sections(text):
        print(section)


if __name__ == "__main__":
    main()
