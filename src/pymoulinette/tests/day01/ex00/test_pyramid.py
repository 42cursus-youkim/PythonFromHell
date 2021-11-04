def answer(num):
    if num < 0:
        return ValueError
    for i in range(num):
        print(" " * (num - i) + "*" * (2 * i + 1))


# answer(5)

# def submit(num):
#     if num < 0:
#         return ValueError
#     for i in range(num):
#         print(' ' * (num - i) + '*' * (2 * i + 1))

from random import randint

import pytest


@pytest.mark.parametrize("temp", [randint(0, 999) for _ in range(20)])
def test_get_set(temp, capsys):
    answer(temp)
    ans_res = capsys.readouterr().out
    submit(temp)
    sub_res = capsys.readouterr().out
    assert ans_res == sub_res


if __name__ == "__main__":
    pytest.main()
