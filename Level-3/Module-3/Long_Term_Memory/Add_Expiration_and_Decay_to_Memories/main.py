import time


class LongTermMemory:
    def __init__(self):
        self.entries = []

    def add(self, content, ttl=30, created=None):
        self.entries.append({"content": content, "ttl": ttl, "created": created or time.time()})

    def cleanup_expired(self, now=None):
        now = now or time.time()
        self.entries[:] = [e for e in self.entries if now - e["created"] <= e["ttl"] * 86400]

    def decay_factor(self, age_days):
        return max(0.5, 1 - min(age_days, 50) / 100)


def main():
    m = LongTermMemory()
    m.add("recent", 30)
    m.add("expired", 1, time.time() - 2 * 86400)
    m.cleanup_expired()
    print(m.entries, m.decay_factor(10), m.decay_factor(100))


if __name__ == "__main__":
    main()
