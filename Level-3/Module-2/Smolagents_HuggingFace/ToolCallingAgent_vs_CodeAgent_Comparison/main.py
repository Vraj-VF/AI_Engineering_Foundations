def run(agent):
    return {
        "agent": agent,
        "steps": 3 if agent == "CodeAgent" else 4,
        "correct": True,
        "actions": "python code" if agent == "CodeAgent" else "named tool calls",
    }


def main():
    print(
        {"runs": [run("CodeAgent"), run("ToolCallingAgent")], "easier_to_debug": "ToolCallingAgent"}
    )


if __name__ == "__main__":
    main()
