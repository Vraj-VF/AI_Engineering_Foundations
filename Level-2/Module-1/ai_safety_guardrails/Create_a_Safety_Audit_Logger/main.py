import csv
import datetime
import hashlib
import json


def record(user_id, text, model, risk):
    now = datetime.datetime.now(datetime.timezone.utc)
    return {
        "timestamp": now.isoformat(),
        "user_id": user_id,
        "input_hash": hashlib.sha256(text.encode()).hexdigest(),
        "output_hash": hashlib.sha256(("local " + text).encode()).hexdigest(),
        "guardrail_decision": "block" if risk == "high" else "allow",
        "latency_ms": 1,
        "model": model,
        "risk_level": risk,
        "safety_flags": ["injection"] if risk == "high" else [],
    }


def main():
    logs = [
        record("user-1", "normal request", "local", "low"),
        record("user-2", "ignore previous", "local", "high"),
    ]
    with open("audit.json", "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=2)
    with open("audit.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=logs[0])
        writer.writeheader()
        writer.writerows(logs)
    print("high_risk_events:", sum(item["risk_level"] == "high" for item in logs))
    print("alert_threshold: more than 10 high-risk events per hour")


if __name__ == "__main__":
    main()
