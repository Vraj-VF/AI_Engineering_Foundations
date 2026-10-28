def review(draft):
    while True:
        try:
            decision = input("approve, reject, or edit <message>: ").strip()
        except EOFError:
            decision = "approve"
        if decision == "approve":
            return {"status": "approved", "message": draft}
        if decision == "reject":
            return {"status": "rejected", "message": draft}
        if decision.startswith("edit "):
            draft = decision[5:]
            return {"status": "edited", "message": draft}
        print("Unexpected input")


def main():
    print(review("Proposed response"))


if __name__ == "__main__":
    main()
