import json


class ConfigurationManager:
    def __init__(self, filename, required):
        self.filename = filename
        self.required = required
        self.settings = {}

    def load(self):
        with open(self.filename, encoding="utf-8") as file:
            self.settings = json.load(file)
        missing = [key for key in self.required if key not in self.settings]
        if missing:
            raise ValueError("Missing required keys: " + ", ".join(missing))

    def get(self, key, default=None):
        return self.settings.get(key, default)


def main():
    try:
        manager = ConfigurationManager(
            input("JSON filename: "), ["model", "temperature"]
        )
        manager.load()
        print(manager.get("model"))
        print(manager.get("optional", "default"))
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(error)


if __name__ == "__main__":
    main()
