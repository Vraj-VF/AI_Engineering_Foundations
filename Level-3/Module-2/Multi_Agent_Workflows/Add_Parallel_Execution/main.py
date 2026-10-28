from concurrent.futures import ThreadPoolExecutor


def research(task):
    return "research:" + task


def code(task):
    return "code:" + task


def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        outputs = list(pool.map(lambda fn: fn("known task"), (research, code)))
    print({"parallel_outputs": outputs, "review": "review both outputs"})


if __name__ == "__main__":
    main()
