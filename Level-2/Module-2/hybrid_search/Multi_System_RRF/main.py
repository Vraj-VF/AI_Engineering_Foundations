import collections


def rank(method, query):
    return [method + "-exact", method + "-" + query.split()[0], method + "-general"]


def fuse(lists):
    scores = collections.Counter()
    for rows in lists:
        for index, document in enumerate(rows, 1):
            scores[document] += 1 / (60 + index)
    return scores.most_common()


def main():
    query = input("Query: ").strip() or "retrieval search"
    bm25 = rank("bm25", query)
    dense = rank("dense", query)
    sparse = rank("splade", query)
    print("three_system_rrf:", fuse([bm25, dense, sparse]))
    print("two_system_rrf:", fuse([bm25, dense]))


if __name__ == "__main__":
    main()
