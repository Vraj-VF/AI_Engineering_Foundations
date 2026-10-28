def words(text):
    return {word.strip(".,!?") for word in text.lower().split()}


def faithfulness(sample):
    context = " ".join(sample["contexts"]).lower()
    claims = [
        claim.strip() for claim in sample["answer"].lower().split(".") if claim.strip()
    ]
    supported = sum(
        all(word.strip(".,!?") in context for word in claim.split())
        for claim in claims
    )
    return supported / max(len(claims), 1)


def answer_relevancy(sample):
    question_terms = words(sample["question"])
    answer_terms = words(sample["answer"])
    return len(question_terms & answer_terms) / max(len(question_terms), 1)


def context_precision(sample):
    truth = words(sample["ground_truth"])
    precision_values = []
    for context in sample["contexts"]:
        context_terms = words(context)
        precision_values.append(len(context_terms & truth) / max(len(context_terms), 1))
    return sum(precision_values) / max(len(precision_values), 1)


def context_recall(sample):
    truth = words(sample["ground_truth"])
    context = words(" ".join(sample["contexts"]))
    return len(truth & context) / max(len(truth), 1)


def main():
    samples = [
        {
            "question": "How long are support tickets retained?",
            "answer": "Support tickets are retained for 90 days.",
            "ground_truth": "Tickets are retained for 90 days.",
            "contexts": ["The support system retains tickets for 90 days."],
        },
        {
            "question": "Who approves production deployments?",
            "answer": "The release manager approves production deployments.",
            "ground_truth": "A release manager must approve production deployments.",
            "contexts": ["Production changes require release manager approval."],
        },
        {
            "question": "What is the password reset window?",
            "answer": "Password reset links expire after 30 minutes.",
            "ground_truth": "Reset links expire after 30 minutes.",
            "contexts": ["Reset links are valid for 30 minutes."],
        },
        {
            "question": "Where are backups stored?",
            "answer": "Backups are stored in the regional vault.",
            "ground_truth": "The regional vault stores backups.",
            "contexts": ["Encrypted backups are copied to the regional vault."],
        },
        {
            "question": "What is the incident response target?",
            "answer": "Critical incidents receive a response within one hour.",
            "ground_truth": "Critical incidents have a one-hour response target.",
            "contexts": ["The critical incident response target is one hour."],
        },
        {
            "question": "Which team owns billing changes?",
            "answer": "The finance platform team owns billing changes.",
            "ground_truth": "Finance platform owns billing changes.",
            "contexts": ["Billing configuration is maintained by finance platform."],
        },
        {
            "question": "What does the data export include?",
            "answer": "Exports include account identifiers and usage totals.",
            "ground_truth": "Exports contain identifiers and usage totals.",
            "contexts": ["The export contains account identifiers and usage totals."],
        },
        {
            "question": "How often is the access review performed?",
            "answer": "Access reviews are performed every quarter.",
            "ground_truth": "Access reviews happen quarterly.",
            "contexts": ["Managers complete access reviews once per quarter."],
        },
        {
            "question": "What is the API request limit?",
            "answer": "The API permits 100 requests per minute.",
            "ground_truth": "The API rate limit is 100 requests per minute.",
            "contexts": ["Clients may send 100 requests per minute."],
        },
        {
            "question": "Which format is used for audit exports?",
            "answer": "Audit exports use JSON format.",
            "ground_truth": "Audit events can be exported as JSON.",
            "contexts": ["The audit export format is JSON."],
        },
    ]
    rows = [
        {
            "faithfulness": faithfulness(sample),
            "answer_relevancy": answer_relevancy(sample),
            "context_precision": context_precision(sample),
            "context_recall": context_recall(sample),
        }
        for sample in samples
    ]
    aggregate = {
        name: round(sum(row[name] for row in rows) / len(rows), 3) for name in rows[0]
    }
    print("per_sample:", rows)
    print("aggregate:", aggregate)
    print(
        "weakest_metric:",
        min(aggregate, key=aggregate.get),
        "hypothesis: context coverage",
    )


if __name__ == "__main__":
    main()
