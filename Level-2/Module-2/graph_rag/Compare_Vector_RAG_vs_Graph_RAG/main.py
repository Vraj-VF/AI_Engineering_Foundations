def vector_answer(question):
    return "vector retrieval answer for " + question


def graph_answer(question):
    return "graph traversal answer for " + question


def main():
    questions = [("vector question " + str(i), "vector") for i in range(5)]
    questions.extend(("graph question " + str(i), "graph") for i in range(5))
    for question, favored in questions:
        vector_score = 4 if favored == "vector" else 3
        graph_score = 4 if favored == "graph" else 3
        winner = "vector" if vector_score > graph_score else "graph"
        print(
            question, "vector=", vector_score, "graph=", graph_score, "winner=", winner
        )


if __name__ == "__main__":
    main()
