from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
profiles = {}


class ConfigurationProfile(BaseModel):
    name: str = Field(min_length=1)
    model: str
    temperature: float = Field(ge=0, le=2)
    max_tokens: int = Field(gt=0)


@app.post("/profiles")
def save(profile: ConfigurationProfile):
    profiles[profile.name] = profile
    return profile


@app.get("/profiles/{name}")
def get(name: str):
    if name not in profiles:
        raise HTTPException(404, "Profile not found")
    return profiles[name]


if __name__ == "__main__":
    print("uvicorn main:app --reload")
