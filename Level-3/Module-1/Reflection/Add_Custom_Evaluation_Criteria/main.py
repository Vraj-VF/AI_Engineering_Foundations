def relevance(output, question):
    question_words = set(question.lower().split())
    output_words = set(output.lower().split())
    return len(question_words & output_words) / max(1, len(question_words))


def evidence(output):
    markers = ("http://", "https://", "source:", "according to")
    return 1.0 if any(marker in output.lower() for marker in markers) else 0.0


def conciseness(output):
    word_count = len(output.split())
    if word_count <= 12:
        return 1.0
    return max(0.0, 1.0 - (word_count - 12) / 20)


WEIGHTS = {"relevance": 0.5, "evidence": 0.3, "conciseness": 0.2}


def score(output, question, weights=WEIGHTS):
    values = {
        "relevance": relevance(output, question),
        "evidence": evidence(output),
        "conciseness": conciseness(output),
    }
    weighted = sum(values[name] * weights[name] for name in values)
    return {**values, "weighted": round(weighted, 3)}


def test_relevance():
    assert relevance("Python loops repeat work", "Explain Python loops") > 0
    assert relevance("A weather report", "Explain Python loops") == 0


def test_evidence():
    assert evidence("According to source: https://example.test") == 1
    assert evidence("This is an unsupported claim") == 0


def test_conciseness():
    assert conciseness("short answer") == 1
    assert conciseness("word " * 40) < 1


def main():
    test_relevance()
    test_evidence()
    test_conciseness()
    cases = [
        ("Explain Python loops", "Python loops repeat work according to source: docs."),
        ("Explain testing", "Testing checks behavior."),
        ("Explain agents", "Agents plan, use tools, and reflect."),
        ("Explain memory", "Memory stores context according to https://example.test."),
        ("Explain APIs", "APIs connect systems. " + "They are useful. " * 8),
    ]
    for question, output in cases:
        base = relevance(output, question)
        improved = score(output, question)["weighted"]
        print(question, {"before": round(base, 3), "after": improved})


if __name__ == "__main__":
    main()
