import json


def weather(city):
    return {"city": city, "temperature": "21 C", "condition": "clear"}


def use_tool(query, last_city):
    words = query.lower().split()
    if "weather" not in words and "again" not in words:
        return {"message": "Please ask about the weather."}, last_city
    city = words[-1] if words[-1] not in ("again", "weather") else last_city
    if not city:
        return {"question": "Which city?"}, last_city
    return weather(city), city


def main():
    history = []
    last_city = ""
    while True:
        query = input("agent> ").strip()
        if query == "quit":
            break
        result, last_city = use_tool(query, last_city)
        history.append({"user": query, "tool_result": result})
        print(result)
    print("complete_conversation:", json.dumps(history, indent=2))


if __name__ == "__main__":
    main()
