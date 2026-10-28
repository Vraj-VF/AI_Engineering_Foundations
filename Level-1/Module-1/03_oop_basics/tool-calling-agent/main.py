class Agent:
    def __init__(self):
        self.tools = {}

    def register_tool(self, keyword, function):
        self.tools[keyword] = function

    def respond(self, message):
        for keyword, function in self.tools.items():
            if keyword in message.lower():
                return function(message)
        return "No matching tool"


def calculate(message):
    return "Calculate tool selected: " + message


def summarize(message):
    return "Summarize tool selected: " + message


def main():
    agent = Agent()
    agent.register_tool("calculate", calculate)
    agent.register_tool("summarize", summarize)
    print(agent.respond(input("Request: ")))


if __name__ == "__main__":
    main()
