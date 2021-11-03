from pathlib import Path
from typing import Any, Callable, Tuple

import pytest


# submit = get_submit(Path("day00.ex00.hello.py"))

# print(modules.keys())
# submit()
# exit(0)
from utils import reds as r


def answer():
    # raise ValueError
    print(1)

def submit():
    # raise ValueError
    print(1)
    print(2)
    print('error')


@pytest.fixture
def get_funcs() -> Tuple[Callable, Callable]:
    return answer, submit


params = [([], {})]


@pytest.mark.parametrize("args, kwargs", params)
def test_answer(capsys, args, exception, kwargs, get_funcs):
    if exception:
        with pytest.raises(ValueError):
            answer, submit = get_funcs
            a_result = answer(*args, **kwargs)
            a_capt = capsys.readouterr()

            s_result = submit(*args, **kwargs)
            s_capt = capsys.readouterr()
            assert s_result == a_result, r("RETURN from function are not same!!")
            assert s_capt.out == a_capt.out, r("STDOUT is not same!!")
            assert s_capt.err == a_capt.err, r("STDERR is not same!!")
    else:
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
