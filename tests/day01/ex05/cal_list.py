def answer(oper, num_list):
    ans = 0
    if oper == '+':
        for num in num_list:
            ans += num
    elif oper == '-':
        for num in num_list:
            ans -= num
    elif oper == '*':
        for num in num_list:
            ans *= num
    elif oper == '/':
        if 0 in num_list:
            return ValueError
        for num in num_list:
            ans /= num
    else:
        return ValueError
    print(ans)

def submit(oper, num_list):
    ans = 0
    if oper == '+':
        for num in num_list:
            ans += num
    elif oper == '-':
        for num in num_list:
            ans -= num
    elif oper == '*':
        for num in num_list:
            ans *= num
    elif oper == '/':
        if 0 in num_list:
            return ValueError
        for num in num_list:
            ans /= num
    else:
        return ValueError
    print(ans)

# answer('+', [1,2,3,4,5,6,7])

from random import sample

import pytest

param= [sample(range(-1000, 1000), n) for n in range(1, 100)]
@pytest.mark.parametrize("temp", param)
def test_get_set(temp, capsys):
    for oper in ['+','-','*','/']:
        answer(oper, list(temp))
        ans_res = capsys.readouterr().out
        submit(oper, list(temp))
        sub_res = capsys.readouterr().out
        assert ans_res == sub_res

if __name__ == "__main__":
    pytest.main()