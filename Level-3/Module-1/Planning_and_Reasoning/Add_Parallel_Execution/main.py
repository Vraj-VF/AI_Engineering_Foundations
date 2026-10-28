from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def work(task):
    time.sleep(0.02)
    return task.upper()


def run_parallel(tasks):
    with ThreadPoolExecutor(max_workers=len(tasks)) as pool:
        futures = {pool.submit(work, task): task for task in tasks}
        return {
            task: future.result()
            for future, task in ((future, futures[future]) for future in as_completed(futures))
        }


def main():
    tasks = ["research", "collect metrics", "draft outline"]
    started = time.perf_counter()
    sequential = [work(task) for task in tasks]
    sequential_time = time.perf_counter() - started
    started = time.perf_counter()
    parallel = run_parallel(tasks)
    parallel_time = time.perf_counter() - started
    print(
        {
            "sequential": sequential,
            "parallel": parallel,
            "speedup": round(sequential_time / parallel_time, 2),
        }
    )


if __name__ == "__main__":
    main()
