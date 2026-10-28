class VectorStore:
    def __init__(self):
        self.documents = {}

    def add(self, text, metadata):
        doc_id = str(len(self.documents) + 1)
        self.documents[doc_id] = {"text": text, "metadata": metadata}
        return doc_id

    def search(self, query, top_k=3, filters=None):
        filters = filters or {}
        rows = [
            item
            for item in self.documents.items()
            if all(
                item[1]["metadata"].get(key) == value for key, value in filters.items()
            )
        ]
        return sorted(
            rows,
            key=lambda item: len(
                set(query.lower().split()) & set(item[1]["text"].lower().split())
            ),
            reverse=True,
        )[:top_k]

    def get(self, doc_id):
        return self.documents.get(doc_id)

    def update(self, doc_id, new_text):
        self.documents[doc_id]["text"] = new_text

    def delete(self, doc_id):
        self.documents.pop(doc_id, None)

    def count(self, filters=None):
        return len(self.search("", len(self.documents), filters))


def main():
    store = VectorStore()
    doc_id = store.add("local vector search", {"tenant": "one"})
    print("get:", store.get(doc_id))
    print("search:", store.search("vector"))
    store.update(doc_id, "updated vector document")
    print("count:", store.count({"tenant": "one"}))
    store.delete(doc_id)
    print("count_after_delete:", store.count())


if __name__ == "__main__":
    main()
