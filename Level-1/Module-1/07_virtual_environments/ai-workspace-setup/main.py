import os
import subprocess


def main():
    os.makedirs("ai-learning", exist_ok=True)
    subprocess.run(["python", "-m", "venv", "ai-learning/.venv"])
    print("Install: openai anthropic langchain fastapi")
    subprocess.run(["python", "-m", "pip", "list"])


if __name__ == "__main__":
    main()
