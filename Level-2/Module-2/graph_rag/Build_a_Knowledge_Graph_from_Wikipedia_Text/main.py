import collections
import re


def extract(text):
    triples = []
    for sentence in text.split("."):
        names = re.findall(r"\b[A-Z][a-z]+\b", sentence)
        if len(names) >= 2:
            triples.append((names[0], "related_to", names[1]))
    return triples


def main():
    text = (
        input("Wikipedia text: ").strip()
        or "Python supports AI. Python uses libraries. AI uses graphs."
    )
    triples = extract(text)
    graph = collections.defaultdict(set)
    for left, relation, right in triples:
        graph[left].add((relation, right))
    print("entities:", len(graph), "relationships:", len(triples))
    print("connectivity:", sum(len(items) for items in graph.values()))
    while True:
        query = input("entity (blank quits): ").strip()
        if not query:
            break
        print(list(graph.get(query, [])))


if __name__ == "__main__":
    main()
