def read_model(number):
    return {
        "name": input(f"Model {number} name: "),
        "provider": input("Provider: "),
        "max_tokens": int(input("Max tokens: ")),
        "temperature": float(input("Temperature: ")),
    }


def find_by_provider(configs, provider):
    return [
        config for config in configs if config["provider"].lower() == provider.lower()
    ]


def main():
    configs = [read_model(number) for number in range(1, 6)]
    provider = input("Provider to search: ")
    maximum = int(input("Minimum max_tokens: "))
    for config in find_by_provider(configs, provider):
        if config["max_tokens"] >= maximum:
            print(config)
    print("Temperature comparison:")
    for config in configs:
        print(config["name"], config["temperature"])


if __name__ == "__main__":
    main()
