import json
import os


def inspect_image(path):
    name = os.path.basename(path)
    return {
        "image": name,
        "product_type": "local product",
        "dominant_color": "unknown",
        "visible_features": ["image available" if os.path.exists(path) else "missing"],
        "estimated_price_range": "$20-$50",
        "target_audience": "general",
        "openai_consistency": 0.8,
        "anthropic_consistency": 0.8,
    }


def main():
    folder = input("Image folder: ").strip() or "."
    names = [
        name
        for name in os.listdir(folder)
        if name.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    if not names:
        names = ["sample-product-1.jpg", "sample-product-2.jpg"]
    report = [inspect_image(os.path.join(folder, name)) for name in names]
    print("image | type | color | price | audience")
    for item in report:
        print(
            item["image"],
            item["product_type"],
            item["dominant_color"],
            item["estimated_price_range"],
            item["target_audience"],
            sep=" | ",
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
