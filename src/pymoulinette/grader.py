from pathlib import Path
from sys import argv
from typing import List

from .submits import Answers, Submits
from .utils import Day, Ex, err


class Grader:
    def __init__(self, name):
        self.name = Path(name).name.upper()
        self.submit, self.answer = Submits(name), Answers(name)

    def __str__(self):
        return f"Grader loaded with submits and answers from <{self.name}>"

    def grade(self):
        for ex_a, ex_s in zip(self.answer, self.submit):
            self.grade_ex(ex_a, ex_s)

    def grade_exlist(self, answers: List[Ex], submits: List[Ex]):
        for py_s, py_a in zip(answers, submits):
            self.grade_ex(py_a, py_s)

    def grade_ex(self, answer: Ex, submit: Ex):
        raise NotImplementedError("TODO")
