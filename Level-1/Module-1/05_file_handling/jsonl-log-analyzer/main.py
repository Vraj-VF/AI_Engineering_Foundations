import json


class JSONLLogAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def analyze(self):
        total = 0
        errors = 0
        calls = {}
        with open(self.filename, encoding="utf-8") as file:
            for line in file:
                try:
                    record = json.loads(line)
                    total += 1
                    errors += record.get("level") == "ERROR"
                    model = record.get("model", "unknown")
                    calls[model] = calls.get(model, 0) + 1
                except json.JSONDecodeError:
                    pass
        return {
            "total": total,
            "error_rate": errors / total if total else 0,
            "calls_per_model": calls,
        }

    def write_report(self, filename, summary):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("# Log summary\n\n" + str(summary) + "\n")


def main():
    try:
        analyzer = JSONLLogAnalyzer(input("JSONL filename: "))
        summary = analyzer.analyze()
        analyzer.write_report(input("Markdown report: "), summary)
        print(summary)
    except OSError as error:
        print(error)


if __name__ == "__main__":
    main()
