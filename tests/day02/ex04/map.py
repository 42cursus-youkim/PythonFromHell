from typing import List


def answer(list_int : List[int]) -> List:
    return list(map(lambda x : x ** 2, list_int))

import pytest

list_int = [
    [
        1, 2, 3, 4, 5
    ],
    [
        100, 50, 0, -50, -100
    ],
    [
        
    ]
]

@pytest.mark.parametrize("temp", list_int)
def test_answer(temp):
    a = list(map(lambda x : x ** 2, temp))

    assert a == answer(temp)

if __name__ == "__main__":
    pytest.main()