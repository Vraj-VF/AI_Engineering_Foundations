import asyncio
import time


class TokenBucket:
    def __init__(self, rate):
        self.rate = rate
        self.tokens = rate
        self.updated = time.monotonic()

    async def acquire(self):
        while self.tokens < 1:
            await asyncio.sleep(0.05)
            self.tokens = min(
                self.rate, self.tokens + (time.monotonic() - self.updated) * self.rate
            )
            self.updated = time.monotonic()
        self.tokens -= 1


async def call(number, bucket):
    await bucket.acquire()
    return "call " + str(number)


async def main():
    bucket = TokenBucket(5)
    results = await asyncio.gather(*(call(number, bucket) for number in range(20)))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
