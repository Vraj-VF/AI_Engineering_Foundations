import hashlib
import os


def ingest(folder):
    records = []
    for name in os.listdir(folder):
        if not name.endswith((".txt", ".md")):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as file:
            text = file.read()
        for index in range(0, len(text), 500):
            chunk = text[index : index + 500]
            records.append(
                {
                    "id": hashlib.sha256(f"{name}:{index // 500}".encode()).hexdigest(),
                    "text": chunk,
                    "source_file": name,
                    "chunk_index": index // 500,
                    "file_type": os.path.splitext(name)[1],
                }
            )
    return records


def main():
    folder = input("Directory: ").strip() or "."
    records = ingest(folder)
    print("qdrant_collection: local_documents")
    print("records:", len(records))
    print(*records[:3], sep="\n")


if __name__ == "__main__":
    main()
