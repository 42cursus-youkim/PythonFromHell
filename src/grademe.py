# from pymoulinette import Grader

# if __name__ == "__main__":
#     grader = Grader("src/pymoulinette/day00")
#     print(grader)
#     grader.grade()

from pathlib import Path
from sys import argv

import pytest

if __name__ == "__main__":
    print(Path(".").resolve())
    pytest.main(args=["../day00", "tests/day00"])
    # if len(argv) != 2:
    #     print("no directory specified!") or exit(1)
    # print("the directory to open", argv[1])
