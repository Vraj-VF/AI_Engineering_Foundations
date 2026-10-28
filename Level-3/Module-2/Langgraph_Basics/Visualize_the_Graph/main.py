def mermaid():
    return "\n".join(
        [
            "graph TD",
            "  START --> understand_issue",
            "  understand_issue --> resolve_issue",
            "  resolve_issue --> confirm_resolution",
            "  confirm_resolution --> collect_feedback",
            "  collect_feedback -->|rating below 3| understand_issue",
            "  collect_feedback -->|rating 3 or above| END",
            "  resolve_issue --> escalation",
            "  escalation --> END",
        ]
    )


def main():
    path = "support_graph.mmd"
    with open(path, "w", encoding="utf-8") as file:
        file.write(mermaid())
    print(path)


if __name__ == "__main__":
    main()
