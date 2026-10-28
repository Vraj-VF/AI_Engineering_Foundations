class ConversationMemory:
    PRIORITY = {"low": 0, "normal": 1, "high": 2}

    def __init__(self, limit=5):
        self.limit = limit
        self.messages = []
        self.evicted = []

    def add(self, text, priority="normal"):
        if priority not in self.PRIORITY:
            raise ValueError("priority must be low, normal, or high")
        self.messages.append({"text": text, "priority": priority})
        while len(self.messages) > self.limit:
            index = min(
                range(len(self.messages)),
                key=lambda position: self.PRIORITY[self.messages[position]["priority"]],
            )
            self.evicted.append(self.messages.pop(index))


def test_eviction_order():
    memory = ConversationMemory(limit=3)
    memory.add("high message", "high")
    memory.add("normal message", "normal")
    memory.add("low message", "low")
    memory.add("new normal", "normal")
    memory.add("new high", "high")
    memory.add("last high", "high")
    assert memory.evicted[0]["priority"] == "low"
    assert memory.evicted[1]["priority"] == "normal"
    assert all(message["priority"] == "high" for message in memory.messages)


def main():
    test_eviction_order()
    memory = ConversationMemory(limit=5)
    priorities = ("high", "low", "normal", "low", "high", "normal", "low", "normal", "high", "low")
    for number, priority in enumerate(priorities):
        memory.add("message " + str(number), priority)
    print({"remaining": memory.messages, "evicted_in_order": memory.evicted})


if __name__ == "__main__":
    main()
