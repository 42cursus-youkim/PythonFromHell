def answer():
    for word in range(ord("a"), ord("z") + 1):
        print(chr(word))


# def submit():
#     for word in range(ord('a'), ord('z')+1):
#         print(chr(word))

# answer()

import pytest


def test_get_set(capsys):
    answer()
    ans_res = capsys.readouterr().out
    submit()
    sub_res = capsys.readouterr().out
    assert ans_res == sub_res


if __name__ == "__main__":
    pytest.main()
