class ModelConfig:
    allowed_models = ["small", "medium", "large"]

    def __init__(self, model, temperature, max_tokens):
        if model not in self.allowed_models:
            raise ValueError("model must be small, medium, or large")
        if not 0 <= temperature <= 2:
            raise ValueError("temperature must be between 0 and 2")
        if max_tokens <= 0:
            raise ValueError("max_tokens must be positive")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def show(self):
        print(self.__dict__)


def main():
    try:
        config = ModelConfig(
            input("Model: "), float(input("Temperature: ")), int(input("Max tokens: "))
        )
        config.show()
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
