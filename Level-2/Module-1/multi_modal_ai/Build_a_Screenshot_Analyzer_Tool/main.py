import json
import os


def analyze(path):
    exists = os.path.exists(path)
    name = os.path.basename(path).lower()
    kind = "chart" if "chart" in name else "webpage" if "web" in name else "ui"
    return {
        "file": path,
        "exists": exists,
        "content_type": kind,
        "visible_text": [],
        "ui_elements": [],
        "alt_text": f"{kind} screenshot ({name})",
    }


def main():
    path = input("Screenshot path: ").strip() or "sample_ui.png"
    report = analyze(path)
    with open("screenshot_analysis.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
