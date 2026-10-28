import secrets
from fastapi import FastAPI, HTTPException

app = FastAPI()
api_keys = {}


@app.post("/admin/keys")
def create_key(owner: str):
    key = secrets.token_urlsafe(24)
    api_keys[key] = owner
    return {"key": key, "owner": owner}


@app.get("/admin/keys")
def list_keys():
    return [{"key": key, "owner": owner} for key, owner in api_keys.items()]


@app.delete("/admin/keys/{key}")
def revoke_key(key: str):
    if api_keys.pop(key, None) is None:
        raise HTTPException(404, "Key not found")
    return {"revoked": True}


if __name__ == "__main__":
    print("uvicorn main:app --reload")
