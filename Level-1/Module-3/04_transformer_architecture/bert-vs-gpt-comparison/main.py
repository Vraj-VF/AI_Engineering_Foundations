architectures = {
    "BERT": {"mask": "bidirectional", "objective": "masked tokens"},
    "GPT": {"mask": "causal", "objective": "next token"},
}
for name, details in architectures.items():
    print(name, details)
print("BERT can use both directions; GPT prevents attention to future tokens.")
