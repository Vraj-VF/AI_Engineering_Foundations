def tester(code):
    return {"passed": "TODO" not in code, "cases": ["syntax", "behavior"]}


def workflow(task):
    for attempt in range(3):
        code = f"solution for {task}" if attempt else "TODO solution"
        result = tester(code)
        if result["passed"]:
            return {"code": code, "test_results": result, "retries": attempt}
    return {"test_results": result, "retries": 2}


def main():
    print(workflow("calculate invoice"))


if __name__ == "__main__":
    main()
