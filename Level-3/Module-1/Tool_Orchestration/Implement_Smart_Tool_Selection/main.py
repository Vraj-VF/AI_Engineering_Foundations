import json


def pattern_select(query):
    tools = []
    if "weather" in query.lower():
        tools.append("weather")
    if "calculate" in query.lower() or "total" in query.lower():
        tools.append("calculator")
    return tools


def llm_select(query):
    return pattern_select(query)


def main():
    queries = [
        "What is the weather?",
        "Calculate the total",
        "Find weather then calculate total",
    ] * 4
    rows = [
        {
            "query": query,
            "pattern": pattern_select(query),
            "llm": llm_select(query),
            "same": pattern_select(query) == llm_select(query),
        }
        for query in queries
    ]
    print(
        json.dumps(
            {"rows": rows, "agreement": sum((row["same"] for row in rows)) / len(rows)}, indent=2
        )
    )


if __name__ == "__main__":
    main()
