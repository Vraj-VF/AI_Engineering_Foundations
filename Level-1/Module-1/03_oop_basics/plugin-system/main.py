class Plugin:
    def execute(self, text):
        raise NotImplementedError


class SentimentAnalyzer(Plugin):
    def execute(self, text):
        positive = sum(
            word in ["good", "great", "helpful"] for word in text.lower().split()
        )
        negative = sum(
            word in ["bad", "poor", "broken"] for word in text.lower().split()
        )
        return (
            "positive"
            if positive > negative
            else "negative"
            if negative > positive
            else "neutral"
        )


class TextSummarizer(Plugin):
    def execute(self, text):
        return " ".join(text.split()[:10])


class CodeReviewer(Plugin):
    def execute(self, text):
        return (
            "Review: add tests"
            if "test" not in text.lower()
            else "Review: tests mentioned"
        )


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def execute(self, name, text):
        return self.plugins[name].execute(text)


def main():
    manager = PluginManager()
    manager.register("sentiment", SentimentAnalyzer())
    manager.register("summary", TextSummarizer())
    manager.register("review", CodeReviewer())
    text = input("Text: ")
    for name in manager.plugins:
        print(name, manager.execute(name, text))


if __name__ == "__main__":
    main()
