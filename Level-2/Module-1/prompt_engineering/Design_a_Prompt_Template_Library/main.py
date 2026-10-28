import unittest


TEMPLATES = {
    "email": "Draft an email to {recipient} about {subject}. Tone: {tone}.",
    "meeting": "Summarize this meeting for {audience}: {notes}",
    "code_review": "Review this {language} code and list risks:\n{code}",
    "data_analysis": "Interpret these {metric} results for {audience}: {data}",
    "customer_response": "Reply to {customer} about {issue}. Resolution: {resolution}.",
}


def render(name, values):
    if name not in TEMPLATES:
        raise ValueError("unknown template")
    required = {
        "email": ["recipient", "subject"],
        "meeting": ["notes"],
        "code_review": ["language", "code"],
        "data_analysis": ["metric", "data"],
        "customer_response": ["customer", "issue"],
    }[name]
    for key in required:
        if not values.get(key, "").strip():
            raise ValueError(key + " cannot be empty")
    defaults = {
        "tone": "professional",
        "audience": "the team",
        "resolution": "we are investigating",
        "customer": "the customer",
    }
    merged = dict(defaults)
    merged.update(values)
    return TEMPLATES[name].format(**merged)


class TemplateTests(unittest.TestCase):
    def test_templates_and_edge_cases(self):
        self.assertIn(
            "Alice", render("email", {"recipient": "Alice", "subject": "status"})
        )
        self.assertIn("!", render("meeting", {"notes": "Great progress!"}))
        with self.assertRaises(ValueError):
            render("email", {"recipient": "", "subject": "status"})
        long_text = "x" * 10000
        rendered = render("meeting", {"notes": long_text})
        self.assertTrue(rendered.endswith(long_text))
        self.assertGreater(len(rendered), len(long_text))


def main():
    for name in TEMPLATES:
        values = {
            "recipient": "Alex",
            "subject": "project update",
            "notes": "Decisions and actions",
            "language": "Python",
            "code": "print('ok')",
            "metric": "conversion",
            "data": "conversion increased",
            "customer": "Sam",
            "issue": "late delivery",
        }
        print(name + ":", render(name, values))
    unittest.main(argv=["ignored"], exit=False)


if __name__ == "__main__":
    main()
