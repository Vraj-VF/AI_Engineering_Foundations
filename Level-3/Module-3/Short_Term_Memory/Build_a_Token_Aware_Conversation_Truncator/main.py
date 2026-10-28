def truncate_messages(messages, max_tokens, model="local"):
    del model
    if not messages:
        return []
    system = next((message for message in messages if message.get("role") == "system"), None)
    latest_user = next(
        (message for message in reversed(messages) if message.get("role") == "user"),
        None,
    )
    required = []
    for message in (system, latest_user):
        if message is not None and message not in required:
            required.append(message)

    def token_count(message):
        return len(message.get("content", "").split())

    used = sum(token_count(message) for message in required)
    optional = [message for message in messages if message not in required]
    middle_first = optional[len(optional) // 2 :] + optional[: len(optional) // 2]
    kept = list(required)
    for message in middle_first:
        cost = token_count(message)
        if used + cost <= max_tokens:
            kept.append(message)
            used += cost
    return [message for message in messages if message in kept]


def test_truncator():
    assert truncate_messages([], 3) == []
    single = [{"role": "user", "content": "hello"}]
    assert truncate_messages(single, 1) == single
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "old user context"},
        {"role": "assistant", "content": "old assistant context"},
        {"role": "user", "content": "latest request"},
    ]
    result = truncate_messages(messages, 4)
    assert result[0]["role"] == "system"
    assert result[-1]["content"] == "latest request"
    assert len(result) <= 3


def main():
    test_truncator()
    messages = [
        {"role": "system", "content": "follow these rules"},
        {"role": "user", "content": "first request"},
        {"role": "assistant", "content": "first answer"},
        {"role": "user", "content": "latest request"},
    ]
    print(truncate_messages(messages, 5))


if __name__ == "__main__":
    main()
