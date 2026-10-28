from fastapi import FastAPI

app = FastAPI(title="Model Registry")
models = [
    {"task_type": "text", "framework": "pytorch"},
    {"task_type": "text", "framework": "jax"},
    {"task_type": "vision", "framework": "pytorch"},
]


@app.get("/stats")
def model_statistics():
    by_task = {}
    by_framework = {}
    for model in models:
        by_task[model["task_type"]] = by_task.get(model["task_type"], 0) + 1
        by_framework[model["framework"]] = by_framework.get(model["framework"], 0) + 1
    return {"total": len(models), "by_task": by_task, "by_framework": by_framework}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
