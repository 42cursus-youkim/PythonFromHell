def answer(str_lst):
    class iterclass(object):
        def __init__(self, str_lst):
            self.idx = 0
            self.str_lst = str_lst
        
        def __iter__(self):
            return self

        def __next__(self):
            if (len(self.str_lst) <= self.idx):
                return StopIteration
            else:
                self.idx += 1
                return self.str_lst[self.idx - 1]
    return (iterclass(str_lst))

# def submit(str_lst):
#     class iterclass(object):
#         def __init__(self, str_lst):
#             self.idx = 0
#             self.str_lst = str_lst
        
#         def __iter__(self):
#             return self

#         def __next__(self):
#             if (len(self.str_lst) <= self.idx):
#                 return StopIteration
#             else:
#                 self.idx += 1
#                 return self.str_lst[self.idx - 1]
#     return (iterclass(str_lst))

# fruits = ("apple", "banana", "cherry")
# iter = answer(fruits)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))

from random import randint
import pytest

fruit_lst = ['apple', 'banana', 'charry', 'dragon fruit', 'escarole', 'figs', 'grapes', 'hanrabong',
                'kiwi', 'melon', 'nectarine', 'orange']
@pytest.mark.parametrize("str_lst", [[fruit_lst[idx] for idx in range(1, randint(2,len(fruit_lst)))] for _ in range(10)])
def test_get_set(str_lst):
    ans = answer(str_lst)
    sub = submit(str_lst)
    for _ in range(len(str_lst) + 1):
        assert next(ans) == next(sub)

if __name__ == "__main__":
    pytest.main()