import asyncio
import time


async def process(item):
    started = time.perf_counter()
    try:
        await asyncio.sleep(0.05)
        return True, time.perf_counter() - started
    except Exception:
        return False, time.perf_counter() - started


async def main():
    items = input("Items separated by commas: ").split(",")
    results = await asyncio.gather(*(process(item) for item in items))
    successes = sum(result[0] for result in results)
    print("success rate", successes / len(results) if results else 0)
    print(
        "average latency",
        sum(result[1] for result in results) / len(results) if results else 0,
    )


if __name__ == "__main__":
    asyncio.run(main())
