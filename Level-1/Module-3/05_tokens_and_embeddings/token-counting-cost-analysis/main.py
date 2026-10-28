def estimate(text, price):
    token_count = len(text.split())
    return token_count, token_count * price / 1000000


def main():
    text = input("Text: ")
    price = float(input("Price per million tokens: "))
    count, cost = estimate(text, price)
    print("Tokens:", count)
    print("Cost:", cost)


if __name__ == "__main__":
    main()
