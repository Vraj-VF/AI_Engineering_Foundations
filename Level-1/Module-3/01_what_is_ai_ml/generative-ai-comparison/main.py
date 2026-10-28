modalities = {
    "text": "language model",
    "image": "diffusion model",
    "video": "video generator",
    "audio": "speech generator",
}
for modality, model in modalities.items():
    print(
        f"{modality}: {model}; input and output should be evaluated for "
        "quality, cost, and misuse risk"
    )
print("Choose one application and describe its data, evaluation, and fairness risks.")
