def sequential(task):
    return ["research", "write", "review"]


def hierarchical(task):
    return ["manager assigns research", "writer", "fact checker", "reviewer"]


def main():
    print(
        {
            "sequential": sequential("article"),
            "hierarchical": hierarchical("article"),
            "manager": "delegates based on results",
        }
    )


if __name__ == "__main__":
    main()
