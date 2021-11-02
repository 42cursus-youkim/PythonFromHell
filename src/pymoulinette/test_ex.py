from typing import Any, Callable, Tuple

import pytest

from utils import END, RED


def answer():
    print("Hello World!")


def submit():
    print("Hello World!")


def r(s: str) -> str:
    return RED + s + END


@pytest.fixture
def get_funcs() -> Tuple[Callable, Callable]:
    return answer, submit


params = [((), {}) for _ in range(100)]


@pytest.mark.parametrize("args, kwargs", params)
def test_answer(capsys, args, kwargs, get_funcs):
    answer, submit = get_funcs
    a_result = answer(*args, **kwargs)
    a_capt = capsys.readouterr()
    s_result = submit(*args, **kwargs)
    s_capt = capsys.readouterr()

    assert s_result == a_result, r("RETURN from function are not same!!")
    assert s_capt.out == a_capt.out, r("STDOUT is not same!!")
    assert s_capt.err == a_capt.err, r("STDERR is not same!!")


if __name__ == "__main__":
    pytest.main()
