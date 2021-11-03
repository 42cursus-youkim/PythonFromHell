from pathlib import Path
from typing import Type

Day = Path
Ex = Path

RED = "\033[1;31m"
END = "\033[0m"


def err(msg: str) -> None:
    print(f"{RED} Error: {msg}{END}")
    exit(1)


def reds(s: str) -> str:
    return RED + s + END


if __name__ == "__main__":
    err("test")
