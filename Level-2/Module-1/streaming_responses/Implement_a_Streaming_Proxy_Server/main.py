import json
import time


STATS = {"requests": 0, "tokens": 0, "connections_dropped": 0}


def stream_sse(messages, provider):
    STATS["requests"] += 1
    response = f"{provider} local response: " + " ".join(messages)
    for token in response.split():
        STATS["tokens"] += 1
        yield "data: " + token + "\n\n"
        time.sleep(0.01)


def handle_request(messages, provider):
    try:
        return list(stream_sse(messages, provider))
    except GeneratorExit:
        STATS["connections_dropped"] += 1
        return []


def main():
    messages = [input("Message: ").strip() or "hello"]
    provider = input("Provider (openai/anthropic): ").strip() or "local"
    print("SSE stream:")
    print("".join(handle_request(messages, provider)), end="")
    print("/stats:", json.dumps(STATS))


if __name__ == "__main__":
    main()
