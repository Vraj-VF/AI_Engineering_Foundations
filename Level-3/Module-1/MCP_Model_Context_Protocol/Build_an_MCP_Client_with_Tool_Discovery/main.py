import json


class ToolClient:
    def __init__(self, servers):
        self.servers = servers
        self.catalog = {}

    def discover(self):
        for server, tools in self.servers.items():
            for tool in tools:
                self.catalog[tool] = {"server": server, "name": tool}
        return self.catalog

    def call(self, name, value):
        if name not in self.catalog:
            raise KeyError(name)
        return {"tool": name, "server": self.catalog[name]["server"], "value": value}


def main():
    client = ToolClient({"files": ["read_json"], "text": ["uppercase", "word_count"]})
    print(json.dumps(client.discover(), indent=2))
    print(client.call("uppercase", "hello"))


if __name__ == "__main__":
    main()
