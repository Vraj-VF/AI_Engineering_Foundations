import json


def search_product(name):
    return {"product_id": "P-1", "name": name, "price": 100.0}


def check_inventory(product):
    product["stock"] = 7
    return product


def calculate_discount(product):
    if product["stock"] <= 0:
        raise ValueError("out of stock")
    product["discounted_price"] = round(product["price"] * 0.9, 2)
    return product


def main():
    name = input("Product: ").strip() or "notebook"
    context = search_product(name)
    context = check_inventory(context)
    context = calculate_discount(context)
    print(json.dumps(context, indent=2))


if __name__ == "__main__":
    main()
