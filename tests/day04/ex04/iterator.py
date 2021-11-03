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

# fruits = ("apple", "banana", "cherry")
# iter = answer(fruits)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))