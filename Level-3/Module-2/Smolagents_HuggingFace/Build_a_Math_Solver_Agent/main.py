import math


def solve_equation(a, b, c):
    d = b * b - 4 * a * c
    return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)] if d >= 0 else []


def unit_convert(value, source, target):
    return value * 3.28084 if (source, target) == ("m", "ft") else value


def plot_function(a, b, c, start, end):
    return {
        "expression": f"{a}x^2+{b}x+{c}",
        "range": [start, end],
        "points": [a * x * x + b * x + c for x in (start, end)],
    }


def main():
    roots = solve_equation(1, -5, 6)
    print(
        {
            "roots": roots,
            "plot": plot_function(1, -5, 6, 0, 5),
            "feet": [unit_convert(root, "m", "ft") for root in roots],
        }
    )


if __name__ == "__main__":
    main()
