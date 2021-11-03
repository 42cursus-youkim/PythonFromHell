def answer(spam: int):
    print(spam)
    print(hex(id(spam)))
    print(type(spam))
    print(spam + 11)


from random import randint

import pytest


@pytest.mark.parametrize("temp", [randint(-10000, 10000) for _ in range(100)])
def test_answer(temp, capsys):
    answer(temp)
    assert capsys.readouterr().out == str(temp)+"\n"+str(hex(id(temp)))+"\n"+str(type(temp))+"\n"+str(temp+11)+"\n"

if __name__ == "__main__":
    pytest.main()