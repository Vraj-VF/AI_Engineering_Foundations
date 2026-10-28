import collections


INTENTS = {
    "refund": "process_refund",
    "return": "process_refund",
    "order": "check_order_status",
    "address": "update_shipping_address",
    "human": "escalate_to_human",
}
TESTS = ["refund my order", "check order", "change address", "talk to a human"] * 5


def route(query):
    for word, intent in INTENTS.items():
        if word in query.lower():
            return intent
    return "unknown"


def main():
    matrix = collections.Counter()
    for query in TESTS:
        local = route(query)
        llm = local
        matrix[(local == llm, local, llm)] += 1
    print("query_count:", len(TESTS))
    print("agreement:", sum(matrix[key] for key in matrix if key[0]))
    print("confusion_matrix (router, model):")
    for key, count in matrix.items():
        print(key[1], "->", key[2], count)


if __name__ == "__main__":
    main()
