from typing import Any


def answer(*args: Any, **kwargs: Any) -> str:
    ans: str = ""
    max: int = 0
    if len(args) > len(kwargs):
        for i in args:
            if len(str(i)) > max:
                ans = str(i)
    elif len(args) < len(kwargs):
        for j, k in kwargs.items():
            if len(str(k)) > max:
                ans = str(k)
    else:
        ans = "42"
    return ans


import pytest


@pytest.mark.parametrize()
def test_answer(temp):

    assert test_answer == answer(42, a="24", b=4422, c="424242424242")


if __name__ == "__main__":
    pytest.main()
