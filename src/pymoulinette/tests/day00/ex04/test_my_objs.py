from typing import Any


def answer(obj: Any):
    print(dir(obj))


import pytest


test_case = [
    12,
    -300,
    "hello",
    str,
    list,
    tuple,
    type(float),
    [123, "134"],
    {"a": 3, "b": "34bsdv"},
]


@pytest.mark.parametrize("temp", test_case)
def test_answer(temp, capsys):
    answer(temp)
    assert capsys.readouterr().out == str(dir(temp)) + "\n"


if __name__ == "__main__":
    pytest.main()
