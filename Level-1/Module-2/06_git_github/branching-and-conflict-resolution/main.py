import subprocess


def main():
    branch = input("Feature branch: ")
    result = subprocess.run(
        ["git", "switch", "-c", branch], text=True, capture_output=True
    )
    print(result.stdout or result.stderr)
    print(
        "Commit the feature, switch to main, make a conflicting edit, then merge and resolve it."
    )


if __name__ == "__main__":
    main()
