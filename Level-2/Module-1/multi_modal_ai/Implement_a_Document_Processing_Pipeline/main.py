import json
import os
import time


def process_page(number, text):
    started = time.perf_counter()
    content_type = (
        "table" if "|" in text else "chart" if "figure" in text.lower() else "text"
    )
    return {
        "page": number,
        "content_type": content_type,
        "text": text[:200],
        "description": "Local description of " + content_type,
        "processing_seconds": round(time.perf_counter() - started, 6),
        "cost": 0.0,
    }


def main():
    path = input("PDF path (blank uses two local pages): ").strip()
    pages = []
    if path and os.path.exists(path):
        with open(path, "rb") as file:
            pages = [file.read().decode("utf-8", errors="ignore")]
    else:
        pages = ["Document title and paragraph.", "Figure 1 shows a trend."]
    report = [process_page(number, text) for number, text in enumerate(pages, 1)]
    result = {"pages": report, "summary": " ".join(page["text"] for page in report)}
    with open("document_report.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
