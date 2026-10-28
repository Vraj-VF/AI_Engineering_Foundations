from fastapi import FastAPI, Query


app = FastAPI(title="Model Registry")
models = [
    {"id": 1, "name": "text-small", "provider": "local"},
    {"id": 2, "name": "vision-large", "provider": "cloud"},
]


@app.get("/models/search")
def search_models(q: str = Query(""), provider: str | None = None):
    matches = [
        model
        for model in models
        if q.lower() in model["name"].lower()
        and (provider is None or model["provider"] == provider)
    ]
    return {"query": q, "provider": provider, "models": matches}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
