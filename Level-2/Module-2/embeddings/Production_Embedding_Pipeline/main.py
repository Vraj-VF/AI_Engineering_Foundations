import hashlib
import os


class EmbeddingPipeline:
    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size

    def read_documents(self, folder):
        documents = []
        for name in os.listdir(folder):
            if name.lower().endswith((".txt", ".md", ".pdf")):
                path = os.path.join(folder, name)
                with open(path, "rb") as file:
                    documents.append(
                        (name, file.read().decode("utf-8", errors="ignore"))
                    )
        return documents

    def run(self, folder):
        output = []
        for name, text in self.read_documents(folder):
            for index in range(0, len(text), self.chunk_size):
                chunk = text[index : index + self.chunk_size]
                output.append(
                    {
                        "id": hashlib.sha256(f"{name}:{index}".encode()).hexdigest(),
                        "source": name,
                        "chunk": index // self.chunk_size,
                        "embedding": [len(chunk) % 101],
                        "text": chunk,
                    }
                )
        return output


def main():
    folder = input("Document directory: ").strip() or "."
    rows = EmbeddingPipeline().run(folder)
    print("chunks:", len(rows), "backend: local fallback")
    for row in rows[:3]:
        print(row)


if __name__ == "__main__":
    main()
