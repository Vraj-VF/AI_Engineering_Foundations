import time


def stream_response(text):
    for token in text.split():
        print(token, end=" ", flush=True)
        time.sleep(0.03)
    print()


def main():
    print("Local streaming adapter. Type quit to stop.")
    while True:
        prompt = input("You: ")
        if prompt == "quit":
            break
        print("Assistant: ", end="")
        stream_response("Local response to " + prompt)


if __name__ == "__main__":
    main()
