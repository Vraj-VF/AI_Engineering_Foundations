import random


def execute(steps, failures, strategy):
    completed = []
    for step in steps:
        if step in failures:
            if strategy == "skip" and step != steps[-1]:
                continue
            if strategy == "retry":
                failures.remove(step)
                continue
            return (False, completed)
        completed.append(step)
    return (True, completed)


def main():
    random.seed(7)
    steps = ["research", "draft", "review", "publish"]
    report = []
    for strategy in ("retry", "skip", "abort"):
        successes = 0
        for _ in range(20):
            ok, completed = execute(steps, [random.choice(steps)], strategy)
            successes += ok
            report.append({"strategy": strategy, "success": ok, "steps": len(completed)})
        print(strategy, "recovery rate", successes / 20)
    print("trials", len(report))


if __name__ == "__main__":
    main()
