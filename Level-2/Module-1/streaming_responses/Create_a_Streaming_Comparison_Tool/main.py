import json
import time


def measure(provider, prompt):
    started = time.perf_counter()
    tokens = (provider + " response " + prompt).split()
    first_token = time.perf_counter() - started
    for token in tokens:
        print(f"{provider:<9}: {token}")
    total = time.perf_counter() - started
    return {
        "provider": provider,
        "time_to_first_token": round(first_token, 6),
        "total_seconds": round(total, 6),
        "token_count": len(tokens),
        "tokens_per_second": round(len(tokens) / max(total, 0.000001), 2),
    }


def main():
    prompts = [input("Prompt 1: ").strip() or "Explain caching"]
    prompts.extend(["Explain streaming"] * 4)
    report = []
    for prompt in prompts:
        for provider in ("openai", "anthropic"):
            report.append(measure(provider, prompt))
    with open("stream_comparison.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
