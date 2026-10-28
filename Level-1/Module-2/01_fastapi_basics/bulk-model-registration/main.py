from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Model Registry")
models = []


class ModelCreate(BaseModel):
    name: str
    task_type: str
    framework: str = "pytorch"


@app.post("/models/bulk", status_code=201)
def register_models(items: list[ModelCreate]):
    start = len(models) + 1
    created = []
    for offset, item in enumerate(items):
        model = {"id": start + offset, **item.model_dump()}
        models.append(model)
        created.append(model)
    return {"created": len(created), "models": created}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
