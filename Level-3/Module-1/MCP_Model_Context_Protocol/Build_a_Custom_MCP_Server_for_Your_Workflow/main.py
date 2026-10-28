import json
from pathlib import Path


def list_files(folder):
    return [path.name for path in Path(folder).glob("*") if path.is_file()]


def search_text(folder, term):
    return [
        str(path)
        for path in Path(folder).glob("**/*")
        if path.is_file() and term.lower() in path.read_text(errors="ignore").lower()
    ]


def summarize_file(path):
    text = Path(path).read_text(encoding="utf-8")
    return {"lines": len(text.splitlines()), "words": len(text.split()), "preview": text[:120]}


def main():
    print(
        json.dumps(
            {
                "tools": ["list_files", "search_text", "summarize_file"],
                "resource": "workspace metadata",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
