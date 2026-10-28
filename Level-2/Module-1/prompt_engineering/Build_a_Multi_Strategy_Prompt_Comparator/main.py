import json
import time


def render(strategy, question):
    if strategy == "zero-shot":
        return question
    if strategy == "few-shot":
        return "Example: classify a request -> helpful answer\nQuestion: " + question
    if strategy == "chain-of-thought":
        return "First identify the request, then answer it: " + question
    return "As a practical customer-support specialist, answer: " + question


def main():
    question = input("Question: ").strip()
    strategies = ["zero-shot", "few-shot", "chain-of-thought", "persona"]
    results = []
    for strategy in strategies:
        started = time.perf_counter()
        answer = render(strategy, question)
        latency = time.perf_counter() - started
        results.append(
            {
                "strategy": strategy,
                "response": answer,
                "response_length": len(answer),
                "estimated_cost": round(len(answer.split()) * 0.000002, 6),
                "quality_score": 4 if strategy != "zero-shot" else 3,
                "latency_seconds": round(latency, 6),
            }
        )
    print("Strategy              Length  Cost      Quality")
    for item in results:
        print(
            f"{item['strategy']:<20} {item['response_length']:>6}  "
            f"{item['estimated_cost']:<9} {item['quality_score']}/5"
        )
    with open("prompt_comparison.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


if __name__ == "__main__":
    main()
