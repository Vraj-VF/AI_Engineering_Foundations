import json
import statistics


def percentile(values, fraction):
    values = sorted(values)
    return values[min(len(values) - 1, int(len(values) * fraction))]


def main():
    events = [
        {"quality": 0.8, "latency_ms": 100, "cost": 0.01, "alert": False},
        {"quality": 0.6, "latency_ms": 180, "cost": 0.02, "alert": True},
    ]
    with open("evaluation_events.json", "w", encoding="utf-8") as file:
        json.dump(events, file, indent=2)
    quality = [event["quality"] for event in events]
    latency = [event["latency_ms"] for event in events]
    print("quality_rolling_average:", statistics.mean(quality))
    print(
        "latency_p50:",
        percentile(latency, 0.5),
        "latency_p95:",
        percentile(latency, 0.95),
    )
    print("cost_trend:", sum(event["cost"] for event in events))
    print("alert_rate:", sum(event["alert"] for event in events) / len(events))
    print("alert_rules: quality < 0.7 or alert rate > 10 percent")
    print("data_flow: LLM API -> JSON events -> evaluator -> dashboard")


if __name__ == "__main__":
    main()
