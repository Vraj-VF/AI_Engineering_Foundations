from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class StreamChunk(BaseModel):
    text: str = Field(min_length=1)
    index: int = Field(ge=0)
    finished: bool = False


@app.post("/stream/chunks")
def accept_chunk(chunk: StreamChunk):
    return {"accepted": True, "chunk": chunk.model_dump()}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
