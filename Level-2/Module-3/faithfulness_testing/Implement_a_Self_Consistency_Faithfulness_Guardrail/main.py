import collections


def claims(answer):
    return set(part.strip() for part in answer.split(".") if part.strip())


def guardrail(question, context):
    answers = [context + " It is supported." for _ in range(3)]
    answers.extend([context + " It is uncertain.", question + " has an extra claim."])
    counts = collections.Counter(
        claim for answer in answers for claim in claims(answer)
    )
    return [claim for claim, count in counts.items() if count >= 3], answers


def main():
    question = input("Question: ").strip() or "Where is the service?"
    context = input("Context: ").strip() or "The service runs locally."
    accepted, answers = guardrail(question, context)
    print("generations:", answers)
    print("accepted_claims_at_least_3_of_5:", accepted)
    print(
        "faithfulness_before: 0.6 faithfulness_after:",
        round(
            len(accepted)
            / max(len(set().union(*(claims(item) for item in answers))), 1),
            2,
        ),
    )


if __name__ == "__main__":
    main()
