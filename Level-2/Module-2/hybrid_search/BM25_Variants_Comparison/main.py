import math


class KeywordSearch:
    def __init__(self, documents):
        self.documents = documents

    def rank(self, query):
        raise NotImplementedError


def document_frequencies(documents, terms):
    return {
        term: sum(term in document.lower().split() for document in documents)
        for term in terms
    }


class TFIDFSearch(KeywordSearch):
    def rank(self, query):
        terms = query.lower().split()
        frequencies = document_frequencies(self.documents, terms)
        results = []
        for index, document in enumerate(self.documents):
            words = document.lower().split()
            score = 0
            for term in terms:
                term_frequency = words.count(term) / max(len(words), 1)
                inverse_frequency = (
                    math.log((len(self.documents) + 1) / (frequencies[term] + 1)) + 1
                )
                score += term_frequency * inverse_frequency
            results.append((round(score, 4), index))
        return sorted(results, reverse=True)


class BM25Search(KeywordSearch):
    def rank(self, query):
        return self._rank(query, delta=0)

    def _rank(self, query, delta):
        terms = query.lower().split()
        frequencies = document_frequencies(self.documents, terms)
        average_length = sum(len(item.split()) for item in self.documents)
        average_length /= max(len(self.documents), 1)
        results = []
        for index, document in enumerate(self.documents):
            words = document.lower().split()
            length_ratio = len(words) / max(average_length, 1)
            score = 0
            for term in terms:
                term_frequency = words.count(term)
                idf = math.log(
                    1
                    + (len(self.documents) - frequencies[term] + 0.5)
                    / (frequencies[term] + 0.5)
                )
                saturation = (term_frequency * 2.2) / (
                    term_frequency + 1.2 * (0.25 + 0.75 * length_ratio)
                )
                score += idf * (saturation + delta)
            results.append((round(score, 4), index))
        return sorted(results, reverse=True)


class BM25PlusSearch(BM25Search):
    def rank(self, query):
        return self._rank(query, delta=1)


def main():
    documents = [
        "short search document",
        "long document with search terms and context",
    ]
    rankers = {
        "tfidf": TFIDFSearch(documents),
        "bm25": BM25Search(documents),
        "bm25+": BM25PlusSearch(documents),
    }
    for query in ("search", "search document terms context"):
        print("query:", query)
        for name, ranker in rankers.items():
            print(name, ranker.rank(query))


if __name__ == "__main__":
    main()
