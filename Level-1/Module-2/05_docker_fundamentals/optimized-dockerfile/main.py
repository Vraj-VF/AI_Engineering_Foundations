from pathlib import Path


def main():
    Path(".dockerignore").write_text(
        ".git\n.venv\n__pycache__\n*.pyc\n.env\n", encoding="utf-8"
    )
    dockerfile = """FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
"""
    Path("Dockerfile").write_text(dockerfile, encoding="utf-8")
    print("Multi-stage Dockerfile and .dockerignore created")


if __name__ == "__main__":
    main()
