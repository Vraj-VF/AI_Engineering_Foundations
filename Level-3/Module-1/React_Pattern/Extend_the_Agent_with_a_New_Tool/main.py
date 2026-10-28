import os


def unit_converter(value, source, target):
    factors = {
        "km:miles": 0.621371,
        "miles:km": 1.60934,
        "celsius:fahrenheit": 9 / 5,
        "fahrenheit:celsius": 5 / 9,
        "kg:pounds": 2.20462,
        "pounds:kg": 0.453592,
    }
    key = f"{source.lower()}:{target.lower()}"
    if key not in factors:
        raise ValueError(f"Unsupported conversion: {source} to {target}")
    if key == "celsius:fahrenheit":
        return value * factors[key] + 32
    if key == "fahrenheit:celsius":
        return (value - 32) * factors[key]
    return value * factors[key]


def main():
    examples = [(100, "fahrenheit", "celsius"), (5, "km", "miles"), (10, "kg", "pounds")]
    for value, source, target in examples:
        print(value, source, "=", round(unit_converter(value, source, target), 3), target)
    custom = os.getenv("CONVERSION", "")
    if custom:
        value, source, target = custom.split(",")
        print(unit_converter(float(value), source, target))


if __name__ == "__main__":
    main()
