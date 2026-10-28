import csv


class DatasetLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def filter_score(self, rows, minimum):
        return [row for row in rows if float(row.get("score", 0)) > minimum]


def main():
    try:
        loader = DatasetLoader(input("CSV filename: "))
        rows = loader.load()
        print("rows", len(rows))
        print(loader.filter_score(rows, 0.8))
    except (OSError, ValueError, csv.Error) as error:
        print("Dataset error:", error)


if __name__ == "__main__":
    main()
