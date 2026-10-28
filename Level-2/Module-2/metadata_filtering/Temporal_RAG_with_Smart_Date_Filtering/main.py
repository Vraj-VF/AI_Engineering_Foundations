import datetime
import re


def date_filter(query, today):
    text = query.lower()
    if "last 7 days" in text:
        return today - datetime.timedelta(days=7), today
    if "last year" in text:
        return datetime.date(today.year - 1, 1, 1), datetime.date(
            today.year - 1, 12, 31
        )
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        year = int(match.group(1))
        return datetime.date(year, 1, 1), datetime.date(year, 12, 31)
    return today - datetime.timedelta(days=30), today


def main():
    query = input("Temporal query: ").strip() or "recent policy"
    start, end = date_filter(query, datetime.date.today())
    print(
        {
            "query": query,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "default_window_days": 30,
        }
    )
    print("interpretation affects results by applying metadata date bounds")


if __name__ == "__main__":
    main()
