from math import gcd

def answer(num1, num2):
    print(f"gcd : {gcd(num1, num2)}")
    print(f"lcm : {int(num1*num2/gcd(num1, num2))}")

def submit(num1, num2):
    print(f"gcd : {gcd(num1, num2)}")
    print(f"lcm : {int(num1*num2/gcd(num1, num2))}")

# answer(38 ,152)

from random import sample

import pytest

param = [sample(range(-1000, 1000), 2) for _ in range(20)]
@pytest.mark.parametrize("temp1, temp2", param)
def test_get_set(temp1, temp2, capsys):
    answer(temp1, temp2)
    ans_res = capsys.readouterr().out
    submit(temp1, temp2)
    sub_res = capsys.readouterr().out
    assert ans_res == sub_res

if __name__ == "__main__":
    pytest.main()