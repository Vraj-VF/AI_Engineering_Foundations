import random
import time


def retry_with_backoff(max_attempts):
    def decorate(function):
        def wrapped():
            for attempt in range(max_attempts):
                try:
                    return function()
                except ValueError as error:
                    if attempt == max_attempts - 1:
                        raise error
                    delay = 2**attempt
                    print(f"Retrying in {delay} seconds")
                    time.sleep(delay)

        return wrapped

    return decorate


@retry_with_backoff(4)
def unreliable_task():
    if random.randint(1, 3) != 1:
        raise ValueError("temporary failure")
    return "completed"


def main():
    try:
        print(unreliable_task())
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
