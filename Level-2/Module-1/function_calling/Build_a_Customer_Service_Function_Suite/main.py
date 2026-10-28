import json


CUSTOMERS = {"100": {"name": "Asha", "order": "A-10"}}
ORDERS = {"A-10": "shipped"}


def lookup_customer(customer_id):
    return CUSTOMERS.get(customer_id, {"error": "customer not found"})


def check_order_status(order_id):
    return {"order_id": order_id, "status": ORDERS.get(order_id, "unknown")}


def process_refund(order_id):
    return {"order_id": order_id, "refund": "queued"}


def update_shipping_address(order_id, address):
    return {"order_id": order_id, "address": address, "updated": True}


def escalate_to_human(reason):
    return {"ticket": "LOCAL-1", "reason": reason}


FUNCTIONS = {
    "customer": lookup_customer,
    "order": check_order_status,
    "refund": process_refund,
    "address": update_shipping_address,
    "human": escalate_to_human,
}


def main():
    history = []
    print(
        "Try: customer 100, order A-10, refund A-10, address A-10 Main Street, human urgent"
    )
    while True:
        command = input("service> ").strip()
        if command == "quit":
            break
        parts = command.split(maxsplit=2)
        if not parts or parts[0] not in FUNCTIONS:
            print("Unknown function")
            continue
        arguments = parts[1:]
        result = FUNCTIONS[parts[0]](*arguments)
        history.append({"request": command, "result": result})
        print(json.dumps(result))
    print("conversation_history:", json.dumps(history, indent=2))


if __name__ == "__main__":
    main()
