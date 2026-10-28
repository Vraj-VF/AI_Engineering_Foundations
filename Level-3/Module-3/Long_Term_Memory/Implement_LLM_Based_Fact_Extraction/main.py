import json
import os


def extract_facts(message):
    if not os.getenv("OPENAI_API_KEY"):
        return [{"content": message, "category": "statement", "confidence": 0.6}]
    try:
        from openai import OpenAI

        result = OpenAI(timeout=10).chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": "Extract facts as JSON list with content, category, confidence: "
                    + message,
                }
            ],
        )
        return json.loads(result.choices[0].message.content).get("facts", [])
    except Exception:
        return [{"content": message, "category": "statement", "confidence": 0.5}]


def main():
    for message in (
        "My name is Alice",
        "I work in finance",
        "I enjoy hiking",
        "I live in Paris",
        "Python is my favorite language",
    ):
        print(extract_facts(message))


if __name__ == "__main__":
    main()
