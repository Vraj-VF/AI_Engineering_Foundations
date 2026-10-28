import json
import os


CRITERIA = ("relevance", "evidence", "conciseness")


def heuristic(text):
    words = text.split()
    return {
        "relevance": min(10, max(1, len(words))),
        "evidence": 8 if "source" in text.lower() or "http" in text.lower() else 3,
        "conciseness": max(1, 10 - len(words) / 10),
    }


def validate_scores(scores):
    if any(key not in scores for key in CRITERIA):
        raise ValueError("missing criterion")
    values = {key: float(scores[key]) for key in CRITERIA}
    if any(value < 1 or value > 10 for value in values.values()):
        raise ValueError("scores must be between 1 and 10")
    return values


def llm_scores(text):
    if not os.getenv("OPENAI_API_KEY"):
        return heuristic(text), 0, "local fallback"
    try:
        from openai import OpenAI

        response = OpenAI(timeout=10, max_retries=2).chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Return JSON with numeric 1-10 scores for relevance, evidence, "
                        "and conciseness. Text: " + text
                    ),
                }
            ],
        )
        scores = validate_scores(json.loads(response.choices[0].message.content))
        tokens = response.usage.total_tokens if response.usage else 0
        return scores, tokens, "openai"
    except (ValueError, KeyError, TypeError, json.JSONDecodeError):
        return heuristic(text), 0, "invalid JSON or score fallback"
    except Exception as error:
        return heuristic(text), 0, "provider fallback: " + str(error)


def correlation(left, right):
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    left_spread = sum((a - left_mean) ** 2 for a in left)
    right_spread = sum((b - right_mean) ** 2 for b in right)
    denominator = (left_spread * right_spread) ** 0.5
    return numerator / denominator if denominator else 0.0


def main():
    texts = [
        "A concise answer with source https://example.test",
        "A long answer without evidence " * 5,
        "A useful explanation with a source",
    ]
    heuristic_values = []
    llm_values = []
    token_cost = 0
    for text in texts:
        baseline = heuristic(text)
        evaluated, tokens, mode = llm_scores(text)
        heuristic_values.append(sum(baseline.values()) / 3)
        llm_values.append(sum(evaluated.values()) / 3)
        token_cost += tokens
        print(json.dumps({"mode": mode, "heuristic": baseline, "llm": evaluated, "tokens": tokens}))
    print(
        {
            "correlation": round(correlation(heuristic_values, llm_values), 3),
            "total_tokens": token_cost,
            "estimated_cost": token_cost * 0.000001,
        }
    )


if __name__ == "__main__":
    main()
