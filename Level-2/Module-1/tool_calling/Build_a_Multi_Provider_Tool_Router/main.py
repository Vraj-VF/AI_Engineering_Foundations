import json
import time


TOOLS = ["weather", "calculator", "search", "calendar"]


def select_tool(query):
    text = query.lower()
    if "weather" in text:
        return "weather"
    if any(symbol in text for symbol in ("+", "-", "*", "/")):
        return "calculator"
    if "schedule" in text or "calendar" in text:
        return "calendar"
    return "search"


def provider_for(query):
    return "anthropic" if len(query.split()) > 8 else "openai"


def main():
    queries = [
        "weather in Paris",
        "calculate 2 + 2",
        "search local policy",
        "schedule a meeting tomorrow",
        "find a short answer",
    ] * 2
    report = []
    for query in queries:
        started = time.perf_counter()
        tool = select_tool(query)
        provider = provider_for(query)
        report.append(
            {
                "query": query,
                "provider": provider,
                "reason": "length heuristic",
                "tool": tool,
                "latency": round(time.perf_counter() - started, 6),
                "quality": 4,
            }
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
