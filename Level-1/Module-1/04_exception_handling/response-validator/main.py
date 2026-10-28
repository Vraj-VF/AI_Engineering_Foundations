import json


def validate_response(text):
    errors = []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return ["Invalid JSON"]
    if not isinstance(data, dict):
        errors.append("Response must be an object")
    else:
        for key in ["id", "content"]:
            if key not in data:
                errors.append("Missing field: " + key)
        if "id" in data and not isinstance(data["id"], str):
            errors.append("id must be a string")
        if "content" in data and not isinstance(data["content"], str):
            errors.append("content must be a string")
    return errors


def main():
    errors = validate_response(input("JSON response: "))
    print("Valid response" if not errors else "\n".join(errors))


if __name__ == "__main__":
    main()
