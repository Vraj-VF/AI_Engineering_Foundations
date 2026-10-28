import json
import uuid


def read_json(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def transform(text, operation):
    operations = {
        "uppercase": str.upper,
        "lowercase": str.lower,
        "reverse": lambda value: value[::-1],
        "word_count": lambda value: len(value.split()),
    }
    if operation not in operations:
        raise ValueError("unsupported operation")
    return operations[operation](text)


def main():
    print(
        {
            "tools": ["read_json", "transform", "generate_uuid"],
            "sample_uuid": str(uuid.uuid4()),
            "sample": transform("MCP tools", "uppercase"),
        }
    )


if __name__ == "__main__":
    main()
