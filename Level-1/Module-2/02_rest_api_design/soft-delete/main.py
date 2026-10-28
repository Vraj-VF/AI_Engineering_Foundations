from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Prompt Library")
prompts = {1: {"id": 1, "name": "answer", "deleted_at": None}}


def active(prompt_id):
    prompt = prompts.get(prompt_id)
    if prompt is None or prompt["deleted_at"] is not None:
        raise HTTPException(404, "Prompt not found")
    return prompt


@app.delete("/prompts/{prompt_id}")
def delete_prompt(prompt_id: int):
    prompt = active(prompt_id)
    prompt["deleted_at"] = datetime.now().isoformat()
    return prompt


@app.get("/trash")
def trash():
    return [prompt for prompt in prompts.values() if prompt["deleted_at"]]


@app.post("/prompts/{prompt_id}/restore")
def restore(prompt_id: int):
    prompt = prompts.get(prompt_id)
    if prompt is None:
        raise HTTPException(404, "Prompt not found")
    prompt["deleted_at"] = None
    return prompt


if __name__ == "__main__":
    print("uvicorn main:app --reload")
