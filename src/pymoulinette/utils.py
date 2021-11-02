from typing import Type

RED = "\033[1;31m"
END = "\033[0m"


def err(msg: str) -> None:
    print(f"{RED} Error: {msg}{END}")
    exit(1)


if __name__ == "__main__":
    err("test")
