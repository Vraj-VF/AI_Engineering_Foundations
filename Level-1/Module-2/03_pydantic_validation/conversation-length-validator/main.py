from fastapi import FastAPI
from pydantic import BaseModel, model_validator

app = FastAPI()


class Conversation(BaseModel):
    messages: list[str]

    @model_validator(mode="after")
    def length_limit(self):
        if sum(len(message) for message in self.messages) > 4000:
            raise ValueError("Conversation exceeds 4000 characters")
        return self


@app.post("/conversations")
def create(conversation: Conversation):
    return {"message_count": len(conversation.messages)}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
