from math import ceil


def answer(n1, n2):
    for num in range(n1, n2 + 1):
        if num % 2:
            yield num
        else:
            pass


# def submit(n1, n2):
#     for num in range(n1, n2 + 1):
#         if (num % 2):
#             yield num
#         else:
#             pass

# n1 = 1
# n2 = 9
# g = geneclass(n1, n2)
# for i in range(ceil((n2 - n1 + 1)/2)):
#     print(next(g))

from random import randint
import pytest

num1_lst = list(range(10))[randint(0, 10)]
num2_lst = list(range(10, 100))[randint(0, 90)]


@pytest.mark.parametrize("n1, n2", [[num1_lst, num2_lst] for _ in range(10)])
def test_get_set(n1, n2):
    ans = answer(n1, n2)
    sub = submit(n1, n2)
    for _ in range(ceil((n2 - n1 + 1) / 2)):
        assert next(ans) == next(sub)


if __name__ == "__main__":
    pytest.main()
