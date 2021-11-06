def answer(n):
    if n < 0:
        return ValueError
    for num in range(1, n + 1):
        if not (num % 3):
            print("fizz")
        if not (num % 5):
            print("buzz")
        if num % 3 and num % 5:
            print(num)


# def submit(n):
#     if n < 0:
#         return ValueError
#     for num in range(1, n + 1):
#         if not (num % 3):
#             print("fizz")
#         if not (num % 5):
#             print("buzz")
#         if (num % 3 and num % 5):
#             print(num)

# answer(15)

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
