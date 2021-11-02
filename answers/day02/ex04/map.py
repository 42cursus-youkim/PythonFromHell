from typing import List


def answer(list_int : List[int]) -> List:
    return list(map(lambda x : x ** 2, list_int))