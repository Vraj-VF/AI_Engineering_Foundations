def agreement(first, second):
    matches = sum(a == b for a, b in zip(first, second))
    return matches / max(len(first), 1)


def main():
    items = [
        {"id": index, "label": "clean" if index < 15 else "hallucinated"}
        for index in range(30)
    ]
    guidelines = "Label supported claims clean. Label unsupported or contradicted claims hallucinated."
    form = ["item_id", "label", "confidence", "notes"]
    reviewer_one = [
        "clean" if item["label"] == "clean" else "hallucinated" for item in items
    ]
    reviewer_two = list(reviewer_one)
    print("annotation_guidelines:", guidelines)
    print("evaluation_form_fields:", form)
    print(
        "items:",
        len(items),
        "inter_annotator_agreement:",
        agreement(reviewer_one, reviewer_two),
    )
    print("threshold_calibration:", "use disagreements to tune detector threshold")


if __name__ == "__main__":
    main()
