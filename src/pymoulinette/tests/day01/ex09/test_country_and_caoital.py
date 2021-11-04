def answer(country, capital):
    couple = sorted([[c, p] for c, p in zip(*[country, capital])], key=lambda x: x[0])
    ans = {}
    for cou, cap in couple:
        try:
            ans[cou] = cap
        except:
            pass
    return ans

# def submit(country, capital):
#     couple = sorted([[c, p] for c, p in zip(*[country, capital])], key=lambda x: x[0])
#     ans = {}
#     for cou, cap in couple:
#         try:
#             ans[cou] = cap
#         except:
#             pass
#     return ans

# country = ['korea','Singapore','Kenya','Iceland','France','Kenya']
# capital = ['Seoul','Singapore','Nairobi','Reykjavik','Paris','Nairobi']
# answer(country, capital)

from random import randint

import pytest

country = ['America','Austria','Australia','Brazil','Canada','China','Denmark',
            'Egypt','Finland','France','Germany','Greece','Israel','Italy',
            'Japan','Korea','Mexico','Netherlands','New Zealand','Norway','Peru']
capital = ['Washington','Vienna','Canberra','Brasilia','Ottawa','Beijing',
            'Copenhagen','Cairo','Helsinki','Paris','Berlin','Athens',
            'Jerusalem','Rome','Tokyo','Seoul','Mexico city','Amsterdam',
            'Wellington','Oslo','Lima']

country_lst = []
capital_lst = []
for _ in range(8):
    idx = randint(0,21)
    country_lst.append(country[idx])
    capital_lst.append(capital[idx])

@pytest.mark.parametrize("cou_lst, cap_lst", [[country_lst, capital_lst] for _ in range(6)])
def test_get_set(cou_lst, cap_lst):
    assert answer(cou_lst, cap_lst) == submit(cou_lst, cap_lst)

if __name__ == "__main__":
    pytest.main()
