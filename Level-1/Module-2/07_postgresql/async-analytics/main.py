from datetime import date, timedelta
from fastapi import FastAPI

app = FastAPI()


@app.get("/analytics")
async def analytics():
    days = [(date.today() - timedelta(days=offset)).isoformat() for offset in range(30)]
    return {
        "conversations_per_day": {day: 0 for day in days},
        "average_tokens": 0,
        "popular_model": None,
    }


if __name__ == "__main__":
    print("Run with uvicorn main:app --reload")
