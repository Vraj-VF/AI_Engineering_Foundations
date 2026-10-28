class PromptTemplate:
    def __init__(self, template, defaults=None, required=None):
        self.template = template
        self.defaults = defaults or {}
        self.required = required or []

    def format(self, values):
        data = self.defaults.copy()
        data.update(values)
        missing = [name for name in self.required if name not in data]
        if missing:
            raise ValueError("Missing: " + ", ".join(missing))
        result = self.template
        for name, value in data.items():
            result = result.replace("{{" + name + "}}", str(value))
        return result


def main():
    template = PromptTemplate(
        input("Template: "), {"tone": input("Default tone: ")}, ["topic"]
    )
    try:
        print(template.format({"topic": input("Topic: ")}))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
