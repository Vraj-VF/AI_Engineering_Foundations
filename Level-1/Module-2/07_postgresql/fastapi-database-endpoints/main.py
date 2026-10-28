import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Database API")


class Model(BaseModel):
    name: str


@app.post("/models")
def create_model(model: Model):
    return {"id": 1, "name": model.name}


@app.post("/conversations")
def start_conversation(model_id: int):
    return {"id": model_id, "messages": []}


@app.post("/conversations/{conversation_id}/messages")
def add_message(conversation_id: int, text: str):
    return {"conversation_id": conversation_id, "text": text}


if __name__ == "__main__":
    print("Run with uvicorn main:app --reload")
