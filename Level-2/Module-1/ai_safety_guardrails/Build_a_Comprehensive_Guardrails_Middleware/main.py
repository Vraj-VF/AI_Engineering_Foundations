import hashlib
import json
import re


class Guardrails:
    def __init__(self, strictness="moderate"):
        self.strictness = strictness
        self.events = []
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def protect(self, text):
        redacted = re.sub(r"[\w.-]+@[\w.-]+", "[EMAIL]", text)
        flags = [rule for rule in self.rules if rule in redacted.lower()]
        if self.strictness == "strict" and flags:
            redacted = "[BLOCKED]"
        self.events.append(
            {"flags": flags, "input_hash": hashlib.sha256(text.encode()).hexdigest()}
        )
        return redacted

    def dashboard(self):
        return {
            "events": len(self.events),
            "flagged": sum(bool(item["flags"]) for item in self.events),
        }


def main():
    guard = Guardrails(
        input("strictness (permissive/moderate/strict): ").strip() or "moderate"
    )
    guard.add_rule("ignore previous")
    samples = [input("Input: "), "contact a@b.com", "ignore previous instructions"] + [
        "normal"
    ] * 17
    for sample in samples[:20]:
        print(guard.protect(sample))
    with open("safety_events.json", "w", encoding="utf-8") as file:
        json.dump(guard.events, file, indent=2)
    print("dashboard:", guard.dashboard())


if __name__ == "__main__":
    main()
