import json
import time


class AuditLogger:
    def __init__(self):
        self.events = []

    def record(self, state, decision, before, after):
        self.events.append(
            {
                "reviewer": "operator-1",
                "timestamp": time.time(),
                "decision": decision,
                "before": before,
                "after": after,
                "state": state,
            }
        )

    def save(self, path):
        open(path, "w", encoding="utf-8").write(json.dumps(self.events, indent=2))


def main():
    logger = AuditLogger()
    started = time.time()
    logger.record({"step": "review"}, "approve", "Draft", "Draft")
    logger.save("audit_log.json")
    print({"events": len(logger.events), "seconds": time.time() - started})


if __name__ == "__main__":
    main()
