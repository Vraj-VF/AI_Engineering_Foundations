import math


class Memory:
    def __init__(self):
        self.entries = []

    def add(self, text, when):
        self.entries.append({"text": text, "when": when})

    def deduplicate(self):
        unique = []
        for item in self.entries:
            words = set(item["text"].lower().split())
            duplicate = None
            for old in unique:
                old_words = set(old["text"].lower().split())
                dot = len(words & old_words)
                similarity = dot / math.sqrt(max(1, len(words) * len(old_words)))
                if similarity >= 0.95:
                    duplicate = old
                    break
            if duplicate and len(item["text"]) > len(duplicate["text"]):
                duplicate.update(item)
            elif not duplicate:
                unique.append(item)
        self.entries = unique

    def __repr__(self):
        return repr(self.entries)


def main():
    m = Memory()
    m.add("User name is Alice", 1)
    m.add("The user's name is Alice", 2)
    m.deduplicate()
    print(m)


if __name__ == "__main__":
    main()
