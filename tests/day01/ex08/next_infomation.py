def answer(info, info_news):
    ans = [tuple(person) for person in info_news]
    for person in info:
        person_lst = list(person)
        person_lst[-1] += 1
        if not person_lst[-1] >= 5:
            ans.append(tuple(person_lst))
    return tuple(sorted(ans, key=lambda x: x[0]))


# info = [['amy', 157, 59, 1], ['jake', 184, 81, 4], ['norman', 182, 86, 2]]
# info_news = [['rachel',178,63,1]]
# print(answer(info, info_news))


# def submit(info, info_news):
#     ans = [tuple(person) for person in info_news]
#     for person in info:
#         person_lst = list(person)
#         person_lst[-1] += 1
#         if not person_lst[-1] >= 5:
#             ans.append(tuple(person_lst))
#     return tuple(sorted(ans, key=lambda x: x[0]))

from random import randint

import pytest

name = ['Liam', 'Olivia',
        'Noah', 'Emma',
        'Oliver', 'Ava',
        'Elijah', 'Charlotte',
        'William', 'Sophia',
        'James', 'Amelia',
        'Benjamin', 'Isabella',
        'Lucas', 'Mia',
        'Henry', 'Evelyn',
        'Alexander', 'Harper']

param = []
for _ in range(8):
    param.append([name[randint(0, 19)], randint(140, 190), randint(40, 120), randint(1, 4)])

new_param = [[name[randint(0, 19)], randint(140, 190), randint(40, 120), randint(1, 4)]]

@pytest.mark.parametrize("lst, lst_new", [[param, new_param] for _ in range(6)])
def test_get_set(lst, lst_new):
    assert answer(lst, lst_new) == submit(lst, lst_new)

if __name__ == "__main__":
    pytest.main()