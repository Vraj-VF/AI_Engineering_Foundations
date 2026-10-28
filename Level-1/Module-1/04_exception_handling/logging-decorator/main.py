import logging
import traceback

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def log_calls(function):
    def wrapped(*args, **kwargs):
        logging.info("calling %s", function.__name__)
        try:
            return function(*args, **kwargs)
        except Exception:
            logging.error("failure in %s", function.__name__)
            traceback.print_exc()
            raise

    return wrapped


@log_calls
def divide(a, b):
    return a / b


@log_calls
def uppercase(text):
    return text.upper()


@log_calls
def item(values, index):
    return values[index]


def main():
    for function, args in [
        (divide, (1, 0)),
        (uppercase, (input("Text: "),)),
        (item, (["first"], 2)),
    ]:
        try:
            print(function(*args))
        except (ZeroDivisionError, IndexError):
            print("Function failed")


if __name__ == "__main__":
    main()
