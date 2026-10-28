def researcher(task):
    return f"facts about {task}"


def coder(facts):
    return f"code based on {facts}"


def reviewer(code):
    return {"approved": True, "review": f"Reviewed {code}"}


def main():
    facts = researcher("user request")
    code = coder(facts)
    print(
        {
            "research": facts,
            "code": code,
            "review": reviewer(code),
            "flow": "Researcher -> Coder -> Reviewer -> END",
        }
    )


if __name__ == "__main__":
    main()
