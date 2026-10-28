from pathlib import Path


def main():
    Path("app").mkdir(exist_ok=True)
    Path("app/main.py").write_text(
        "from fastapi import FastAPI\napp = FastAPI()\n", encoding="utf-8"
    )
    Path("requirements.txt").write_text("fastapi\nuvicorn\n", encoding="utf-8")
    Path(".env").write_text(
        "API_KEY=change-me\nMODEL_NAME=local-model\n", encoding="utf-8"
    )
    dockerfile = """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
"""
    Path("Dockerfile").write_text(dockerfile, encoding="utf-8")
    print("Docker project created; run docker compose up --build")


if __name__ == "__main__":
    main()
