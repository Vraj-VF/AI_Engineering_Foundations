import time


def classify(error):
    if isinstance(error, ValueError):
        return "validation"
    if isinstance(error, TimeoutError):
        return "transient"
    return "permanent"


def run(primary, fallback=None):
    for attempt in range(3):
        try:
            return primary()
        except Exception as error:
            if classify(error) != "transient":
                break
            time.sleep(0.01 * 2**attempt)
    return fallback() if fallback else None


def main():
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 3:
            raise TimeoutError("temporary")
        return "primary result"

    print(run(flaky, lambda: "fallback result"), "attempts", calls["count"])


if __name__ == "__main__":
    main()
