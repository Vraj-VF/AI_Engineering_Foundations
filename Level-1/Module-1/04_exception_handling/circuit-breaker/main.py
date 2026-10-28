import time


class CircuitOpenError(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failures, cooldown):
        self.failures_allowed = failures
        self.cooldown = cooldown
        self.failures = 0
        self.opened_at = None

    def call(self, function):
        if self.opened_at is not None and time.time() - self.opened_at < self.cooldown:
            raise CircuitOpenError("circuit is open")
        if self.opened_at is not None:
            self.opened_at = None
            print("half-open test call")
        try:
            result = function()
            self.failures = 0
            return result
        except ConnectionError:
            self.failures += 1
            if self.failures >= self.failures_allowed:
                self.opened_at = time.time()
            raise


def main():
    breaker = CircuitBreaker(2, 5)

    def unavailable():
        raise ConnectionError("service unavailable")

    for _ in range(3):
        try:
            print(breaker.call(unavailable))
        except (ConnectionError, CircuitOpenError) as error:
            print(error)


if __name__ == "__main__":
    main()
