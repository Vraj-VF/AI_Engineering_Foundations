import os


def summarize(messages):
    text = " ".join((message["content"] for message in messages))
    if not os.getenv("OPENAI_API_KEY"):
        return "Extractive summary: " + " ".join(text.split()[:20])
    try:
        from openai import OpenAI

        result = OpenAI(timeout=10).chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Summarize in 1-2 sentences, preserving key facts and decisions: " + text
                    ),
                }
            ],
        )
        return result.choices[0].message.content
    except Exception:
        return "Fallback summary: " + " ".join(text.split()[:20])


def main():
    print(
        summarize(
            [
                {"role": "user", "content": f"Turn {i}: discussed project decisions"}
                for i in range(8)
            ]
        )
    )


if __name__ == "__main__":
    main()
