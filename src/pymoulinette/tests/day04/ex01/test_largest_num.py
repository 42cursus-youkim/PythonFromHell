def answer(num_lst):
    num_lst_edit = [num * 3 for num in num_lst]
    num_lst = [num[: int(len(num) / 3)] for num in sorted(num_lst_edit, reverse=True)]
    number = ""
    for num in num_lst:
        number += num
    return number


# def submit(num_lst):
#     num_lst_edit = [num*3 for num in num_lst]
#     num_lst = [num[:int(len(num)/3)] for num in sorted(num_lst_edit, reverse=True)]
#     number = ""
#     for num in num_lst:
#         number += num
#     return number

# num_lst = ["3", "300", "303", "9"]
# answer(num_lst)


from random import randint

import pytest

param = [str(randint(1, 1000)) for _ in range(randint(1, 30))]


@pytest.mark.parametrize("num_lst", [param for _ in range(10)])
def test_get_set(num_lst):
    assert answer(num_lst) == submit(num_lst)


if __name__ == "__main__":
    pytest.main()
