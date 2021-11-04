def answer(line):
    return eval(line)


def submit(line):
    return eval(line)


# answer("round(3.14)")

from random import randint

import pytest

param = ["abs(-3)", "1+2", "10-7", "0", "3.14*7678+9-1/123"]


@pytest.mark.parametrize("line", [param[i] for i in range(len(param))])
def test_get_set(line):
    assert answer(line) == submit(line)


if __name__ == "__main__":
    pytest.main()
