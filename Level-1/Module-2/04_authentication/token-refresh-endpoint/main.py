from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException

app = FastAPI()
refresh_tokens = {"demo-refresh": "user-1"}


@app.post("/auth/refresh")
def refresh(token: str):
    user = refresh_tokens.get(token)
    if user is None:
        raise HTTPException(401, "Invalid refresh token")
    expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    return {"access_token": "access-" + user, "expires_at": expires.isoformat()}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
