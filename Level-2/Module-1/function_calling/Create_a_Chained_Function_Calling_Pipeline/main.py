import json


def search_flights(origin, destination):
    if not origin or not destination:
        raise ValueError("origin and destination are required")
    return ["FL-101", "FL-202"]


def get_flight_details(flight_id):
    return {"flight_id": flight_id, "base_price": 180.0}


def calculate_total(details, tax_rate=0.1):
    return round(details["base_price"] * (1 + tax_rate), 2)


def main():
    origin = input("Origin: ").strip() or "NYC"
    destination = input("Destination: ").strip() or "LON"
    chain = []
    try:
        flight_ids = search_flights(origin, destination)
        chain.append({"step": "search_flights", "output": flight_ids})
        details = get_flight_details(flight_ids[0])
        chain.append(
            {"step": "get_flight_details", "input": flight_ids[0], "output": details}
        )
        total = calculate_total(details)
        chain.append({"step": "calculate_total", "input": details, "output": total})
        print(json.dumps(chain, indent=2))
    except (ValueError, KeyError) as error:
        print("chain failed:", error)


if __name__ == "__main__":
    main()
