import subprocess
from pathlib import Path


def run(*args):
    return subprocess.run(["git", *args], text=True, capture_output=True)


def main():
    result = run("init", "ai-sentiment-analyzer")
    print(result.stdout or result.stderr)
    project = Path("ai-sentiment-analyzer")
    (project / "src").mkdir(parents=True, exist_ok=True)
    (project / "tests").mkdir(exist_ok=True)
    (project / "src" / "model.py").write_text(
        "def sentiment(text): return 'positive' if 'good' in text.lower() else 'neutral'\n",
        encoding="utf-8",
    )
    print("Created project structure and src/model.py")


if __name__ == "__main__":
    main()
