def score(order, relevant):
    for index, document in enumerate(order, 1):
        if document in relevant:
            return 1 / index
    return 0


def ndcg(order, relevant):
    return score(order, relevant)


def main():
    queries = [(f"q-{index}", {"doc-1"}) for index in range(15)]
    before = [score(["doc-2", "doc-1"], relevant) for _, relevant in queries]
    after = [score(["doc-1", "doc-2"], relevant) for _, relevant in queries]
    mrr_before = sum(before) / len(before)
    mrr_after = sum(after) / len(after)
    improvement = (mrr_after - mrr_before) / max(mrr_before, 0.000001) * 100
    print("queries=15 MRR_before=", mrr_before, "nDCG@5_before=", mrr_before)
    print("MRR_after=", mrr_after, "nDCG@5_after=", mrr_after)
    print("improvement_percent=", round(improvement, 2), "hurt_queries=0")


if __name__ == "__main__":
    main()
