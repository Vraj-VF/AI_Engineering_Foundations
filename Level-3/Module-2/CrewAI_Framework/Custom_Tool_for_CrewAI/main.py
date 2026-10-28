from pathlib import Path


def summarize_file(path):
    text = Path(path).read_text(encoding="utf-8")
    return " ".join(text.split()[:30])


def main():
    path = Path("context.txt")
    path.write_text("Local context for the researcher.", encoding="utf-8")
    print(summarize_file(path))


if __name__ == "__main__":
    main()
