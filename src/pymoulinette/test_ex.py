from typing import Any, Tuple

import pytest


def answer():
    print("Hello World!")


def submit():
    print("Hello World?")
    return 111


def test_answer(capsys):
    a_result = answer()
    a_capt = capsys.readouterr()
    s_result = submit()
    s_capt = capsys.readouterr()

    assert s_result == a_result, "returns from function are not same!!"
    assert s_capt.out == a_capt.out, "stdout is not same!!"
    assert s_capt.err == a_capt.err, "stderr is not same!!"


if __name__ == "__main__":
    pytest.main()
