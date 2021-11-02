from pathlib import Path
from sys import argv
from typing import List

from submits import Answers, Submits
from utils import Day, Ex, err


class Grader:
    def __init__(self, name):
        self.name = Path(name).name.upper()
        self.submit, self.answer = Submits(name), Answers(name)

    def __str__(self):
        return f"Grader loaded with submits and answers from <{self.name}>"


if __name__ == "__main__":
    grader = Grader("src/pymoulinette/day00")
    print(grader)
