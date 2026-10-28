import importlib.util


def main():
    filename = input("requirements filename: ")
    with open(filename, encoding="utf-8") as file:
        requirements = [line.strip().split("==")[0] for line in file if line.strip()]
    for package in requirements:
        print(package, "installed" if importlib.util.find_spec(package) else "missing")


if __name__ == "__main__":
    main()
