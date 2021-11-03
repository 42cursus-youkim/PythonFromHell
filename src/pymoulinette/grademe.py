#!/usr/bin/python3
from pathlib import Path
from shutil import copytree
from sys import argv

import pytest

pkg = Path("src/pymoulinette")
temp = pkg / "temp"
test = pkg / "tests"


def is_valid_submit(submit: Path):
    if not submit.is_dir():
        print(f"given path {submit} is not a valid directory!")
    elif (s := len([ex for ex in submit.glob("ex")])) != (
        t := len([ex for ex in (test / submit.name).glob("ex")])
    ):
        print(f"your {s:02} exes are not same as expected number {t:02}!!")
    else:
        return True
    return False


def main():
    submit = Path(argv[1])
    if not is_valid_submit(submit):
        return
    day, tday = temp / submit.name, test / submit.name
    copytree(submit, day, dirs_exist_ok=True)
    pytest.main(args=[str(day), str(tday)])


if __name__ == "__main__":
    if len(argv) == 2:
        main()
    else:
        print("Usage: [python3] grademe.py <submit path>")
