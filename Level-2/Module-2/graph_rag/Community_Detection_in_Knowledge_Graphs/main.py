import collections


def detect(edges):
    labels = {}
    for left, right in edges:
        labels.setdefault(left, left)
        labels.setdefault(right, right)
        if labels[left] != labels[right]:
            old = labels[right]
            for node in labels:
                if labels[node] == old:
                    labels[node] = labels[left]
    return labels


def main():
    edges = [
        ("search", "retrieval"),
        ("retrieval", "embedding"),
        ("billing", "invoice"),
    ]
    labels = detect(edges)
    communities = collections.defaultdict(list)
    for entity, community in labels.items():
        communities[community].append(entity)
    for community, entities in communities.items():
        print("community:", community, "summary:", ", ".join(entities))
    print("global_answer:", "community summaries connect thematic entities")
    print("direct_graph_answer:", edges)


if __name__ == "__main__":
    main()
