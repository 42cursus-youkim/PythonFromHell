from dataclasses import dataclass, field
from pathlib import Path
from sys import argv
from typing import List

from utils import err

Day, Ex = Path, Path


ANSWERS = Path(__file__).parent.parent.parent / "answers"


@dataclass
class Projects:
    """holds ex files for given day, indexable"""

    _input: str = field(repr=False)
    path: Path = field(init=False)
    exlist: List[Ex] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.path = Path(self._input)
        self.exlist = [path for path in self.path.glob("ex*")]

    def __len__(self) -> int:
        return len(self.exlist)


class Answers(Projects):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.path = ANSWERS / self.path.name


class Grader:
    def __init__(self, name: str):
        self.set_path(Path(name))
        self.set_ex()
        self.check_answers()

    def get_ex(self, path: Path) -> List[Ex]:
        return [path for path in path.glob("ex*")]

    def set_path(self, path: Path) -> None:
        self.submit: Day = path
        self.answer: Day = ANSWERS / path.name
        if not all(
            [
                self.answer.exists() and self.answer.is_dir(),
                self.submit.exists() and self.submit.is_dir(),
            ]
        ):
            err(f"{self.submit.resolve()}: invalid path!")

    def set_ex(self):
        self.answer_ex: List[Ex] = self.get_ex(self.answer)
        self.submit_ex: List[Ex] = self.get_ex(self.submit)
        if (a := len(self.answer_ex)) != (s := len(self.submit_ex)):
            err(
                f"ex mismatch! expected {a} answers but got {s} answers instead"
            )

    def check_answers(self):
        pass

    def __repr__(self):
        return "\n".join(
            [
                f"would grade: <{self.submit}>",
                f"holds answers: <{self.day}>",
                f"list of ex(answer): <{[ex.name for ex in self.answer_ex]}>",
                f"list of ex(submit): <{[ex.name for ex in self.submit_ex]}>",
            ]
        )


if __name__ == "__main__":
    # submit = Projects("src/pymoulinette/day00")
    submit = Answers("src/pymoulinette/day00")
    print(submit)
    # grader = Grader("src/pymoulinette/day00")
    # print(grader)
