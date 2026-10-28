import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="ai-project")
parser.add_argument("--pytorch", action="store_true")
parser.add_argument("--transformers", action="store_true")
args = parser.parse_args()
os.makedirs(os.path.join(args.name, "src"), exist_ok=True)
os.makedirs(os.path.join(args.name, "tests"), exist_ok=True)
packages = ["fastapi"]
if args.pytorch:
    packages.append("torch")
if args.transformers:
    packages.append("transformers")
open(os.path.join(args.name, "requirements.txt"), "w", encoding="utf-8").write(
    "\n".join(packages) + "\n"
)
open(os.path.join(args.name, "src", "main.py"), "w", encoding="utf-8").write(
    "print('start here')\n"
)
print("Created", args.name)
