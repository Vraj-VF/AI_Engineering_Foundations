import time
from fastapi import FastAPI, HTTPException

app = FastAPI()
visits = {}


@app.get("/limited")
def limited(user: str = "anonymous"):
    now = time.time()
    timestamps = [stamp for stamp in visits.get(user, []) if now - stamp < 60]
    if len(timestamps) >= 5:
        raise HTTPException(429, "Rate limit exceeded")
    timestamps.append(now)
    visits[user] = timestamps
    return {"user": user, "requests_remaining": 5 - len(timestamps)}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
