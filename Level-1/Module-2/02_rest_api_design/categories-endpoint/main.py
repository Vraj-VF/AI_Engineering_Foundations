from fastapi import FastAPI

app = FastAPI(title="Prompt Library")
prompts = [
    {"name": "answer", "category": "qa"},
    {"name": "brief", "category": "summary"},
    {"name": "rewrite", "category": "editing"},
]


@app.get("/api/v1/categories")
def categories():
    counts = {}
    for prompt in prompts:
        counts[prompt["category"]] = counts.get(prompt["category"], 0) + 1
    return [{"name": name, "count": count} for name, count in sorted(counts.items())]


if __name__ == "__main__":
    print("uvicorn main:app --reload")
