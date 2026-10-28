import asyncio


async def response_stream(text):
    for token in text.split():
        await asyncio.sleep(0.05)
        yield token


async def main():
    async for token in response_stream(input("Response: ")):
        print(token, end=" ", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(main())
