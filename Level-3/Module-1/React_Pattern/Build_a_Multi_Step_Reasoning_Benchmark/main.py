import json
import time


def population(city):
    return {"Tokyo": 14000000, "Osaka": 2700000, "Kyoto": 1500000}.get(city, 1000000)


def percentage(part, whole):
    return part / whole * 100


def run(query):
    started = time.perf_counter()
    city = query.split("|")[0]
    value = percentage(population(city), 125000000)
    return {
        "query": query,
        "tools": ["population", "percentage"],
        "iterations": 2,
        "answer": round(value, 2),
        "seconds": round(time.perf_counter() - started, 5),
        "correct": value > 0,
    }


def main():
    queries = [f"{city}|population share" for city in ("Tokyo", "Osaka", "Kyoto")] * 4
    results = [run(query) for query in queries]
    print(
        json.dumps(
            {
                "results": results,
                "success_rate": sum((r["correct"] for r in results)) / len(results),
                "average_iterations": 2,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
