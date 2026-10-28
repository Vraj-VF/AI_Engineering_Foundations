import json
import os


def local_plan(goal):
    return [
        {"id": "research", "task": f"Gather facts for {goal}", "depends_on": []},
        {"id": "draft", "task": "Draft an answer", "depends_on": ["research"]},
        {"id": "review", "task": "Review the answer", "depends_on": ["draft"]},
    ]


def create_plan(goal):
    if not os.getenv("OPENAI_API_KEY"):
        return local_plan(goal)
    try:
        from openai import OpenAI

        client = OpenAI(timeout=10, max_retries=2)
        result = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Return JSON with a plan list of 3-7 tasks, each having id, task, "
                        f"depends_on. Goal: {goal}"
                    ),
                }
            ],
        )
        plan = json.loads(result.choices[0].message.content).get("plan", [])
        if not plan or any((not isinstance(item.get("depends_on", []), list) for item in plan)):
            raise ValueError("Invalid plan")
        return plan
    except Exception:
        return local_plan(goal)


def main():
    print(json.dumps(create_plan(os.getenv("GOAL", "prepare a product launch")), indent=2))


if __name__ == "__main__":
    main()
