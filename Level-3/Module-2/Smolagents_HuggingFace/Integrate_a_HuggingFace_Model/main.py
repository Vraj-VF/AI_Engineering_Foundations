import os


def main():
    token = bool(os.getenv("HF_TOKEN"))
    print(
        {
            "model": os.getenv("HF_MODEL", "HuggingFaceTB/SmolLM2-1.7B-Instruct"),
            "live_inference": token,
            "result": "local data analysis fallback"
            if not token
            else "configure HfApiModel with token",
        }
    )


if __name__ == "__main__":
    main()
