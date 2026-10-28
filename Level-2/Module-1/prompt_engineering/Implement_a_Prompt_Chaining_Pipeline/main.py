import time


def call_step(label, action, temperature):
    started = time.perf_counter()
    try:
        value = action()
        return {
            "step": label,
            "temperature": temperature,
            "output": value,
            "latency_seconds": round(time.perf_counter() - started, 6),
            "error": None,
        }
    except Exception as error:
        return {
            "step": label,
            "temperature": temperature,
            "output": "",
            "error": str(error),
        }


def pipeline(topic):
    stages = [
        ("questions", lambda: [f"What is an important aspect of {topic}?"] * 10, 0.7),
        ("answers", lambda: [f"Local answer about {topic}"] * 10, 0.4),
        ("sections", lambda: [f"Section about {topic}"], 0.3),
        ("report", lambda: f"Final report about {topic}", 0.2),
    ]
    log = []
    for label, action, temperature in stages:
        result = call_step(label, action, temperature)
        log.append(result)
        if result["error"]:
            break
    return log


def main():
    topic = input("Research topic: ").strip() or "local retrieval"
    started = time.perf_counter()
    log = pipeline(topic)
    for item in log:
        print(
            item["step"], "temperature=", item["temperature"], "output=", item["output"]
        )
    print("pipeline_latency_seconds=", round(time.perf_counter() - started, 6))


if __name__ == "__main__":
    main()
