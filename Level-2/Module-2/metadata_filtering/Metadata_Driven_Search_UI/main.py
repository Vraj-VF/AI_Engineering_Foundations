import json


DOCUMENTS = [
    {
        "category": "guide",
        "date": "2025-01-10",
        "access": "public",
        "text": "search guide",
    },
    {
        "category": "api",
        "date": "2025-02-10",
        "access": "private",
        "text": "api reference",
    },
]


def facets():
    result = {}
    for field in ("category", "date", "access"):
        result[field] = {}
        for document in DOCUMENTS:
            value = document[field]
            result[field][value] = result[field].get(value, 0) + 1
    return result


def main():
    preset = {"category": "guide", "access": "public"}
    with open("search_preset.json", "w", encoding="utf-8") as file:
        json.dump(preset, file, indent=2)
    print("facets:", facets())
    query = input("Query (blank uses search): ").strip() or "search"
    active = {key: value for key, value in preset.items() if value}
    rows = [item for item in DOCUMENTS if query in item["text"] or query == "search"]
    rows = [
        item
        for item in rows
        if all(item[key] == value for key, value in active.items())
    ]
    print("query:", query, "active_filters:", active, "results:", rows)


if __name__ == "__main__":
    main()
