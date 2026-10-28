from fastapi import FastAPI, HTTPException

app = FastAPI(title="Prompt Library")
prompts = [{"name": "zeta", "category": "qa"}, {"name": "alpha", "category": "summary"}]


@app.get("/prompts")
def list_prompts(sort_by: str = "name", sort_order: str = "asc"):
    if sort_by not in ["name", "category"] or sort_order not in ["asc", "desc"]:
        raise HTTPException(400, "Invalid sort parameters")
    return sorted(
        prompts, key=lambda prompt: prompt[sort_by], reverse=sort_order == "desc"
    )


if __name__ == "__main__":
    print("uvicorn main:app --reload")
