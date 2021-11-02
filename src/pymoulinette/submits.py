from dataclasses import dataclass, field
from pathlib import Path
from sys import argv
from typing import List

from utils import Day, Ex, err

ANSWERS = Path(__file__).parent.parent.parent / "answers"


@dataclass
class Submits:
    """holds ex Path for given day, indexable"""

    _input: str = field(repr=False)
    path: Path = field(init=False)
    exlist: List[Ex] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.path = self._parsed_path
        self.exlist = [path for path in self.path.glob("ex*")]

        if not len(self.exlist):
            err(f"there isn't a single ex inside <{self.path}>!")

    @property
    def _parsed_path(self) -> Path:
        result = Path(self._input)
        del self._input
        return result

    @property
    def __len__(self) -> int:
        return len(self.exlist)

    def __getitem__(self, item: int) -> List[Path]:
        """Returns list of python file from given ex index"""
        return [py for py in self.exlist[item].glob("*.py")]


@dataclass
class Answers(Submits):
    """Answers"""

    @property
    def _parsed_path(self) -> Path:
        result = ANSWERS / Path(self._input).name
        del self._input
        return result


if __name__ == "__main__":
    submit = Submits("src/pymoulinette/day00")
    answer = Answers("day00")
    print(submit)
    print(answer)
